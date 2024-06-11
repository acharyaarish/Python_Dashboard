import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from data_processing import load_and_preprocess_data
from styles import app_style, index_string

# Load and preprocess data
data, species_options, date_range = load_and_preprocess_data('Wildlife_incident_locations_20240609.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# External CSS
app.css.append_css({
    'external_url': 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'
})

# Inline CSS for custom styles
app.layout = html.Div(style=app_style, children=[
    html.H1(children='Wildlife Incidents in Canberra', style={
        'textAlign': 'center',
        'marginBottom': '10px',
        'fontSize': '24px'
    }),

    html.Div(children=[
        html.Label('Select Species:', style={
            'fontWeight': 'bold',
            'marginRight': '5px',
            'fontSize': '12px'
        }),
        dcc.Dropdown(
            id='species-dropdown',
            options=species_options,
            value='All',
            clearable=False,
            style={
                'width': '120px',
                'display': 'inline-block',
                'verticalAlign': 'middle',
                'marginRight': '5px',
                'backgroundColor': '#ecf0f1',
                'color': '#34495e',
                'border': 'none',
                'borderRadius': '4px',
                'padding': '2px',
                'fontSize': '10px'
            }
        ),
        html.Label('Select Date Range:', style={
            'fontWeight': 'bold',
            'marginRight': '5px',
            'fontSize': '12px',
            'verticalAlign': 'middle'
        }),
        dcc.DatePickerRange(
            id='date-picker',
            start_date=date_range['min'],
            end_date=date_range['max'],
            display_format='YYYY-MM-DD',
            style={
                'display': 'inline-block',
                'verticalAlign': 'middle',
                'backgroundColor': '#ecf0f1',
                'color': '#34495e',
                'border': 'none',
                'borderRadius': '4px',
                'padding': '2px',
                'fontSize': '10px',
                'width': '290px'
            }
        ),
    ], style={
        'textAlign': 'center',
        'marginBottom': '10px',
        'padding': '10px',
        'backgroundColor': '#34495e',
        'borderRadius': '10px'
    }),

    html.Div(style={
        'display': 'flex',
        'flexDirection': 'row',
        'justifyContent': 'space-between',
        'marginBottom': '10px',
        'gap': '10px'
    }, children=[
        dcc.Graph(id='species-bar', style={
            'flex': '1',
            'height': '300px',
            'padding': '10px',
            'backgroundColor': '#34495e',
            'borderRadius': '10px',
            'fontSize': '12px'
        }),
        dcc.Graph(id='time-histogram', style={
            'flex': '1',
            'height': '300px',
            'padding': '10px',
            'backgroundColor': '#34495e',
            'borderRadius': '10px',
            'fontSize': '12px'
        }),
    ]),

    dcc.Graph(id='geo-scatter', style={
        'width': '100%',
        'height': '400px',
        'padding': '10px',
        'backgroundColor': '#34495e',
        'borderRadius': '10px',
        'fontSize': '12px',
        'margin': '10px 0'
    })
])

# Custom CSS to improve dropdown readability
app.index_string = index_string

# Callbacks to update graphs based on user input
@app.callback(
    [Output('species-bar', 'figure'),
     Output('time-histogram', 'figure'),
     Output('geo-scatter', 'figure')],
    [Input('species-dropdown', 'value'),
     Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')]
)
def update_graphs(selected_species, start_date, end_date):
    # Filter data based on user selections
    filtered_data = data[(data['CREATED_DATE'] >= start_date) & (data['CREATED_DATE'] <= end_date)]
    if selected_species != 'All':
        filtered_data = filtered_data[filtered_data['SPECIES'] == selected_species]

    # Number of Incidents by Species
    species_count = filtered_data['SPECIES'].value_counts().reset_index()
    species_count.columns = ['Species', 'Count']
    fig_species = px.bar(species_count, x='Species', y='Count', title='Number of Incidents by Species',
                         labels={'Count': 'Number of Incidents'},
                         color_discrete_sequence=px.colors.qualitative.Dark2)
    fig_species.update_layout(
        xaxis_title='Species',
        yaxis_title='Number of Incidents',
        template='plotly_dark',
        margin=dict(l=10, r=10, t=30, b=150),
        font=dict(size=10, color='#ecf0f1'),
        bargap=0.15,
        paper_bgcolor='#2c3e50',
        plot_bgcolor='#2c3e50',
        xaxis=dict(tickangle=45)
    )

    # Incidents Over Time
    fig_time = px.histogram(filtered_data, x='CREATED_DATE', title='Incidents Over Time',
                            labels={'CREATED_DATE': 'Date', 'count': 'Number of Incidents'},
                            color_discrete_sequence=['#e74c3c'])
    fig_time.update_layout(
        xaxis_title='Date',
        yaxis_title='Number of Incidents',
        template='plotly_dark',
        margin=dict(l=10, r=10, t=30, b=80),
        font=dict(size=10, color='#ecf0f1'),
        bargap=0.2,
        paper_bgcolor='#2c3e50',
        plot_bgcolor='#2c3e50',
        xaxis=dict(tickangle=0)
    )

    # Geographic Distribution of Incidents
    fig_geo = px.scatter_mapbox(filtered_data, lat='LATITUDE', lon='LONGITUDE', color='SPECIES', hover_name='SPECIES',
                                hover_data=['CREATED_DATE'], zoom=10, height=400, title='Geographic Distribution of Incidents',
                                color_discrete_sequence=px.colors.qualitative.Dark2)
    fig_geo.update_layout(
        mapbox_style="open-street-map",
        margin=dict(l=10, r=10, t=30, b=10),
        font=dict(size=10, color='#ecf0f1'),
        hovermode='closest',
        dragmode=False,
        paper_bgcolor='#2c3e50',
        plot_bgcolor='#2c3e50'
    )
    fig_geo.update_traces(marker=dict(size=8))

    return fig_species, fig_time, fig_geo

if __name__ == '__main__':
    app.run_server(debug=True)
