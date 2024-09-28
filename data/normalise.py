import pandas as pd

# Load the datasets
income_data = pd.read_csv('hh_income_state.csv')
population_data = pd.read_csv('population_state.csv')

# Convert 'date' columns to datetime format
income_data['date'] = pd.to_datetime(income_data['date'])
population_data['date'] = pd.to_datetime(population_data['date'])

# Filter the datasets for the year 2022
income_2022 = income_data[income_data['date'].dt.year == 2022]
population_2022 = population_data[population_data['date'].dt.year == 2022]

# Select the most recent data for each state (if necessary)
latest_income_2022 = income_2022.loc[income_2022.groupby('state')['date'].idxmax()]
latest_population_2022 = population_2022.loc[population_2022.groupby('state')['date'].idxmax()]


# Merge datasets on 'state'
merged_data = pd.merge(latest_income_2022[['state', 'income_mean']], 
                        latest_population_2022[['state', 'population']], 
                        on='state')

# Calculate per capita income
merged_data['per_capita_income'] = merged_data['income_mean'] / merged_data['population']

# Display the updated DataFrame
print(merged_data)
