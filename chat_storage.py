
import json
from pathlib import Path
from datetime import datetime

# Location of chat history file
CHAT_FILE = Path(__file__).parent / "chat_history.json"


def load_all_chats():
    """Load all saved conversations."""

    if not CHAT_FILE.exists():
        return {}

    try:
        with open(CHAT_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


def save_chat(chat_id, title, messages):
    """Save or update a conversation."""

    chats = load_all_chats()

    chats[chat_id] = {
        "title": title,
        "messages": messages,
        "updated_at": datetime.now().isoformat()
    }

    with open(CHAT_FILE, "w", encoding="utf-8") as file:
        json.dump(chats, file, indent=4, ensure_ascii=False)


def load_chat(chat_id):
    """Load one conversation."""

    chats = load_all_chats()
    return chats.get(chat_id)


def delete_chat(chat_id):
    """Delete one conversation."""

    chats = load_all_chats()

    if chat_id in chats:
        del chats[chat_id]

        with open(CHAT_FILE, "w", encoding="utf-8") as file:
            json.dump(chats, file, indent=4, ensure_ascii=False)
