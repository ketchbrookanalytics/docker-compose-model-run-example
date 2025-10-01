# docker-compose-model-run-example
Template repository for projects containing a service (web app, API, etc.) and a local LLM (via Docker Model Runner) via Docker Compose

## Features

- 🐳 Dev Container with Docker Compose for consistent development environment
- 🐍 Python 3.12 slim base image
- 🎨 Gradio web interface for chatting with LLMs
- 🤖 OpenAI-compatible API client (works with OpenAI or local LLMs)
- 🛠️ Pre-configured with Python development tools (pylint, black, pytest, etc.)

## Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd docker-compose-model-run-example
   ```

2. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and set your API credentials:
   - For OpenAI: Set `OPENAI_API_KEY` to your API key
   - For local LLM: Set `OPENAI_API_BASE` to your local endpoint (e.g., `http://localhost:8080/v1`)

3. **Open in Dev Container**
   - Open the project in VS Code
   - Click "Reopen in Container" when prompted
   - Or use Command Palette: "Dev Containers: Reopen in Container"

4. **Run the Gradio app**
   ```bash
   python app.py
   ```
   The app will be available at `http://localhost:7860`

## Project Structure

```
.
├── .devcontainer/
│   ├── devcontainer.json    # Dev Container configuration
│   ├── docker-compose.yml   # Docker Compose for dev environment
│   └── Dockerfile           # Python dev environment image
├── app.py                   # Main Gradio application
├── requirements.txt         # Python dependencies
├── .env.example            # Example environment variables
└── README.md               # This file
```

## Configuration

The application is configured via environment variables in the `.env` file:

- `OPENAI_API_KEY`: Your OpenAI API key (or any value for local LLMs)
- `OPENAI_API_BASE`: API endpoint URL
- `MODEL_NAME`: Model identifier to use
- `SYSTEM_PROMPT`: System prompt for the LLM
- `GRADIO_HOST`: Host for Gradio server (default: 0.0.0.0)
- `GRADIO_PORT`: Port for Gradio server (default: 7860)

## Using with Local LLMs

To connect to a local LLM with an OpenAI-compatible API:

1. Start your local LLM service (e.g., Docker Model Runner)
2. Update `.env`:
   ```env
   OPENAI_API_KEY=not-needed-for-local
   OPENAI_API_BASE=http://localhost:8080/v1
   MODEL_NAME=your-local-model-name
   ```
3. Run the app

## Development

The Dev Container includes:
- Python 3.11-slim
- Development tools: pylint, black, autopep8, pytest, ruff
- VS Code Python extensions
- Git and build essentials

## License

MIT
