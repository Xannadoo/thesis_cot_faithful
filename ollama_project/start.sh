#!/bin/bash
set -e

# Set custom directory for storing models
export OLLAMA_MODELS="/models"

mkdir -p /models
chmod 777 /models

mkdir -p /outputs
chmod 777 /outputs

# Start Ollama in the background
OLLAMA_CONTEXT_LENGTH=8192 ollama serve &
echo "Starting Ollama server..."
sleep 5  # wait for the server to be ready

# Check if the model already exists
if ! ollama list | grep -q "deepseek-r1:8b"; then
    echo "Model 'deepseek-r1:8b' not found. Pulling..."
    ollama pull deepseek-r1:8b
    ollama list
    echo "Listing /models directory:"
    ls -l /models
else
    echo "Model 'deepseek-r1:8b' already available."
fi

# Run your app
echo "Starting chat..."
python3 -m src.main
