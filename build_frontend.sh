#!/bin/bash

# Navigate to the frontend directory
cd frontend || { echo "Failed to navigate to frontend directory"; exit 1; }

# Build the Docker image with the tag 'frontend'
docker build -t frontend . || { echo "Docker build failed"; exit 1; }

# Navigate back to the previous directory
cd .. || { echo "Failed to navigate back to the parent directory"; exit 1; }

# Build the frontend service using Docker Compose
docker compose build frontend || { echo "Docker Compose build failed"; exit 1; }

echo "Frontend build process completed successfully"
``