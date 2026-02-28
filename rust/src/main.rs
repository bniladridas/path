use clap::{Parser, Subcommand};
use crossterm::{
    event::{self, Event, KeyCode, KeyEventKind},
    terminal::{disable_raw_mode, enable_raw_mode, Clear, ClearType},
};
use ratatui::{
    backend::CrosstermBackend,
    layout::{Constraint, Direction, Layout},
    style::{Color, Style},
    widgets::{Block, Borders, Paragraph},
    Frame, Terminal,
};
use reqwest::Client;
use std::env;
use std::fs::File;
use std::io::Write;
use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::Arc;

#[derive(Parser)]
#[command(name = "harper")]
#[command(about = "CLI for Harper - AI-powered media exploration", long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    Search {
        query: String,
    },
    Image {
        #[arg(short, long)]
        prompt: String,

        #[arg(short, long, default_value = "output.png")]
        output: Option<String>,
    },
    Tui,
}

struct AppState {
    pub started: bool,
    pub query: String,
    pub response: String,
    pub loading: bool,
    pub error: Option<String>,
}

impl AppState {
    fn new() -> Self {
        Self {
            started: false,
            query: String::new(),
            response: String::new(),
            loading: false,
            error: None,
        }
    }
}

fn render_welcome(frame: &mut Frame) {
    let chunks = Layout::default()
        .direction(Direction::Vertical)
        .constraints([Constraint::Min(1), Constraint::Length(3)])
        .split(frame.area());

    let prompt = Paragraph::new("").block(Block::default().borders(Borders::NONE));
    frame.render_widget(prompt, chunks[0]);

    let input = Paragraph::new("")
        .style(Style::default().fg(Color::DarkGray))
        .block(
            Block::default()
                .borders(Borders::ALL)
                .title(" type to search "),
        );
    frame.render_widget(input, chunks[1]);
}

fn render_search_ui(frame: &mut Frame, app: &AppState) {
    let chunks = Layout::default()
        .direction(Direction::Vertical)
        .constraints([Constraint::Length(3), Constraint::Min(0)])
        .split(frame.area());

    let input = Paragraph::new(app.query.as_str())
        .style(Style::default().fg(Color::White))
        .block(Block::default().borders(Borders::ALL).title(" "));
    frame.render_widget(input, chunks[0]);

    let response_text = if app.loading {
        "Loading..."
    } else if let Some(ref err) = app.error {
        err.as_str()
    } else {
        app.response.as_str()
    };

    let response_style = if app.loading {
        Style::default().fg(Color::Yellow)
    } else if app.error.is_some() {
        Style::default().fg(Color::Red)
    } else {
        Style::default().fg(Color::Green)
    };

    let response = Paragraph::new(response_text)
        .style(response_style)
        .block(Block::default().borders(Borders::ALL));
    frame.render_widget(response, chunks[1]);
}

async fn run_tui() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = env::var("GEMINI_API_KEY").expect("GEMINI_API_KEY not set");
    let client = Client::new();

    enable_raw_mode()?;
    let stdout = std::io::stdout();
    let backend = CrosstermBackend::new(stdout);
    let mut terminal = Terminal::new(backend)?;

    let quit = Arc::new(AtomicBool::new(false));
    let app = Arc::new(std::sync::Mutex::new(AppState::new()));
    let app_clone = app.clone();
    let quit_clone = quit.clone();

    std::thread::spawn(move || loop {
        if event::poll(std::time::Duration::from_millis(50)).unwrap() {
            if let Event::Key(key) = event::read().unwrap() {
                if key.kind == KeyEventKind::Press {
                    let mut app = app_clone.lock().unwrap();
                    match key.code {
                        KeyCode::Char(c) => {
                            if !app.started {
                                app.started = true;
                            }
                            app.query.push(c);
                        }
                        KeyCode::Backspace => {
                            app.query.pop();
                        }
                        KeyCode::Enter => {
                            let query = app.query.clone();
                            if !query.is_empty() && !app.loading {
                                app.loading = true;
                                app.response.clear();
                                app.error = None;
                                drop(app);

                                let client = client.clone();
                                let api_key = api_key.clone();
                                let app = app_clone.clone();

                                std::thread::spawn(move || {
                                    let rt = tokio::runtime::Runtime::new().unwrap();
                                    rt.block_on(async {
                                        let result = search_gemini(&client, &api_key, &query).await;
                                        let mut app = app.lock().unwrap();
                                        app.loading = false;
                                        match result {
                                            Ok(resp) => {
                                                app.response = resp;
                                            }
                                            Err(e) => {
                                                app.error = Some(e);
                                            }
                                        }
                                    });
                                });
                            }
                        }
                        KeyCode::Esc => {
                            if app.query.is_empty() {
                                quit_clone.store(true, Ordering::SeqCst);
                            } else {
                                app.query.clear();
                                app.started = false;
                                app.response.clear();
                                app.error = None;
                            }
                        }
                        _ => {}
                    }
                }
            }
        }
    });

    loop {
        terminal.draw(|f| {
            let app = app.lock().unwrap();
            if !app.started {
                render_welcome(f);
            } else {
                render_search_ui(f, &app);
            }
        })?;

        if quit.load(Ordering::SeqCst) {
            break;
        }
    }

    disable_raw_mode()?;
    terminal.show_cursor()?;
    print!("{}", Clear(ClearType::All));
    Ok(())
}

async fn search_gemini(client: &Client, api_key: &str, query: &str) -> Result<String, String> {
    let prompt = build_prompt(query);

    let request_body = serde_json::json!({
        "contents": [{
            "parts": [{ "text": prompt }]
        }],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 1024
        }
    });

    let response = client
        .post("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent")
        .query(&[("key", api_key)])
        .json(&request_body)
        .send()
        .await
        .map_err(|e| e.to_string())?;

    if !response.status().is_success() {
        let body = response.text().await.map_err(|e| e.to_string())?;
        return Err(body);
    }

    let resp: serde_json::Value = response.json().await.map_err(|e| e.to_string())?;

    extract_gemini_text(&resp)
}

fn build_prompt(query: &str) -> String {
    format!(
        "You are Harper, an AI that helps people discover media like movies, music, books, and games. \
        Respond in a conversational, helpful way. Keep responses concise but informative.\n\n\
        User query: {}",
        query
    )
}

fn extract_gemini_text(resp: &serde_json::Value) -> Result<String, String> {
    let candidates = resp
        .get("candidates")
        .and_then(|c| c.as_array())
        .ok_or("no candidates")?;

    for candidate in candidates {
        let parts = candidate
            .get("content")
            .and_then(|c| c.get("parts"))
            .and_then(|p| p.as_array())
            .ok_or("no parts")?;

        for part in parts {
            if let Some(text) = part.get("text").and_then(|t| t.as_str()) {
                return Ok(text.to_string());
            }
        }
    }

    Err("no text found".to_string())
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    dotenv::dotenv().ok();

    let cli = Cli::parse();

    match cli.command {
        Commands::Search { query } => {
            let api_key = env::var("GEMINI_API_KEY").expect("GEMINI_API_KEY not set");
            let client = Client::new();

            println!("Searching for: {}\n", query);

            let response = search_gemini(&client, &api_key, &query).await?;

            println!("{}", response);
        }
        Commands::Image { prompt, output } => {
            let api_key = env::var("GEMINI_API_KEY").expect("GEMINI_API_KEY not set");
            let client = Client::new();

            let out = output.unwrap_or_else(|| "output.png".to_string());
            println!("Generating image: {}\n", prompt);

            let request_body = serde_json::json!({
                "contents": [{
                    "parts": [{ "text": prompt }]
                }],
                "generationConfig": {
                    "responseModalities": ["IMAGE", "TEXT"]
                }
            });

            let response = client
                .post("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:streamGenerateContent")
                .query(&[("key", &api_key)])
                .json(&request_body)
                .send()
                .await?;

            if !response.status().is_success() {
                let status = response.status();
                let body = response.text().await?;
                eprintln!("Error: {} - {}", status, body);
                return Ok(());
            }

            let body_text = response.text().await?;

            for line in body_text.lines() {
                if line.is_empty() {
                    continue;
                }
                if let Ok(chunk) = serde_json::from_str::<serde_json::Value>(line) {
                    if let Some(candidates) = chunk.get("candidates").and_then(|c| c.as_array()) {
                        for candidate in candidates {
                            if let Some(content) = candidate
                                .get("content")
                                .and_then(|c| c.get("parts"))
                                .and_then(|p| p.as_array())
                            {
                                for part in content {
                                    if let Some(inline_data) = part.get("inlineData") {
                                        if let Some(data) =
                                            inline_data.get("data").and_then(|d| d.as_str())
                                        {
                                            let decoded = base64::Engine::decode(
                                                &base64::engine::general_purpose::STANDARD,
                                                data,
                                            )?;

                                            let mut file = File::create(&out)?;
                                            file.write_all(&decoded)?;
                                            println!("Image saved to: {}", out);
                                            return Ok(());
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

            println!("No image generated");
        }
        Commands::Tui => {
            run_tui().await?;
        }
    }

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::{build_prompt, extract_gemini_text};

    #[test]
    fn test_extract_gemini_text_success() {
        let response = r#"{
            "candidates": [{
                "content": {
                    "parts": [{"text": "Test response text"}]
                }
            }]
        }"#;

        let json: serde_json::Value =
            serde_json::from_str(response).expect("valid JSON should parse");
        let result = extract_gemini_text(&json).expect("valid response should extract text");
        assert_eq!(result, "Test response text");
    }

    #[test]
    fn test_extract_gemini_text_multiple_parts() {
        let response = r#"{
            "candidates": [{
                "content": {
                    "parts": [
                        {"text": "First part"},
                        {"text": "Second part"}
                    ]
                }
            }]
        }"#;

        let json: serde_json::Value =
            serde_json::from_str(response).expect("valid JSON should parse");
        let result = extract_gemini_text(&json).expect("valid response should extract text");
        assert_eq!(result, "First part");
    }

    #[test]
    fn test_extract_gemini_text_multiple_candidates() {
        let response = r#"{
            "candidates": [
                {"content": {"parts": []}},
                {"content": {"parts": [{"text": "Second candidate"}]}}
            ]
        }"#;

        let json: serde_json::Value =
            serde_json::from_str(response).expect("valid JSON should parse");
        let result = extract_gemini_text(&json).expect("valid response should extract text");
        assert_eq!(result, "Second candidate");
    }

    #[test]
    fn test_extract_gemini_text_empty_response() {
        let response = r#"{}"#;

        let json: serde_json::Value =
            serde_json::from_str(response).expect("valid JSON should parse");
        let result = extract_gemini_text(&json);
        assert!(result.is_err());
    }

    #[test]
    fn test_extract_gemini_text_empty_candidates() {
        let response = r#"{"candidates": []}"#;

        let json: serde_json::Value =
            serde_json::from_str(response).expect("valid JSON should parse");
        let result = extract_gemini_text(&json);
        assert!(result.is_err());
    }

    #[test]
    fn test_build_prompt_format() {
        let query = "What are some sci-fi books?";
        let prompt = build_prompt(query);

        assert!(prompt.contains("Harper"));
        assert!(prompt.contains("sci-fi books?"));
        assert!(prompt.contains("User query:"));
    }
}
