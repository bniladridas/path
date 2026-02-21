use clap::{Parser, Subcommand};
use reqwest::Client;
use serde::Deserialize;
use std::env;
use std::fs::File;
use std::io::Write;

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
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    dotenv::dotenv().ok();

    let cli = Cli::parse();
    let api_key = env::var("GEMINI_API_KEY").expect("GEMINI_API_KEY not set");

    let client = Client::new();

    match cli.command {
        Commands::Search { query } => {
            println!("Searching for: {}\n", query);

            let prompt = format!(
                "You are Harper, an AI that helps people discover media like movies, music, books, and games. \
                Respond in a conversational, helpful way. Keep responses concise but informative.\n\n\
                User query: {}",
                query
            );

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

            let resp: serde_json::Value = response.json().await?;

            if let Some(candidates) = resp.get("candidates").and_then(|c| c.as_array()) {
                if let Some(candidate) = candidates.first() {
                    if let Some(content) = candidate
                        .get("content")
                        .and_then(|c| c.get("parts"))
                        .and_then(|p| p.as_array())
                    {
                        for part in content {
                            if let Some(text) = part.get("text").and_then(|t| t.as_str()) {
                                println!("{}", text);
                            }
                        }
                    }
                }
            }
        }
        Commands::Image { prompt, output } => {
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
    }

    Ok(())
}
