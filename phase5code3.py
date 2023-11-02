import pandas as pd
import matplotlib.pyplot as plt

# Load COVID-19 data from a CSV file
covid_data = pd.read_csv('covid_data.csv')

# Explore the dataset
print(covid_data.head())  # Display the first few rows of the dataset

# Data preprocessing (if needed)
# For example, you can convert the 'Date' column to a proper date format:
# covid_data['Date'] = pd.to_datetime(covid_data['Date'])

# Basic statistics
total_cases = covid_data['Confirmed'].sum()
total_deaths = covid_data['Deaths'].sum()
total_recovered = covid_data['Recovered'].sum()

print(f'Total cases: {total_cases}')
print(f'Total deaths: {total_deaths}')
print(f'Total recovered: {total_recovered}')

# Plotting data
plt.figure(figsize=(12, 6))
plt.plot(covid_data['Date'], covid_data['Confirmed'], label='Confirmed Cases', color='b')
plt.plot(covid_data['Date'], covid_data['Deaths'], label='Deaths', color='r')
plt.plot(covid_data['Date'], covid_data['Recovered'], label='Recovered', color='g')
plt.xlabel('Date')
plt.ylabel('Counts')
plt.title('COVID-19 Cases Over Time')
plt.legend()
plt.grid()
plt.show()
