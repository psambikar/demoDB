import requests

url_json = "https://udemytrstorageaccgen2.blob.core.windows.net/uddataall/ActivityLog-01.json"

response = requests.get(url_json)

# Check response status
if response.status_code == 200:
    print("Response Content:", response.text)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
