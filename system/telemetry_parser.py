import subprocess
import random
import re
import os
import json
import time
import hashlib

AGY_BIN = "/data/data/com/termux/files/home/workspace/matrix_ce/MATRIX_GEN8_HOME-1.2.0-alpha/H2OIDE/agy"
CACHE_FILE = os.environ.get("TELEMETRY_CACHE_FILE", os.path.expanduser("~/.matrix_ide/cache/telemetry_cache.json"))
CACHE_TTL = int(os.environ.get("TELEMETRY_CACHE_TTL", "30"))  # seconds

class TelemetryParser:
    def __init__(self):
        print("📊 [TELEMETRY PARSER] Listening to Windows CE Memory & Scheduler Logs...")
        self.hex_pattern = re.compile(r'([0-9a-fA-F]{2}\s){7}[0-9a-fA-F]{2}')

    def generate_mock_telemetry(self):
        addr = hex(random.randint(0x10000, 0xFFFFF))
        dump = " ".join([hex(random.randint(0, 255))[2:].zfill(2) for _ in range(8)])
        return f"Thread 4 Exception. EIP: {addr}. Stack Dump: {dump}"

    def _cache_get(self, key):
        try:
            if os.path.exists(CACHE_FILE):
                with open(CACHE_FILE, 'r') as f:
                    cache = json.load(f)
                entry = cache.get(key)
                if entry:
                    if time.time() - entry.get("ts", 0) < CACHE_TTL:
                        return entry.get("result")
                    else:
                        del cache[key]
                        with open(CACHE_FILE, 'w') as f:
                            json.dump(cache, f)
        except Exception:
            pass
        return None

    def _cache_put(self, key, result):
        try:
            os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
            cache = {}
            if os.path.exists(CACHE_FILE):
                with open(CACHE_FILE, 'r') as f:
                    cache = json.load(f)
            cache[key] = {"ts": time.time(), "result": result}
            with open(CACHE_FILE, 'w') as f:
                json.dump(cache, f)
        except Exception:
            pass

    def analyze_telemetry(self):
        raw_log = self.generate_mock_telemetry()
        cache_key = hashlib.md5(raw_log.encode()).hexdigest()
        cached = self._cache_get(cache_key)
        if cached is not None:
            print(f"📥 Cached TE Telemetry (TTL={CACHE_TTL}s): {raw_log}")
            print(f"🧠 [DANUBE ANALYSIS]: {cached}")
            return cached

        if not self.hex_pattern.search(raw_log):
            print("⚠️ [TELEMETRY PARSER] Invalid hex dump format detected. Skipping analysis.")
            return

        print(f"📥 Raw CE Telemetry: {raw_log}")
        prompt = f"Analyze this Windows CE telemetry log and explain what the hex dump implies about the crash. Keep it under 2 sentences. Log: {raw_log}"
        result = subprocess.run([AGY_BIN, "-p", prompt], capture_output=True, text=True)

        analysis = result.stdout.strip()
        print(f"🧠 [DANUBE ANALYSIS]: {analysis}")
        self._cache_put(cache_key, analysis)
        return analysis

if __name__ == "__main__":
    parser = TelemetryParser()
    parser.analyze_telemetry()
