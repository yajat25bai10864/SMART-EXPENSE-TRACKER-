import json
import os

# Absolute path to the data file — works regardless of where Python is launched from.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root
FILE = os.path.join(BASE_DIR, "data", "expense.json")


def load_data() -> list:
    """Load expenses from disk. Returns an empty list if the file doesn't exist or is corrupt."""
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Warning: Could not read expense data — starting fresh. Error: {e}")
        return []


def save_data(data: list) -> None:
    """Persist the expense list to disk as formatted JSON."""
    os.makedirs(os.path.dirname(FILE), exist_ok=True)
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)