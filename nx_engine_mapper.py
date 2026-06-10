import json
import sqlite3
import os
import requests
from datetime import datetime

/**
 * KAI 9000: NXEngine Mind Palace Mapper
 * Links the 2D visual world to the Matrix CE Brain Database.
 */

DB_PATH = os.path.expanduser("~/.matrix_ide/database/knowledge_hub.db")
SERVER_URL = "http://127.0.0.1:8081/api/knowledge/search"

def map_room_to_context(room_id):
    """
    Triggered by NXEngine when entering a room.
    Fetches room-specific knowledge from the project DB.
    """
    print(f"[*] NXEngine: Entered Room {room_id}")
    
    # Query logic based on room ID
    query = f"project overview room {room_id}"
    
    try:
        response = requests.post(SERVER_URL, json={"query": query})
        if response.status_code == 200:
            data = response.json()
            # Return top match as an interactive text asset
            return data.get('results', ["Knowledge gap detected in this sector."])[0]
    except Exception as e:
        return f"Database Link Severed: {e}"

def update_game_state(state_json):
    """
    Saves visual memory coordinates back to the brain.
    """
    state = json.loads(state_json)
    # logic to store X,Y coords as visual anchors in SQLite
    pass

if __name__ == "__main__":
    # Test mapping
    print(f"Room context: {map_room_to_context('Laboratory')}")
