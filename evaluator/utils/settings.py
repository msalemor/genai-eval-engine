import os
from dotenv import load_dotenv

global _settings_instance
_settings_instance = None


def get_settings():
    global _settings_instance
    if not _settings_instance:
        _settings_instance = Settings()
    return _settings_instance


class Settings:
    def __init__(self):
        load_dotenv()
        self._endpoint = os.getenv("ENDPOINT")
        self._api_key = os.getenv("API_KEY")
        self._version = os.getenv("VERSION")
        if not self._endpoint or not self._api_key or not self._version:
            raise ValueError(
                "OpenAI API credentials not found in environment variables.")

    @property
    def endpoint(self):
        return self._endpoint

    @property
    def api_key(self):
        return self._api_key

    @property
    def version(self):
        return self._version
