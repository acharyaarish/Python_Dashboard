
## Overview

This dashboard visualizes wildlife incidents in Canberra, providing insights into the number of incidents by species, their distribution over time, and their geographic locations. It is built using Dash, Plotly, and Pandas.

# Python Dashboard

This project is deployed and can be accessed [here](http://ec2-52-62-61-15.ap-southeast-2.compute.amazonaws.com).


![F9B40F03-EFD9-48CB-AF35-9F4316A8681F](https://github.com/acharyaarish/Python_Dashboard/assets/87922896/63b84853-03a9-4b99-8c5f-1a04f2b8b247)

![7FBDD433-8DE0-43F9-8209-CDEC00C493E5](https://github.com/acharyaarish/Python_Dashboard/assets/87922896/7f7bc64e-b44c-49f6-8dbd-453b02704af1)

![D8FC5332-682A-44E1-B0F1-59EF9B9DC726](https://github.com/acharyaarish/Python_Dashboard/assets/87922896/5bdaddf7-5075-4ff6-b100-86bdc0aa04e6)

![024A30C6-6EC6-4FDE-B3AB-2E0130F05EC5](https://github.com/acharyaarish/Python_Dashboard/assets/87922896/264f2c21-0e57-4c98-b662-a601fc722644)


## Features

- Select Species: Dropdown to filter incidents by species.
- Select Date Range: Date picker to filter incidents by date range.
- Number of Incidents by Species: Bar chart displaying the number of incidents for each species.
- Incidents Over Time: Histogram showing the number of incidents over time.
- Geographic Distribution of Incidents: Interactive map showing the locations of incidents.

## File Structure

- `app.py`: Main application file containing the layout and callbacks.
- `data_processing.py`: Handles data loading and preprocessing.
- `styles.py`: Contains custom CSS styles for the dashboard.

## Prerequisites

- Python 3.x
- Dash
- Plotly
- Pandas

## Installation

1. Clone the repository:

   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Create a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```sh
   pip install dash plotly pandas
   ```

## Running the Dashboard

1. Place the CSV file in the directory:
   
   Ensure the `Wildlife_incident_locations_20240609.csv` file is in the same directory as the Python files.

2. Run the application:

   ```sh
   python app.py
   ```

3. Access the dashboard:

   Open your web browser and go to `http://127.0.0.1:8050/` to view the dashboard.

## Files and Directories

- `app.py`: The main application file. It defines the layout of the dashboard and contains the callback functions to update the graphs based on user inputs.

- `data_processing.py`: A helper file for loading and preprocessing the data. It includes functions to load the CSV file, convert date formats, and prepare data for the dashboard.

- `styles.py`: Contains custom styles for the dashboard elements. It includes CSS rules to style the dropdown menus, labels, and other components.

## Code Explanation

### app.py

- Imports: Imports necessary libraries and functions from other files.
- Data Loading: Calls the function from `data_processing.py` to load and preprocess the data.
- Layout: Defines the layout of the dashboard, including dropdowns, date picker, and graphs.
- Callbacks: Defines callback functions to update the graphs based on user inputs.

### data_processing.py

- load_and_preprocess_data: A function to load the CSV file, convert date formats, fill missing values, and prepare dropdown options and date range.

### styles.py

- app_style: A dictionary containing CSS styles for the dashboard.
- index_string: Custom HTML and CSS to improve the readability and appearance of dropdown menus.

## Customization

You can customize the dashboard by modifying the layout, styles, or data processing logic:

- Adding new graphs: You can add new graphs by modifying the `app.layout` in `app.py` and creating new callback functions.
- Changing styles: Update the styles in `styles.py` to change the appearance of the dashboard.
- Processing new data: Modify `data_processing.py` to handle different datasets or preprocessing steps.

## Troubleshooting

- Missing packages: Ensure all required packages are installed using `pip install dash plotly pandas`.
- Data loading issues: Verify the CSV file format and ensure it matches the expected structure.
- Server errors: Check the terminal for error messages and ensure the server is running without issues.

## Dataset

https://data.gov.au/dataset/ds-act-https%3A%2F%2Fwww.data.act.gov.au%2Fapi%2Fviews%2Fqw4j-6rbq/details?q=wildlife
