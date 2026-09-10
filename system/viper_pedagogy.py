import os
import re
import sqlite3
from collections import Counter, defaultdict

def process_viper_notes(notes_dir):
    all_lines = []

    # 1. Read physical markdown files
    if os.path.exists(notes_dir):
        for file in os.listdir(notes_dir):
            if file.endswith('.md'):
                try:
                    with open(os.path.join(notes_dir, file), 'r', errors='ignore') as f:
                        content = f.read()
                        segments = [seg.strip() for seg in content.split('\n') if seg.strip()]
                        all_lines.extend(segments)
                except Exception:
                    continue

    # 2. Read from Cognitive Harvest DB (The 'retrace steps' data)
    db_path = "/data/data/com.termux/files/home/openrouter_manager/pedagogy_cognitive.db"
    if os.path.exists(db_path):
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("SELECT content_blob FROM local_training_data")
            for row in c.fetchall():
                content = row[0]
                # Split large blobs into logical sections (e.g. paragraphs or code blocks)
                segments = [seg.strip() for seg in content.split('\n\n') if seg.strip()]
                all_lines.extend(segments)
            conn.close()
        except Exception:
            pass

    # 3. Read from Knowledge Hub (Clippy's brain)
    hub_db = os.path.expanduser("~/.matrix_ide/database/knowledge_hub.db")
    if os.path.exists(hub_db):
        try:
            conn = sqlite3.connect(hub_db)
            c = conn.cursor()
            c.execute("SELECT content FROM knowledge")
            for row in c.fetchall():
                all_lines.append(row[0].strip())
            conn.close()
        except Exception:
            pass

    # Count frequencies for tabbing
    segment_counts = Counter(all_lines)

    frequent_tabs = defaultdict(list)
    numbered_groups = []
    unique_general = []

    seen = set()

    for seg in all_lines:
        if seg in seen:
            continue
        seen.add(seg)

        count = segment_counts[seg]

        # TABBING: If segment appears > 3 times, isolate it
        if count > 3:
            # Clean up the name for a tab
            clean_name = re.sub(r'[^a-zA-Z0-9 ]', '', seg[:20]).strip()
            tab_name = f"Common: {clean_name}..."
            frequent_tabs[tab_name].append(seg)
            continue

        # NUMBER GROUPING: 1. 2. 3.
        if re.match(r'^\d+[\.\-\)]?\s', seg):
            numbered_groups.append(seg)
            continue

        # GENERAL (The main body)
        unique_general.append(seg)

    # Sort numbered groups
    def extract_num(s):
        match = re.search(r'^(\d+)', s)
        return int(match.group(1)) if match else 0
    numbered_groups.sort(key=extract_num)

    # Genetic Darwin Advance: If we have a massive amount of notes, prioritize most recent
    return {
        "frequent_tabs": dict(frequent_tabs),
        "numbered_groups": numbered_groups,
        "general": unique_general,
        "total_harvested_count": len(all_lines)
    }
