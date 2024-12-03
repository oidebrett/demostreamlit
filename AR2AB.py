'''
Basic Requirement 2:
Create a form or poll relating to your chosen dataset on your information system that collects
and stores data from the users. This form must show evidence of the use of JavaScript.
a. The data collected should contain at least three different data types.
b. The data should be validated and stored in a database or file.
c. Some aspect of the collected data from all users should be summarised and displayed
through the information system
'''

import streamlit as st
import streamlit.components.v1 as components
import csv
import os

mycomponent = components.declare_component(
    "htmlform",
    path="./htmlform"
)

# File path of the CSV file
file_path = "data-from-users.csv"

form_value = mycomponent() 

if (form_value is not None): 
    column_headings = list(form_value.keys()) # take the keys from the json returned from form_value

    # The new row of data to add
    row_data = list(form_value.values())# take the values from the json returned from form_value
    row_data = [str(item) for item in row_data] #convert the items into strings so they can be joined into a row

    # Check if the file exists
    file_exists = os.path.exists(file_path)

    # Open the file to read and write
    with open(file_path, "a+") as file:
        file.seek(0) #go back to the start of the file
        lines = file.readlines()

        # Write headings if the file is empty
        if not file_exists or len(lines) == 0 or column_headings[0] not in lines[0]:
            file.write(",".join(column_headings) + "\n")

        # Write the new row
        file.write(",".join(row_data) + "\n")


    print("Data added successfully!")
