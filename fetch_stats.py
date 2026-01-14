import requests
import json

# URL for the stats endpoint
# TODO: replace with your stats endpoint
url = "https://www.nytimes.com/svc/crosswords/v3/221431134/stats-and-streaks.json?date_start=1988-01-01&start_on_monday=true"

# headers to mimic a browser request   
headers = {
    "User-Agent": "Mozilla/5.0",
}

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

if __name__ == "__main__":
    fetch_stats()