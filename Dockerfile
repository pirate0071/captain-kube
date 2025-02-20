# Use an official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy project files to container
COPY . .

# Install system dependencies
RUN apt update && apt install -y binutils curl && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install pytest explicitly
RUN pip install --upgrade pytest

ENV PYTHONPATH=/app

# Ensure Python and pytest are correctly set up
RUN ln -sf $(which python3) /usr/local/bin/python
