# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies needed for tree-sitter and other packages
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy the source code and metadata
COPY pyproject.toml README.md ./
COPY src/ /app/src/

# Install dependencies and the local package
RUN pip install --no-cache-dir . && pip install --no-cache-dir websockets

# Expose the port the app runs on
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV CARTOGRAPHY_DIR=/app/.cartography

# Run the application
CMD ["uvicorn", "src.ui.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
