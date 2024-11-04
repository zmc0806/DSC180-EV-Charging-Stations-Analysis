## `src/data_processor.py`
import json
import pandas as pd
import os

def process_ev_data(json_path='data/alt_fuel_stations.json', output_csv='data/alt_fuel_stations.csv'):
    if not os.path.exists(json_path):
        print(f"File not found: {json_path}")
        return
    
    with open(json_path) as f:
        data = json.load(f)
    
    df = pd.json_normalize(data['fuel_stations'])
    df.to_csv(output_csv, index=False)
    print("Data processed and saved to alt_fuel_stations.csv")

def filter_sdge_zip_codes(csv_path='data/alt_fuel_stations.csv', zip_codes_path='data/SDGE_Service_Territory_Zip_Code_List.xlsx', output_csv='data/filtered_alt_fuel_stations.csv'):
    if not os.path.exists(csv_path) or not os.path.exists(zip_codes_path):
        print(f"File not found: {csv_path} or {zip_codes_path}")
        return
    
    df = pd.read_csv(csv_path)
    zip_codes_df = pd.read_excel(zip_codes_path)
    zip_codes = zip_codes_df['ZIP_CODE'].astype(str).tolist()
    
    filtered_df = df[df['zip'].isin(zip_codes)]
    filtered_df.to_csv(output_csv, index=False)
    print("Filtered data saved to filtered_alt_fuel_stations.csv")