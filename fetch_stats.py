import requests
import json
import os

# URL for the stats endpoint
user_id = os.environ.get("NYT_USER_ID", "221431134")
url = f"https://www.nytimes.com/svc/crosswords/v3/{user_id}/stats-and-streaks.json?date_start=1988-01-01&start_on_monday=true"

# header with your cookies for authentication
headers = {
    "User-Agent": "Mozilla/5.0",
}

if "NYT_COOKIE" in os.environ:
    headers["Cookie"] = os.environ["NYT_COOKIE"]

def fetch_stats():
    # fetch stats from api
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        stats = response.json()
        #save to file
        with open("nyt_stats.json", "w") as f:
            json.dump(stats, f, indent=4)
        print("Stats fetched and saved successfully!")
    else:
        print(f"Failed to fetch stats. Status code: {response.status_code}")
        raise Exception("Failed to fetch stats")

if __name__ == "__main__":
    fetch_stats()