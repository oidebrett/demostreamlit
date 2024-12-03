import streamlit as st
import streamlit.components.v1 as components
import csv
import os

mycomponent = components.declare_component(
    "htmlform",
    path="./htmlform"
)

# File path of the CSV file
file_path = "data.csv"

form_value = mycomponent() 

st.write(form_value)

if (form_value is not None): 
    column_headings = list(form_value.keys()) # take the keys from the json returned from form_value

    # The new row of data to add
    #row_data = list(form_value.values())
    st.write(form_value)

    '''
    # Check if the file exists
    file_exists = os.path.exists(file_path)

    # Open the file in append mode ('a' for append, '+' to create if not exists)
    with open(file_path, mode='a+', newline='') as csvfile:
        csvfile.seek(0)  # Go to the start of the file to check headers
        reader = csv.reader(csvfile)
        writer = csv.writer(csvfile)
        
        # Read the current headers
        headers = next(reader, [])
        
        # If headers are missing or incomplete, write the required columns
        if not file_exists or headers != column_headings:
            csvfile.seek(0)  # Reset file position to overwrite
            csvfile.truncate()  # Clear the file to write new headers
            writer.writerow(column_headings)
        
        # Add the new data row
        writer.writerow(row_data)
    '''
    print("Data added successfully!")
