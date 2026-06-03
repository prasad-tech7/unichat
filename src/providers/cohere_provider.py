import cohere
from typing import List, Dict
from src.providers.base_provider import BaseProvider


class CohereProvider(BaseProvider):
    """Cohere LLM Provider — Free trial key available."""

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.name = "Cohere"
        self.model = "command-r-plus-08-2024"
        self.client = cohere.ClientV2(api_key=api_key)

    def chat(self, messages: List[Dict]) -> str:
        """Sends messages to Cohere and returns response."""
        try:
            formatted = self.format_messages(messages)
            response = self.client.chat(
                model=self.model,
                messages=formatted,
                max_tokens=1024,
                temperature=0.7
            )
            return response.message.content[0].text

        except Exception as e:
            error = str(e)
            if "rate_limit" in error.lower() or "429" in error:
                raise Exception("LIMIT_EXCEEDED: Cohere free limit reached.")
            raise Exception(f"Cohere error: {error}")

    def validate_key(self) -> bool:
        """Validates Cohere API key."""
        try:
            self.client.chat(
                model=self.model,
                messages=[{"role": "user", "content": "hi"}],
                max_tokens=5
            )
            return True
        except:
            return False