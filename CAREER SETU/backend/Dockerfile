# Backend Dockerfile - Production Ready
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better Docker layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download spacy language model
RUN python -m spacy download en_core_web_sm

# Copy the entire backend source into /app
# This gives us: /app/app/, /app/ml_models/, /app/models/
COPY . .

# Set PYTHONPATH so that 'app' and 'ml_models' are importable as top-level packages
ENV PYTHONPATH=/app

# Expose the port (Render overrides this via PORT env var)
EXPOSE 8000

# Use shell form so $PORT env var is expanded at container runtime
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 1
