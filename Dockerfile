# Use Python slim image as base
FROM python:3.12-slim

# Update system dependencies
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy the project files
COPY . /app
WORKDIR /app

# Configure uv to create venv in project directory
ENV UV_PROJECT_ENVIRONMENT=/app/.venv

# Activate the virtual environment by default
ENV PATH="/app/.venv/bin:$PATH"