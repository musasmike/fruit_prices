# Import required packages
import pandas as pd
import numpy as np
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import base64

# ------------------------------------------------------------------------------------------------------------------
# APP INITIALIZATION
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)


# Insert an image
image_file = 'assets/mmk_logo_desgin.png'
encoded_image = base64.b64encode(open(image_file, 'rb').read()).decode('ascii')


# ------------------------------------------------------------------------------------------------------------------
# APP SIDEBAR
sidebar = dbc.Navbar([
    dbc.NavLink([
        html.Div(page['name'])
    ],
        href=page['path'],
        active='exact',
        className='ms-2'
    ) for page in dash.page_registry.values()
],
    className='navbar',
)


# ------------------------------------------------------------------------------------------------------------------
# APP LAYOUT
app.layout = html.Div(children=[
    # --------------------------------------------------------------------------------------------------------------
    # TITLE SECTION
    dbc.Row(children=[
        dbc.Col(children=[
            html.Div('U.S.A. FRUITS & VEGETABLES PRICES', id='title', className='dash-title')
        ],
            width={'size': 10},
            xs=12, sm=8, md=8, lg=10, xl=10
        )
    ],
        className='title-section',
        justify='center'
    ),

    # --------------------------------------------------------------------------------------------------------------
    # Section Break and Line
    html.Br(),
    dbc.Row(dbc.Col(html.Div(), width={'size': 10}, className='break-line'), justify='center'),
    html.Br(),

    # --------------------------------------------------------------------------------------------------------------
    # FILTER SECTION
    dbc.Row(children=[
        # Buttons Section
        dbc.Col([
            sidebar,
        ],
            width={'size': 4, 'offset': 1},
            xs=12, sm=10, md=10, lg=4, xl=4
        ),

    ],
        justify='left',
    ),

    # Line Break Section
    html.Br(),

    # Content of each page
    dash.page_container,

    # Section Break and Line
    html.Br(),
    html.Br(),
    dbc.Row(dbc.Col(html.Div(), width={'size': 10}, className='break-line'), justify='center'),
    html.Br(),

    # --------------------------------------------------------------------------------------------------------------
    # FOOTER SECTION
    dbc.Row([
        # Made by
        dbc.Col([
            html.Div([
                # Copyright
                html.Div('Made by', style={'margin-right': '5px'}),
                html.Div('Mike Musas', style={'margin-right': '5px'}),
                html.Div('|', style={'margin-right': '5px'}),

                # Data Source
                html.Div('Data Source:', style={'margin-right': '5px'}),
                html.Div(html.A("data.gov", href='https://catalog.data.gov/dataset/fruit-and-vegetable-prices',
                                style={'color': '#F2A444', 'font-family': 'Lato', 'font-weight': 'bold'}))

            ], className='copyright')
        ],
            width={'size': 9},
            xs=12, sm=8, md=8, lg=9, xl=9
        ),

        # Logo
        dbc.Col([
            html.Div(html.Img(src='data:image/png;base64,{}'.format(encoded_image)),
                     className='logo'
                     )
        ],
            width={'size': 1},
            xs=4, sm=2, md=2, lg=1, xl=1
        )
    ],
        justify='center'
    ),

    # Line Break
    html.Br(),


])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
