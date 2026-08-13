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

if "NYT_COOKIE" in os.environ and os.environ["NYT_COOKIE"].strip():
    cookie_val = os.environ["NYT_COOKIE"].strip()
    if not cookie_val.startswith("NYT-S="):
        cookie_val = f"NYT-S={cookie_val}"
    headers["Cookie"] = cookie_val

def fetch_stats():
    if "NYT_COOKIE" not in os.environ:
        print("Warning: NYT_COOKIE environment variable is not set. Authenticated requests may fail.")

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
        if response.status_code in (401, 403, 404):
            print("Authentication failed. Please verify NYT_COOKIE and NYT_USER_ID secrets in repository settings.")
        raise Exception(f"Failed to fetch stats: HTTP {response.status_code}")

if __name__ == "__main__":
    fetch_stats()