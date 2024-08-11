# Import required packages
import pandas as pd
import numpy as np
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html, callback
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# ------------------------------------------------------------------------------------------------------------------
# APP INITIALIZATION

dash.register_page(__name__)

# ------------------------------------------------------------------------------------------------------------------
# LOAD THE DATA
fruit_prices = pd.read_csv('data/Vegetable-Prices-2022.csv')

# ------------------------------------------------------------------------------------------------------------------
# APP LAYOUT
layout = html.Div(children=[
    # --------------------------------------------------------------------------------------------------------------
    # Section Break and Line
    html.Br(),


    # --------------------------------------------------------------------------------------------------------------
    # FILTER SECTION
    dbc.Row(children=[
        # Drop Down Menu
        dbc.Col([
            html.Div(dcc.Dropdown(id='v-category-input',
                                  options=[{'label': i, 'value': i}
                                           for i in ['Acorn squash', 'Artichoke', 'Asparagus', 'Avocados', 'Beets',
                                                     'Beans', 'Peas', 'Broccoli', 'Brussels sprouts',
                                                     'Butternut squash', 'Cabbage', 'Carrots', 'Cauliflower', 'Celery',
                                                     'Collard greens', 'Corn', 'Cucumbers', 'Peppers', 'Kale',
                                                     'Lentils', 'Lettuce', 'Mixed vegetables', 'Mushrooms', 'Mustard',
                                                     'Okra', 'Olives', 'Onions', 'Potatoes', 'Pumpkin', 'Radish',
                                                     'Spinach', 'Tomatoes', 'Turnip', 'Zucchini']
                                           ],
                                  value='Acorn squash'
                                  ))
        ],
            width={'size': 5},
            xs=10, sm=10, md=10, lg=5, xl=5
        ),

        # Buttons Section
        dbc.Col([
        ],
            width={'size': 5},
            xs=10, sm=10, md=10, lg=5, xl=5
        ),

    ],
        justify='center'
    ),

    # Line Break Section
    html.Br(),

    # --------------------------------------------------------------------------------------------------------------
    # GRAPHS SECTION
    dbc.Row(children=[
        # ----------------------------------------------------------------------------------------------------------
        # First Graph Section
        dbc.Col([
            html.Div(dcc.Graph(id='v-graph-1', className='graphs'))
        ],
            width={'size': 5},
            xs=10, sm=10, md=10, lg=5, xl=5
        ),

        # Line Break
        html.Br(),

        # ----------------------------------------------------------------------------------------------------------
        # Second & Third Graph Section
        dbc.Col([
            # Second Graph
            dbc.Row([
                dbc.Col([
                    html.Div(dcc.Graph(id='v-graph-2', className='graphs'))
                ])
            ]),

            # Line Break
            html.Br(),

            # Third Graph
            dbc.Row([
                dbc.Col([
                    html.Div(dcc.Graph(id='v-graph-3', className='graphs'))
                ])
            ])

        ],
            width={'size': 5},
            xs=10, sm=10, md=10, lg=5, xl=5
        )
    ],
        justify='center'
    )
])


