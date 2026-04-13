**Harper CLI** is a native command-line interface for Harper, designed for AI-powered media exploration. It lets you interactively browse content, run searches directly from the terminal, and even generate images using simple commands. The tool is lightweight and focused on providing a smooth developer-friendly workflow without extra overhead. ⚡

To install it, navigate to the `rust` directory, build the project in release mode, and copy the compiled binary into your local bin directory. After installation, you’ll need to configure your API access by creating a `.env` file from the example template and adding your `GEMINI_API_KEY`. This key can be obtained from Google AI Studio, and once set, the CLI is ready to use. 🛠️

Usage is straightforward. You can launch the interactive terminal UI with `harper tui`, perform quick searches directly from the command line using `harper search "best sci-fi movies"`, or generate images with prompts such as `harper image --prompt "a sunset"`. These commands provide flexible ways to interact depending on whether you prefer an interactive interface or fast one-off queries. 🚀

Inside the TUI, controls are simple and intuitive: typing starts a search, pressing Enter submits your query, and Escape clears the input or exits. This keeps navigation minimal and efficient, making the CLI comfortable for continuous exploration. 🎛️
