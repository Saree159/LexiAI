import json
import os

DEFAULT_SETTINGS = {
    "model_name": "llama3",
    "chunk_size": 300,
    "llm_source": "ollama",
    "dark_mode": True
}

def load_settings(path="settings.json"):
    if not os.path.exists(path):
        save_settings(DEFAULT_SETTINGS, path)
        return DEFAULT_SETTINGS

    with open(path, "r", encoding="utf-8") as f:
        settings = json.load(f)

    # Ensure all default keys exist
    for key, value in DEFAULT_SETTINGS.items():
        settings.setdefault(key, value)

    return settings

def save_settings(settings, path="settings.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)
