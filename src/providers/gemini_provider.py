# src/providers/gemini_provider.py

# src/providers/gemini_provider.py

from google import genai
from google.genai import types
from typing import List, Dict
from src.providers.base_provider import BaseProvider


class GeminiProvider(BaseProvider):
    """Google Gemini Provider — Free tier available."""

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.name = "Gemini"
        self.model = "gemini-2.5-flash"  # ✅ better free limits
        self.client = genai.Client(api_key=api_key)

    def chat(self, messages: List[Dict]) -> str:
        """Sends messages to Gemini and returns response."""
        try:
            # ✅ Build contents list
            contents = []
            for msg in messages:
                contents.append(
                    types.Content(
                        role="user" if msg["role"] == "user" else "model",
                        parts=[types.Part(text=msg["content"])]
                    )
                )

            response = self.client.models.generate_content(
                model=self.model,
                contents=contents
            )
            return response.text

        except Exception as e:
            error = str(e)
            if "quota" in error.lower() or "429" in error or "RESOURCE_EXHAUSTED" in error:
                raise Exception("LIMIT_EXCEEDED: Gemini free limit reached.")
            raise Exception(f"Gemini error: {error}")

    def validate_key(self) -> bool:
        """Validates Gemini API key."""
        try:
            self.client.models.generate_content(
                model=self.model,
                contents="hi"
            )
            return True
        except:
            return False