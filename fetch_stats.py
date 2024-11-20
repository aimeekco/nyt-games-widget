import requests
import json

# URL for the stats endpoint
url = "https://www.nytimes.com/svc/crosswords/v3/221431134/stats-and-streaks.json?date_start=1988-01-01&start_on_monday=true"

# Headers with your cookies for authentication
headers = {
    "User-Agent": "Mozilla/5.0",
    "Cookie": "nyt-a=Eu9gF_ec8lI6xbSqZwXPOa; nyt-gdpr=0; nyt-purr=cfshcfhssckfsdfhhgah2; purr-cache=<G_<C_<T0<Tp1_<Tp2_<Tp3_<Tp4_<Tp7_<a0_<K0<S0<r<ur; purr-pref-agent=<G_<C_<T0<Tp1_<Tp2_<Tp3_<Tp4_<Tp7_<a12; datadome=rgKIM4JwpJ4FevO_Iq4MretPVtOLNMSauvD2xIdonfDT0ZWNamZUG1q_GUWBwQ33NZGWYMZyDuAZmToFi_LVAt28TevNjPBA_vLQ85SN9LN3nMDCv_YbC0lAU6OSM_Qh;"  # Replace with your actual cookies
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