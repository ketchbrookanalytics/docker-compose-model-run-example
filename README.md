# Docker Compose with Docker Model Runner

Template repository for projects containing a service (web app, API, etc.) and a local LLM (via Docker Model Runner) via Docker Compose

## Features

- 🐳 Dev Container with Docker Compose for consistent development environment
- 🐍 Python 3.12 slim base image
- 🎨 Gradio web interface for chatting with LLMs
- 🤖 OpenAI-compatible API client (works with OpenAI or local LLMs)

## Quick Start

1. **Open in Dev Container**
   - Open the project in VS Code
   - Click "Reopen in Container" when prompted
   - Or use Command Palette: "Dev Containers: Reopen in Container"

4. **Run the Gradio app**
   ```bash
   uv run app.py
   ```
   The app will be available at <http://localhost:8000>

## Using with Local LLMs

You can configure the Docker Model Runner LLM you want to use in the `models` section of `compose.yml`.