import requests
import json

# URL of the API endpoint
url = "http://api.open-notify.org/iss-now.json"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    
    data = response.json()
    # Print the JSON response
    print("JSON response:", data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
