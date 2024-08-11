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

dash.register_page(__name__, path='/')


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
            html.Div(dcc.Dropdown(id='category-input',
                                  options=[{'label': i, 'value': i}
                                           for i in ['Apples', 'Beverages', 'Cocoa and chocolate',
                                                     'Coffee, tea, and spices', 'Dairy',
                                                     'Fish and shellfish', 'Fruits', 'Grains',
                                                     'Live meat animals', 'Meats', 'Nuts',
                                                     'Sugar and candy', 'Vegetable oils', 'Vegetables',
                                                     'Other edible products']
                                           ],
                                  value='Apples'
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
            html.Div(dcc.Graph(id='graph-1', className='graphs'))
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
                    html.Div(dcc.Graph(id='graph-2', className='graphs'))
                ])
            ]),

            # Line Break
            html.Br(),

            # Third Graph
            dbc.Row([
                dbc.Col([
                    html.Div(dcc.Graph(id='graph-3', className='graphs'))
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


# ------------------------------------------------------------------------------------------------------------------
# LOAD THE DATA
fruit_prices = pd.read_csv('data/Fruit-Prices-2022.csv')


# ------------------------------------------------------------------------------------------------------------------
# GRAPH FUNCTIONS
def bar_chart(data, x_column, y_column, x_label, y_label, title, formatting=1):
    # Set up the figure
    fig = go.Figure()
    # Draws the figure
    fig.add_trace(go.Bar(x=data[x_column], y=data[y_column],
                         marker=dict(color=['#B4BEC9', '#B4BEC9', '#B4BEC9', '#D9560B', '#D9560B']),
                         name=title,
                         orientation='h',
                         text=['${:,}'.format(round(i * formatting, 2)) for i in
                               data[x_column]],
                         textfont=dict(color='white', size=14),
                         textposition='inside')  # more ['inside', 'outside', 'none']
                  )

    #

    return fig


# ------------------------------------------------------------------------------------------------------------------
# CALLBACK SECTION

# Callback for ...
@callback(Output(component_id='graph-1', component_property='figure'),
          Input(component_id='category-input', component_property='value'))
def fruits_prices(category_input):
    # Group the data
    df = fruit_prices.groupby('Fruit Category')[['RetailPrice']].mean().reset_index().sort_values(by='RetailPrice')
    return bar_chart(data=df, x_column='RetailPrice', y_column='Fruit Category', x_label='X', y_label='Y',
                     title='The title')
