'''
Basic Requirement 2: Data analytics and visualisation
a. Use Python to carry out analytics on your data and to create at least two different basic
visualisations (e.g., bar chart, line graph, pie chart) with each representing different key
aspects of the dataset.
b. Ensure that each visualisation is clearly labelled with titles, axis labels, and legends
where appropriate.
c. You should use Python data structure(s) such as lists, tuples or dictionaries to manage
the data you will be analysing.
'''

import pandas as pd
import plotly.express as px

# Read the CSV file into a DataFrame
file_path = "cleaned-data.csv"  # The CSV file path to the cleaned data
df = pd.read_csv(file_path)

# 1. Analytics: Total vehicles tested per vehicle make
total_per_make = df.groupby('Vehicle Make')['Total'].sum().reset_index()

# 2. Analytics: Overall pass and fail percentages
overall_pass = df['PASS'].sum()
overall_fail = df['FAIL'].sum()
total_tests = overall_pass + overall_fail
overall_pass_percentage = (overall_pass / total_tests) * 100
overall_fail_percentage = (overall_fail / total_tests) * 100

# Visualization 1: Bar chart for total vehicles tested per make
fig1 = px.bar(
    total_per_make,
    x='Vehicle Make',
    y='Total',
    title='Total Vehicles Tested per Make',
    labels={'Total': 'Total Vehicles Tested', 'Vehicle Make': 'Vehicle Make'},
    text='Total'
)
fig1.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig1.update_layout(xaxis_tickangle=-45)

# Visualization 2: Pie chart for overall pass vs fail percentages
overall_data = {
    "Result": ["Pass", "Fail"],
    "Percentage": [overall_pass_percentage, overall_fail_percentage]
}
overall_df = pd.DataFrame(overall_data)

fig2 = px.pie(
    overall_df,
    names='Result',
    values='Percentage',
    title='Overall Pass vs Fail Percentage',
    labels={'Result': 'Result', 'Percentage': 'Percentage'},
    color_discrete_sequence=px.colors.sequential.RdBu
)

# Print the analytics
print("Total vehicles tested per make:")
print(total_per_make)

print("\nOverall Pass Percentage: {:.2f}%".format(overall_pass_percentage))
print("Overall Fail Percentage: {:.2f}%".format(overall_fail_percentage))

# Show the visualizations
choice = input("Show fig1 of fig2? ")
if choice == 'fig1':
    fig1.show()
elif choice == 'fig2':
    fig2.show()
else:
    print("you must choose fig1 or fig2")

