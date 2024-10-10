import pandas as pd

# Load the CO2 emissions data
co2_data_path = 'world_emissions_by_sector.csv'  # Update with your actual file path
co2_data = pd.read_csv(co2_data_path)

sector_mapping = {
    "Carbon dioxide emissions from buildings": "Buildings",
    "Carbon dioxide emissions from bunker fuels": "Bunker Fuels",

    "Carbon dioxide emissions from electricity and heat": "Electricity & Heat",
    "Carbon dioxide emissions from land use change and forestry": "Land Use",
    "Carbon dioxide emissions from other fuel combustion": "Other Fuels",
    "Carbon dioxide emissions from transport": "Transport",
    "Carbon dioxide emissions from manufacturing and construction": "Manufacturing",
    "Fugitive emissions of carbon dioxide from energy production": "Fugitive Emissions",
    "Carbon dioxide emissions from industry": "Industry"
}

# Replace sector names
co2_data['Sector'] = co2_data['Sector'].replace(sector_mapping)

# Display the grouped data
print(co2_data)

# Optionally, save the grouped data to a new CSV file
co2_data.to_csv('1world_emissions_by_sector.csv', index=False)
