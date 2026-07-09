import json
from pathlib import Path

STATE_FILE = Path("storage/state.json")


class StateManager:

    @staticmethod
    def load():
        if not STATE_FILE.exists():
            return {}

        try:
            with open(STATE_FILE, "r") as f:
                content = f.read().strip()

                if not content:
                    return {}

                return json.loads(content)

        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    @staticmethod
    def save(data):
        with open(STATE_FILE, "w") as f:
            json.dump(data, f, indent=4)