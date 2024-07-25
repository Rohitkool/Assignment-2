import json

# JSON data copied from the provided URL
json_data = '''
{
    "date": "2024-07-26",
    "explanation": "This image of the day shows a stunning view of the Milky Way galaxy, captured by the Hubble Space Telescope.",
    "hdurl": "https://apod.nasa.gov/apod/image/2407/milkyway_hst.jpg",
    "media_type": "image",
    "service_version": "v1",
    "title": "The Milky Way Overhead",
    "url": "https://apod.nasa.gov/apod/image/2407/milkyway_hst.jpg"
}
'''


data = json.loads(json_data)

# Print the values associated with the keys "explanation" and "title"
print("Explanation:", data.get("explanation"))
print("Title:", data.get("title"))
