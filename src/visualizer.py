## `src/visualizer.py`
import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_stations_per_year(csv_path='data/alt_fuel_stations.csv'):
    if not os.path.exists(csv_path):
        print(f"File not found: {csv_path}")
        return
    
    df = pd.read_csv(csv_path)
    df['Open Date'] = pd.to_datetime(df['Open Date'], errors='coerce')
    df['Open Year'] = df['Open Date'].dt.year

    stations_per_year = df.groupby('Open Year').size().reset_index(name='Number of Stations Opened')
    
    plt.figure(figsize=(10, 6))
    plt.plot(stations_per_year['Open Year'], stations_per_year['Number of Stations Opened'], marker='o')
    plt.title('Number of Charging Stations Opened Each Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Stations Opened')
    plt.grid(True)
    plt.show()