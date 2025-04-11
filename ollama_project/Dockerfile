FROM ollama/ollama:latest

WORKDIR /ollama_project

# Copy your Python application files
COPY . /ollama_project

RUN chmod +x /ollama_project/start.sh

# Install Python and dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip install .

# Expose the Ollama API port
EXPOSE 11434

ENTRYPOINT []

CMD ["/ollama_project/start.sh"]