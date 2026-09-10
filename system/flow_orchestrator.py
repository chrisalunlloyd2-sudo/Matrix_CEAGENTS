import json
import sqlite3
import requests
import os
import PocketMatrix.system.viper_pedagogy as viper
from PocketMatrix.system.knowledge_hub import search_knowledge_bm25

TODO_DB = os.path.expanduser("~/.matrix_ide/database/todo.db")
NOTES_DIR = os.path.expanduser("~/VIPER_SCRIPT_LIBRARY/notes_ce")

def get_system_flow():
    # 1. Get active tasks
    conn = sqlite3.connect(TODO_DB)
    c = conn.cursor()
    try:
        c.execute("SELECT task FROM tasks WHERE status = 'pending'")
        tasks = [row[0] for row in c.fetchall()]
    except Exception:
        tasks = []
    conn.close()

    # 2. Get Viper Pedagogy State
    try:
        notes_state = viper.process_viper_notes(NOTES_DIR)
        numbered = notes_state.get('numbered_groups', [])
        frequent = list(notes_state.get('frequent_tabs', {}).keys())
    except Exception:
        numbered = []
        frequent = []

    # 3. Construct the prompt for the local AI
    state_summary = f"Active Tasks: {tasks[:3]}. Core Principles: {numbered[:3]}. Key Concepts: {frequent[:3]}."
    prompt = f"You are the Matrix Flow Orchestrator. Analyze this system state: '{state_summary}'. What is the optimal logical flow and next immediate steps for the developer? Be analytical and precise."

    try:
        response = requests.post("http://127.0.0.1:8080/completion", json={
            "prompt": prompt,
            "n_predict": 200,
            "temperature": 0.7,
            "repeat_penalty": 1.2,
            "top_k": 40,
            "top_p": 0.95
        }, timeout=45)

        if response.status_code == 200:
            flow_plan = response.json().get('content', '').strip()
            return flow_plan if flow_plan else "No flow generated."
    except Exception as e:
        return f"Orchestrator LLM failure: {e}"

if __name__ == '__main__':
    print(get_system_flow())