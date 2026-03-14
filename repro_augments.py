
import sys
import logging
sys.stdout.reconfigure(encoding='utf-8')

# Mock logging
logging.basicConfig(level=logging.INFO)

from apexlol_data import load_cache, extract_top_synergies, resolve_champion_id
from config import APEXLOL_CACHE_DIR

print(f"Loading cache from: {APEXLOL_CACHE_DIR}")
load_cache(APEXLOL_CACHE_DIR)

champs_to_test = ["金克丝", "Jinx", "小法", "亚索", "薇恩"]
for name in champs_to_test:
    print(f"\n--- Testing: {name} ---")
    cid = resolve_champion_id(name)
    print(f"Resolved ID: {cid}")
    augments = extract_top_synergies(name)
    if augments:
        print(f"Augments Found (len={len(augments)}):")
        print(augments[:200] + "...")
    else:
        print("❌ NO AUGMENTS FOUND!")
