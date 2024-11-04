## `run.py`
import sys
from src.data_fetcher import fetch_ev_data
from src.data_processor import process_ev_data, filter_sdge_zip_codes
from src.visualizer import plot_stations_per_year
from src.geospatial_analysis import generate_ev_map, calculate_route

def main(targets):
    if 'data' in targets:
        fetch_ev_data()
    if 'filter' in targets:
        process_ev_data()
        filter_sdge_zip_codes()
    if 'visualize' in targets:
        plot_stations_per_year()
    if 'geospatial' in targets:
        generate_ev_map()
    if 'route' in targets:
        sdge_location = (32.82434409454857, -117.1429236351)  # Example coordinates
        ev_charger_location = (32.831882293954735, -117.15902477363302)  # Example coordinates
        calculate_route(sdge_location, ev_charger_location)

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)
