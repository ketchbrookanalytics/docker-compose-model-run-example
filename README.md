# Docker Compose with Docker Model Runner

Template repository for projects containing a service (web app, API, etc.) and a local LLM (via Docker Model Runner) via Docker Compose.

The official documentation on using Docker Model Runner with Docker Compose can be found here: <https://docs.docker.com/ai/compose/models-and-compose/>.

## Motivation

We found ourselves constantly following the same pattern of creating a Docker Compose environment with two services: (1) a web application and (2) an API for hosting an open-weights LLM using [ollama](https://github.com/ollama/ollama). When [Docker Model Runner](https://docs.docker.com/ai/model-runner/) was released, it appeared that we may be able to greatly simplify the effort required to stand up the second service. This approach has significantly reduced the configuration required to utilize an open-weights LLM with another Docker container service.

## Features

- 🐳 Dev Container with Docker Compose for consistent development environment
- 🐍 Python 3.12 slim base image
- 🎨 Gradio web interface for chatting with LLMs
- 🤖 OpenAI-compatible API client (works with OpenAI or local LLMs)

## Requirements

- [Docker Engine (i.e., Docker)](https://docs.docker.com/engine/)
- [Docker Model Runner](https://docs.docker.com/ai/model-runner/)
  + See requirements for Docker Model Runner [here](https://docs.docker.com/ai/model-runner/#requirements), which are dependent on your underlying OS outside of Docker
- VS Code

⚠️ NOTE: This approach is currently **not supported in GitHub Codespaces** because Codespaces machines lack the required Docker CLI plugins to run Docker Model Runner.

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
