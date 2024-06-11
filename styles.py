app_style = {
    'backgroundColor': '#2c3e50',
    'color': '#ecf0f1',
    'padding': '10px',
    'fontFamily': 'Arial, sans-serif'
}

index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            .Select-control {
                background-color: #ecf0f1 !important;
                color: #34495e !important;
                font-size: 10px !important;
                padding: 2px !important;
            }
            .Select-menu-outer {
                background-color: #34495e !important;
                color: #ecf0f1 !important;
                font-size: 10px !important;
                padding: 2px !important;
            }
            .Select-option {
                background-color: #34495e !important;
                color: #ecf0f1 !important;
                padding: 10px !important;
                font-weight: bold !important;
                font-family: Arial, sans-serif !important;
            }
            .Select-option:hover {
                background-color: #2980b9 !important;
                color: #ecf0f1 !important;
            }
            .Select-option.is-focused {
                background-color: #2980b9 !important;
                color: #ecf0f1 !important;
            }
            .Select-option.is-selected {
                background-color: #2980b9 !important;
                color: #ecf0f1 !important;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''
