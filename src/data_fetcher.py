## `src/data_fetcher.py`
import requests
import json
import os

def fetch_ev_data(config_path='config/api_config.json'):
    with open(config_path) as f:
        config = json.load(f)
    
    url = f"{config['base_url']}?api_key={config['api_key']}&fuel_type={config['fuel_type']}&state={config['state']}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open('data/alt_fuel_stations.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Data fetched and saved to alt_fuel_stations.json")
    else:
        print(f"Failed to fetch data: {response.status_code}, {response.text}")



