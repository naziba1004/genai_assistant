# ==============================================================================
# 1. Base Image Setup
# ==============================================================================
FROM python:3.11-slim AS base

# Prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Poetry Configuration Environments
ENV POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

# Add Poetry to the system PATH so it can be called directly
ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app

# ==============================================================================
# 2. Install System Dependencies & Poetry
# ==============================================================================
# Install curl to download Poetry, and build-essential if any packages need compiling
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Download and install Poetry using the official installer script
RUN curl -sSL https://install.python-poetry.org | python3 -

# ==============================================================================
# 3. Dependency Installation
# ==============================================================================
# Copy only dependency files first to leverage Docker's build caching
COPY poetry.lock pyproject.toml ./

# Install project dependencies globally in the container (skips development packages)
RUN poetry install --no-root --only main

# ==============================================================================
# 4. Application Deployment
# ==============================================================================
# Copy the rest of your Flask application code
COPY . .

# Expose the Flask port
EXPOSE 5000

# Sets the working directory
WORKDIR genai_assistant

# ==============================================================================
# 5. Runtime Execution
# ==============================================================================
# Run the application directly using the Python interpreter
CMD ["python", "app.py"]