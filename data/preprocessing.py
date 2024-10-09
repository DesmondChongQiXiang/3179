import pandas as pd

# Load the CO2 emissions data
co2_data_path = 'combined_co2_continents_2022.csv'  # Update with your actual file path
co2_data = pd.read_csv(co2_data_path)

# Group the data by region and calculate the total emissions for each region
grouped_data = co2_data.groupby('Continent', as_index=False).agg({
    'Annual CO₂ emissions': 'sum'  # Sum emissions for each region
})

# Display the grouped data
print(grouped_data)

# Optionally, save the grouped data to a new CSV file
grouped_data.to_csv('grouped_co2_emissions_by_region.csv', index=False)
