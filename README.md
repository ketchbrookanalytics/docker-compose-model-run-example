# Docker Compose with Docker Model Runner

Template repository for projects containing a service (web app, API, etc.) and a local LLM (via Docker Model Runner) via Docker Compose.

The official documentation on using Docker Model Runner with Docker Compose can be found here: <https://docs.docker.com/ai/compose/models-and-compose/>.

## Motivation

We found ourselves constantly following the same pattern of creating a Docker Compose environment with two services:

1. A web application
1. An API for hosting an open-weights LLM using [ollama](https://github.com/ollama/ollama).

When [Docker Model Runner](https://docs.docker.com/ai/model-runner/) was released, it appeared that we may be able to greatly simplify the effort required to stand up the second service. This approach has significantly reduced the configuration required to utilize an open-weights LLM with another Docker container service.

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

> ⚠️ NOTE: This approach is currently **not supported in GitHub Codespaces** because Codespaces machines lack the required Docker CLI plugins to run Docker Model Runner.

## Quick Start 🏃‍➡️

1. **Open in Dev Container**
   - Open the project in VS Code
   - Click "Reopen in Container" when prompted
   - Or use Command Palette: "Dev Containers: Reopen in Container"

1. **Run the Gradio app**
   ```bash
   uv run app.py
   ```
   The app will be available at <http://localhost:8000>

## Using a Different LLM

You can configure the Docker Model Runner LLM you want to use in the `models` section of [compose.yml](compose.yml#L32-L36).

## Adapting for Your Project

This project leverages [uv](https://docs.astral.sh/uv/) for Python dependency management. As you change/replace [app.py](app.py) to adapt this repository for your own needs, you'll want to use the following `uv` terminal commands to manage your dependencies:

- `uv add <package>` to install a new Python package in the virtual environment
- `uv remove <package>` to remove an installed Python package from the virtual environment
- `uv sync` to sync the environment with the lock file(s)

### Initializing `uv` from Scratch

If you want to initialize `uv` from scratch, perform the following steps:

- Comment out the [`postCreateCommand` in devcontainer.json](.devcontainer/devcontainer.json#L13) that runs `uv sync`
- (Optional) Change the version of Python you want to use in the [Dockerfile](Dockerfile#L2) and [.python-version](.python-version) file
- Delete the [pyproject.toml](pyproject.toml) and [uv.lock](uv.lock) files
- Via the VSCode Command Palette, select `Dev Containers: Rebuild and Reopen in Container` to apply your changes to the Dev Container environment
- Once the Dev Container has been successfully reopened, run `uv init` from a terminal.

## Deployment 🚀

When deploying your services to a production environment (i.e., no longer utilizing the Dev Container), you'll want to add a line to the [Dockerfile](Dockerfile) that installs the Python package dependencies from the lock file like so:

```docker
RUN uv sync
```

Lastly, see the [Development Dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/#development-dependencies) section of the `uv` project documentation for information on managing Python package dependencies that are only used for development purposes (and aren't required for production).