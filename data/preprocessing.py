import pandas as pd

# Load the datasets
co2_by_region_path = 'annual-co-emissions-by-region.csv'  # Update with your file path
continents_data_path = 'continents2.csv'  # Update with your file path

# Read the CO2 emissions by region data
co2_data = pd.read_csv(co2_by_region_path)

# Read the continents data
continents_data = pd.read_csv(continents_data_path)

# Extract only the rows for the year 2022
co2_2022 = co2_data[co2_data['Year'] == 2022]

# Merge with continents data on 'Entity' and 'name'
# Assuming 'Entity' in CO2 data corresponds to 'name' in continents data
combined_data = pd.merge(co2_2022, continents_data[['name', 'region']], left_on='Entity', right_on='name')

# Display the combined data
print(combined_data)

# Optionally, save the combined data to a new CSV file
combined_data.to_csv('combined_co2_continents_2022.csv', index=False)
