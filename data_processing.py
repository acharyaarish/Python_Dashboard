import pandas as pd

def load_and_preprocess_data(file_path):
    # Load the data
    data = pd.read_csv(file_path)

    # Convert CREATED_DATE to datetime with the specified format
    data['CREATED_DATE'] = pd.to_datetime(data['CREATED_DATE'], format='%m/%d/%Y %I:%M:%S %p')

    # Fill missing values in SPECIES with 'Unknown'
    data['SPECIES'] = data['SPECIES'].fillna('Unknown')

    # Generate species options for the dropdown
    species_options = [{'label': species, 'value': species} for species in data['SPECIES'].unique()]
    species_options.append({'label': 'All', 'value': 'All'})

    # Get the date range for the date picker
    date_range = {'min': data['CREATED_DATE'].min(), 'max': data['CREATED_DATE'].max()}

    return data, species_options, date_range
