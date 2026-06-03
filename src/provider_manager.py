# src/provider_manager.py

from typing import Dict, Optional
from src.providers.groq_provider import GroqProvider
from src.providers.gemini_provider import GeminiProvider
from src.providers.mistral_provider import MistralProvider
from src.providers.cohere_provider import CohereProvider


# ✅ All supported providers
PROVIDERS = {
    "Groq (LLaMA)": {
        "class": GroqProvider,
        "icon": "⚡",
        "description": "Fast LLaMA model — best free option",
        "get_key_url": "https://console.groq.com"
    },
    "Google Gemini": {
        "class": GeminiProvider,
        "icon": "🌟",
        "description": "Google's Gemini Flash — multimodal",
        "get_key_url": "https://aistudio.google.com/apikey"
    },
    "Mistral": {
        "class": MistralProvider,
        "icon": "🌊",
        "description": "Mistral Small — efficient and fast",
        "get_key_url": "https://console.mistral.ai"
    },
    "Cohere": {
        "class": CohereProvider,
        "icon": "🤝",
        "description": "Command R Plus — great for long context",
        "get_key_url": "https://dashboard.cohere.com/api-keys"
    },

}


class ProviderManager:
    """
    Manages all AI providers.
    Handles provider switching with session preservation.
    """

    def __init__(self):
        self.active_provider = None
        self.active_provider_name = None
        self.initialized_providers: Dict = {}

    def initialize_provider(
        self,
        provider_name: str,
        api_key: str
    ) -> bool:
        """
        Initializes a provider with API key.

        Returns:
            bool: True if successful
        """
        try:
            provider_class = PROVIDERS[provider_name]["class"]
            provider = provider_class(api_key=api_key)
            self.initialized_providers[provider_name] = provider
            return True
        except Exception as e:
            print(f"❌ Failed to initialize {provider_name}: {e}")
            return False

    def switch_provider(self, provider_name: str) -> bool:
        """
        Switches active provider.

        Returns:
            bool: True if switch successful
        """
        if provider_name not in self.initialized_providers:
            return False

        self.active_provider = self.initialized_providers[provider_name]
        self.active_provider_name = provider_name
        return True

    def chat(self, messages: list) -> str:
        """
        Sends messages to active provider.

        Returns:
            str: Response from active provider
        """
        if not self.active_provider:
            raise Exception("No provider selected.")

        return self.active_provider.chat(messages)

    def get_provider_list(self) -> list:
        """Returns list of all available providers."""
        return list(PROVIDERS.keys())

    def get_initialized_providers(self) -> list:
        """Returns list of initialized providers."""
        return list(self.initialized_providers.keys())

    def is_ready(self) -> bool:
        """Returns True if active provider is set."""
        return self.active_provider is not None