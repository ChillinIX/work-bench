import pandas as pd

api_key='4eced22c-924d-4aa3-8a36-d4205ec34cfe'
account_id= 44067861
dotaData = pd.read_html('https://api.opendota.com/api/players/44067861/wl/api_key=',api_key)

print(dotaData)