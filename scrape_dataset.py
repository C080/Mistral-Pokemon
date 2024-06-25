import requests
import time
import json
from pathlib import Path

def get_all_gen5_random_battle_replays():
    base_url = "https://replay.pokemonshowdown.com/search.json"
    params = {"format": "gen5randombattle"}
    existing_ids = set()
    total_replays = 0

    # Load existing replay IDs if any
    replay_file = Path("gen5_random_battle_replays.jsonl")
    if replay_file.exists():
        with open(replay_file, "r") as f:
            for line in f:
                replay = json.loads(line)
                existing_ids.add(replay["id"])
                total_replays += 1
            if total_replays > 0:
                params["before"] = json.loads(line)["uploadtime"]

    with open(replay_file, "a") as f:
        while True:
            response = requests.get(base_url, params=params)
            data = response.json()

            # Add only new replays
            new_replays = [replay for replay in data if replay["id"] not in existing_ids]
            for replay in new_replays:
                json.dump(replay, f)
                f.write("\n")
                existing_ids.add(replay["id"])
                total_replays += 1

            print(f"Fetched {len(new_replays)} new Gen 5 Random Battle replays. Total: {total_replays}")

            # Check if there are more pages
            if len(data) <= 50:
                break

            # Update the 'before' parameter for the next request
            params["before"] = data[-1]["uploadtime"]

            # Add a small delay to avoid overwhelming the server
            time.sleep(1)

    return total_replays

# Usage
total_gen5_random_battle_replays = get_all_gen5_random_battle_replays()
print(f"Total unique Gen 5 Random Battle replays found: {total_gen5_random_battle_replays}")
