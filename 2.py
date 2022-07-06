import requests
import json

url = "https://api.opendota.com/api/data/parquet"

match_response = requests.get(url)

# request code
print(match_response.status_code)

match_data = match_response.json()

print(type(match_data))
print(len(match_data))
print(list(match_data.keys))