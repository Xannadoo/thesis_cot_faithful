from ollama import chat
from .config import (OLLAMA_MODEL)


class LlamaChat:
    def __init__(self):
        self.model = OLLAMA_MODEL

    def get_response(self, messages):
        response = chat(model=self.model,
                    messages=messages)

        return response.message.content
