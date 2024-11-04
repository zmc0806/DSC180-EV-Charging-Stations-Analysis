## README.md

# EV Charging Stations Project

This project analyzes EV charging station data in California, focusing on the SDG&E service area. It uses data from the NREL API to understand the distribution of charging stations over time and perform geospatial analyses.

## Project Structure

The project is organized into the following directories and files:

- `config/`
  - `api_config.json`: Configuration file for storing API key and other parameters.
- `data/`: Directory for storing fetched, processed, and filtered data files.
- `src/`: Directory containing the main Python scripts for different components of the project.
  - `data_fetcher.py`: Script to fetch EV charging station data from the NREL API.
  - `data_processor.py`: Script to process and filter the data.
  - `visualizer.py`: Script for visualizing the data.
  - `geospatial_analysis.py`: Script for geospatial analysis, including mapping and route calculation.
- `run.py`: Main build script for running different parts of the project.

## Installation

To run this project, you will need Python 3 installed along with the required dependencies.

1. Clone the repository:
   ```
   git clone <repository_url>
   cd EV_Stations_Project
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies using the requirements file:
   ```
   pip install -r requirements.txt
   ```

## Configuration

The project uses a configuration file located at `config/api_config.json` to store API parameters:
```json
{
  "api_key": "YOUR_API_KEY_HERE",
  "base_url": "https://developer.nrel.gov/api/alt-fuel-stations/v1.json",
  "fuel_type": "ELEC",
  "state": "CA"
}
```
Replace `YOUR_API_KEY_HERE` with your actual NREL API key.

## Running the Project

The project can be run by using the `run.py` script with different targets to execute parts of the project. The available targets are:

- **data**: Fetches data from the API.
- **filter**: Processes and filters the raw data.
- **visualize**: Generates visualizations.
- **geospatial**: Performs geospatial analyses (including map creation).
- **route**: Calculates a route between specified locations using OSMnx.

### Example Commands

To fetch data and generate visualizations, you can run:
```sh
python run.py data visualize
```

To fetch data, filter it, and perform geospatial analyses:
```sh
python run.py data filter geospatial
```

To calculate a route from SDG&E to a selected EV charger:
```sh
python run.py route
```

## Data Fetching

The data fetching process uses the NREL API to obtain information about electric vehicle charging stations. The script `data_fetcher.py` reads parameters from `config/api_config.json` and saves the fetched data as a JSON file in the `data/` directory.

## Data Processing

The `data_processor.py` script is used to process the JSON data into a CSV file. It also has functionality to filter the data based on SDG&E service territory zip codes. The filtered data is saved as `filtered_alt_fuel_stations.csv`.

## Visualization

The visualization script, `visualizer.py`, generates time-series plots for the number of charging stations opened each year. It uses `matplotlib` to create the visualizations.

## Geospatial Analysis

The `geospatial_analysis.py` script includes:

- **Mapping**: Uses `folium` and `geopandas` to create an interactive map showing the locations of EV charging stations.
- **Route Calculation**: Uses `osmnx` and `networkx` to calculate the driving distance between SDG&E and selected EV chargers.

### Geospatial Map
The map of EV charging stations is saved as `data/all_ev_stations_map.html` and provides an interactive visualization of the stations.

### Route Calculation
The route calculation determines the shortest driving path from SDG&E to a specified EV charger. The result is displayed as both text (distance) and a plotted route.

## Dependencies

The project depends on the following Python packages:
- `requests`
- `json`
- `pandas`
- `matplotlib`
- `geopandas`
- `folium`
- `osmnx`
- `networkx`

Ensure these are listed in your `requirements.txt` file for easy installation.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Data provided by the [NREL API](https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/).
- Geospatial analysis tools provided by [OSMnx](https://osmnx.readthedocs.io/) and [NetworkX](https://networkx.github.io/).

