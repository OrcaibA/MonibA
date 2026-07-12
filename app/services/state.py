import json
from pathlib import Path
from app.core.config import settings


STATE_FILE = Path(settings.STATE_FILE)

STATE_FILE.parent.mkdir(parents=True, exist_ok=True)

class StateManager:

    @staticmethod
    def load():
        if not STATE_FILE.exists():
            return {}

        try:
            with open(STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}

    @staticmethod
    def save(data):
        with open(STATE_FILE, "w") as f:
            json.dump(data, f, indent=4)