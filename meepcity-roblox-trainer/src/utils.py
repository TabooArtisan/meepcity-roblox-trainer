"""Utility functions for MeepCity trainer."""

import json
import os
from datetime import datetime


def save_profile(data: dict, filepath: str = "profile.json") -> bool:
    """Save player profile to JSON file."""
    try:
        data["last_saved"] = datetime.now().isoformat()
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving profile: {e}")
        return False


def load_profile(filepath: str = "profile.json") -> dict:
    """Load player profile from JSON file."""
    if not os.path.exists(filepath):
        return {"username": "default", "coins": 0, "xp": 0}
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading profile: {e}")
        return {}


def format_time(seconds: int) -> str:
    """Format seconds into HH:MM:SS."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"