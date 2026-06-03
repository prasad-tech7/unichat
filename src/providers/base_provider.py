# src/providers/base_provider.py

from abc import ABC, abstractmethod
from typing import List, Dict


class BaseProvider(ABC):
    """
    Base class for all AI providers.
    Every provider must implement the chat method.
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.name = "Base"
        self.model = "base"

    @abstractmethod
    def chat(self, messages: List[Dict]) -> str:
        """
        Sends messages to provider and returns response.

        Args:
            messages: List of {"role": "user/assistant", "content": "..."}

        Returns:
            str: Provider response
        """
        pass

    @abstractmethod
    def validate_key(self) -> bool:
        """Validates if API key is working."""
        pass

    def format_messages(self, messages: List[Dict]) -> List[Dict]:
        """
        Formats messages to standard format.
        Each provider may override this if needed.
        """
        return [
            {
                "role": msg["role"],
                "content": msg["content"]
            }
            for msg in messages
        ]