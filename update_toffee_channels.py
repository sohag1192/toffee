import requests
import json

# Replace with actual Toffee API endpoint
TOFFEE_API_URL = "https://toffeelive.com/api/channel/list"

# Your cookie string
COOKIE = (
    "locale=en;device_id=4bf1bd3c1ae36e14d7252a42aabece69;"
    "device_refresh_token=...;"  # truncated for clarity
    "device_token=...;"
    "Edge-Cache-Cookie=..."
)

HEADERS = {
    "User-Agent": "okhttp/4.9.3",
    "Cookie": COOKIE
}

def fetch_channels():
    response = requests.get(TOFFEE_API_URL, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch channels: {response.status_code}")

def save_channels(data):
    with open("toffee_channels.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    try:
        channels = fetch_channels()
        save_channels(channels)
        print("✅ Channels updated successfully.")
    except Exception as e:
        print(f"❌ Error: {e}")