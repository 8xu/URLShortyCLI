import requests

UserURL = input("Enter URL: ")
BASE = "https://url.cyclic.app"
URL = f"{BASE}/shorten"

raw_data = {
    "url": UserURL
}
response = requests.post(URL, data=raw_data)

if response.status_code == 201:
    shortUrl = f"{BASE}/{response.json()['shortUrl']}"
    print(f"Shortened URL: {shortUrl}")
else:
    print(f"We got an error: {response.status_code}.")