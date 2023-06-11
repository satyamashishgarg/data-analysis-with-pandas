import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Get the summary statistics of numerical columns
print(df.describe())

# Calculate the average value of a specific column
average = df['column_name'].mean()
print(f"Average: {average}")

# Group data by a column and calculate the average of another column
grouped_data = df.groupby('group_column')['value_column'].mean()
print(grouped_data)
