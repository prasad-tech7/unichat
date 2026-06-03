# src/session_manager.py

from typing import List, Dict
from datetime import datetime


class SessionManager:
    """
    Manages chat history across provider switches.
    Core feature — preserves conversation context.
    """

    def __init__(self):
        self.messages: List[Dict] = []
        self.provider_switches: List[Dict] = []

    def add_user_message(self, content: str):
        """Adds user message to history."""
        self.messages.append({
            "role": "user",
            "content": content,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "provider": None
        })

    def add_assistant_message(self, content: str, provider_name: str):
        """Adds assistant message with provider info."""
        self.messages.append({
            "role": "assistant",
            "content": content,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "provider": provider_name
        })

    def record_switch(self, from_provider: str, to_provider: str):
        """Records provider switch for display."""
        self.provider_switches.append({
            "from": from_provider,
            "to": to_provider,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "message_index": len(self.messages)
        })

    def get_messages_for_api(self) -> List[Dict]:
        """
        Returns messages in API format.
        Only role and content — no metadata.
        """
        return [
            {
                "role": msg["role"],
                "content": msg["content"]
            }
            for msg in self.messages
        ]

    def get_display_messages(self) -> List[Dict]:
        """Returns messages with metadata for display."""
        return self.messages

    def clear(self):
        """Clears entire chat history."""
        self.messages = []
        self.provider_switches = []

    def is_empty(self) -> bool:
        return len(self.messages) == 0