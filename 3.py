import requests
import json
import os
import pandas as pd
import datetime
Dota2 = ''

parquet_data_exists = False
ls_parquet = ""
if any(["heroes" in item for item in ls_parquet]):
    parquet_data_exists = True
    for idx, file in enumerate(ls_parquet):
        if "heroes" in file:
            pq_fname = file

if not(parquet_data_exists):

    print("Pulling from OpenDOTA.")

    resp = requests.get("https://api.opendota.com/api/heroes")

    if not(resp.status_code == 200):
        print("The request failed. There may be an outage.")

    heroes_json = resp.json()

    Dota2.Heroes.json = heroes_json
    Dota2.Heroes.dataframe = pd.DataFrame(heroes_json)
    Dota2.Heroes.table = pd.to_table(Dota2.Heroes.dataframe)\
        .update_view(["Roles = (java.lang.String[])jpy.array(`java.lang.String`, roles)", \
            "Name = (java.lang.String)name", "LocalizedName = (java.lang.String)localized_name", \
            "Attribute = (java.lang.String)primary_attr", "AttackType = (java.lang.String)attack_type", \
            "Legs = (int)legs"])\
        .drop_columns(["name", "localized_name", "primary_attr", "attack_type", "roles", "legs"])

    todays_date = datetime.datetime.now().strftime("%Y-%m-%d")
    fname = f"/data/parquet/heroes_{todays_date}.parquet"
    dhpq.write(Dota2.Heroes.table, fname, compression_codec_name="GZIP")

else:

    fname_write_date = pq_fname.split("_")[1].split(".")[0]
    print(f"Found local hero data. It was written on {fname_write_date}.")

    Dota2.Heroes.table = pd.read(f"/data/parquet/{pq_fname}")
    Dota2.Heroes.dataframe = pd.to_pandas(Dota2.Heroes.table)
    Dota2.Heroes.dataframe["Roles"] = Dota2.Heroes.dataframe["Roles"].apply(lambda item: list(item))
    Dota2.Heroes.json = Dota2.Heroes.dataframe.to_dict("records")