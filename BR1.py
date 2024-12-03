'''
Basic requirement 1. Collect and prepare the data
a. Select the dataset you will use.
b. Use Python to extract, clean and store the data that you will need for your project into
a suitable format.
You will need to provide clear evidence of how you extracted, cleaned and stored this
data set
'''

import pandas as pd

# File path of the CSV file to extract
file_path = "2023-Make-and-Model-Data.csv"
cleaned_file_path = "cleaned-data.csv"

df = pd.read_csv(file_path)

# Ensure columns are named correctly and trimmed of any extra spaces
df.columns = df.columns.str.strip()

# Check for missing values in the Totals column indicating no tests and remove them
missing_in_column = df['Total'].isnull().sum()
if missing_in_column > 0:
    print(f"Numbber of missing rows without a test ie. 'Total' is empty: {missing_in_column}")
    df_cleaned = df.dropna() # drop the row that is entry
else:
    df_cleaned = df

# We only want the data Grouped by Vehicle Make and Model (average across all years of that make/model)
grouped = df_cleaned.groupby(['Vehicle Make', 'Vehicle Model']).agg({
    'PASS': 'sum',
    'FAIL': 'sum'
}).reset_index()

# Calculate total tests for each group
grouped['Total'] = grouped['PASS'] + grouped['FAIL']

# Calculate pass and fail percentages
grouped['PASS %'] = (grouped['PASS'] / grouped['Total']) * 100
grouped['FAIL %'] = (grouped['FAIL'] / grouped['Total']) * 100

# Final summarized DataFrame
result = grouped[['Vehicle Make', 'Vehicle Model', 'PASS %', 'FAIL %']]

# Display the result
print(result)

# Write out the cleaned file
grouped.to_csv(cleaned_file_path, index=False)  