import pandas as pd
import matplotlib.pyplot as plt

# Load COVID-19 data from a CSV file
data = pd.read_csv('covid_data.csv')

# View the first few rows of the data to understand its structure
print(data.head())

# Basic statistics of the data
print(data.describe())

# Data preprocessing
data['Date'] = pd.to_datetime(data['Date'])  # Convert the 'Date' column to a datetime object
data.set_index('Date', inplace=True)  # Set 'Date' as the index

# Plot the total cases over time
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['TotalCases'], label='Total Cases', color='b')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.title('COVID-19 Total Cases Over Time')
plt.legend()
plt.grid()
plt.show()

# Calculate and plot daily new cases
data['DailyNewCases'] = data['TotalCases'].diff().fillna(0)
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['DailyNewCases'], label='Daily New Cases', color='r')
plt.xlabel('Date')
plt.ylabel('Daily New Cases')
plt.title('COVID-19 Daily New Cases')
plt.legend()
plt.grid()
plt.show()

# Perform other analyses as needed, such as regional breakdowns, mortality rates, and more.

# Save the processed data if necessary
data.to_csv('processed_covid_data.csv')
