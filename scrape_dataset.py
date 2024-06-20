import os
import requests
import json

# URL to fetch the JSON data from
url = "https://replay.pokemonshowdown.com/search.json?format=gen7randombattle"

# Create the "replays" folder if it doesn't exist
if not os.path.exists("replays"):
    os.makedirs("replays")

try:
    # Make a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Get the JSON data from the response
        data = response.json()
        
        # Iterate over each item in the data
        for item in data:
            # Extract the "id" field from the item
            replay_id = item.get("id")
            
            if replay_id:
                # Construct the URL for the replay log
                replay_url = f"https://replay.pokemonshowdown.com/{replay_id}.log"
                
                try:
                    # Make a GET request to the replay URL
                    replay_response = requests.get(replay_url)
                    
                    # Check if the replay request was successful
                    if replay_response.status_code == 200:
                        # Save the replay content as a file in the "replays" folder
                        file_path = os.path.join("replays", f"{replay_id}.log")
                        with open(file_path, "w", encoding="utf-8") as file:
                            file.write(replay_response.text)
                        
                        print(f"Replay saved: {file_path}")
                    else:
                        print(f"Failed to retrieve replay: {replay_id}. Status code: {replay_response.status_code}")
                
                except requests.exceptions.RequestException as e:
                    print(f"An error occurred while retrieving replay: {replay_id}. Error: {e}")
            
            else:
                print(f"ID not found for item: {item}")
        
    else:
        print("Failed to retrieve data. Status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
