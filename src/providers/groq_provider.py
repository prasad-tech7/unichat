# src/providers/groq_provider.py

from groq import Groq
from typing import List, Dict
from src.providers.base_provider import BaseProvider


class GroqProvider(BaseProvider):
    """Groq LLM Provider — Free tier available."""

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.name = "Groq"
        self.model = "llama-3.3-70b-versatile"
        self.client = Groq(api_key=api_key)

    def chat(self, messages: List[Dict]) -> str:
        """Sends messages to Groq and returns response."""
        try:
            formatted = self.format_messages(messages)
            response = self.client.chat.completions.create(
                model=self.model,
                messages=formatted,
                max_tokens=1024,
                temperature=0.7
            )
            return response.choices[0].message.content

        except Exception as e:
            error = str(e)
            if "rate_limit" in error.lower() or "429" in error:
                raise Exception("LIMIT_EXCEEDED: Groq free limit reached.")
            raise Exception(f"Groq error: {error}")

    def validate_key(self) -> bool:
        """Validates Groq API key."""
        try:
            self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": "hi"}],
                max_tokens=5
            )
            return True
        except:
            return False