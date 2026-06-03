# src/providers/mistral_provider.py

from mistralai.client import Mistral as MistralClient
from typing import List, Dict
from src.providers.base_provider import BaseProvider


class MistralProvider(BaseProvider):
    """Mistral AI Provider — Free tier available."""

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.name = "Mistral"
        self.model = "mistral-small-latest"
        self.client = MistralClient(api_key=api_key)

    def chat(self, messages: List[Dict]) -> str:
        """Sends messages to Mistral and returns response."""
        try:
            formatted = self.format_messages(messages)

            response = self.client.chat.complete(
                model=self.model,
                messages=formatted,
                max_tokens=1024,
                temperature=0.7
            )
            return response.choices[0].message.content

        except Exception as e:
            error = str(e)
            if "rate_limit" in error.lower() or "429" in error:
                raise Exception("LIMIT_EXCEEDED: Mistral free limit reached.")
            raise Exception(f"Mistral error: {error}")

    def validate_key(self) -> bool:
        """Validates Mistral API key."""
        try:
            self.client.chat.complete(
                model=self.model,
                messages=[{"role": "user", "content": "hi"}],
                max_tokens=5
            )
            return True
        except:
            return False