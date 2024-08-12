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

        dbc.Col([
            # Filter title
            html.Div("Top or Least Values", className='filter-title'),
            # Top 10 Values
            html.Div(dcc.Dropdown(id='v-top-input',
                                  options=[{'label': i, 'value': i}
                                           for i in ['All', 'Top 7', 'Least 7']
                                           ],
                                  value='All'
                                  ))

        ],
            width={'size': 5},
            xs=12, sm=10, md=10, lg=5, xl=5
        ),

        # Buttons Section
        dbc.Col([

            # Filter title
            html.Div("Categories", className='filter-title'),
            # Drop Down Menu
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
            xs=12, sm=10, md=10, lg=5, xl=5
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
            xs=12, sm=10, md=10, lg=5, xl=5
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
            xs=12, sm=10, md=10, lg=5, xl=5
        )
    ],
        justify='center'
    )
])


# ------------------------------------------------------------------------------------------------------------------
# LOAD THE DATA
vegetable_prices = pd.read_csv('data/Vegetable-Prices-2022.csv')

# ------------------------------------------------------------------------------------------------------------------
# GRAPH FUNCTIONS
# SINGLE BARCHART
def bar_chart(data, x_column, y_column, x_label, y_label, title, color, formatting=1):
    # Set up the figure
    fig = go.Figure()
    # Draws the figure
    fig.add_trace(go.Bar(x=data[x_column], y=data[y_column],
                         marker=dict(color=color),
                         name=title,
                         orientation='h',
                         text=['${:,}'.format(round(i * formatting, 2)) for i in
                               data[x_column]],
                         textfont=dict(color='white', size=14),
                         textposition='inside')  # more ['inside', 'outside', 'none']
                  )

    # Figure layout Updates
    fig.update_layout(
        # Graph Title
        title=dict(
            text=title,
            font=dict(size=22, color='#0C0B09'),
        ),
        # X-axis Label
        xaxis_title=dict(
            text=x_label,
            font=dict(size=14, color='#595959')
        ),
        # X-axis formatting
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='#D9D9D9',
            linewidth=2,
            ticks='outside',
            tickcolor='#595959',
            tickfont=dict(
                color='#595959'
            )
        ),
        # Y-axis Label
        yaxis=dict(
            showline=False,
            showgrid=False,
            showticklabels=True,
            linecolor='#D9D9D9',
            linewidth=2,
            tickfont=dict(
                color='#595959'
            )
        ),
        # Plot background
        plot_bgcolor='white',
        # Adjust the margins of the graph
        margin=dict(
            l=120,
            r=30,
            b=70,
            t=70,
            pad=4
        )
    )

    return fig


# GROUPED BARCHART
def stacked_bar_chart(data, x_column, currency, z_column, x_label, y_label, title, formatting=1):
    # The data
    fig = go.Figure()

    # colors
    colors_dict = {'Fresh': '#1F736A', 'Canned': '#DBD96E', 'Juice': '#6EDB7E', 'Dried': '#D98841', 'Frozen': '#F2B138'}

    for i in z_column:
        fig.add_trace(go.Bar(x=data[i],
                             y=data[x_column],
                             name=i,
                             orientation='h',
                             marker=dict(color=colors_dict[i]),
                             text=['{}{:,}'.format(currency, round(j * formatting, 2)) for j in
                                   data[i]],
                             textfont=dict(color='white', size=14),
                             textposition='inside'
                             ))

    fig.update_traces(width=0.6)
    # Rotate the x-axis labels
    fig.update_xaxes(tickangle=0)
    # Layout
    fig.update_layout(
        # Graph Title
        title=dict(
            text=title,
            font=dict(size=22, color='#0C0B09'),
        ),
        # X-axis Label
        xaxis_title=dict(
            text=x_label,
            font=dict(size=14, color='#595959')
        ),
        # X-axis Label
        yaxis_title=dict(
            text=y_label,
            font=dict(size=14, color='#595959')
        ),
        # X-axis formatting
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='#D9D9D9',
            linewidth=2,
            ticks='outside',
            tickcolor='#595959',
            tickfont=dict(
                color='#595959'
            )
        ),
        # Y-axis Label
        yaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='#D9D9D9',
            linewidth=2,
            tickfont=dict(
                color='#595959'
            )
        ),
        # Plot background
        plot_bgcolor='white',
        barmode='stack',
        bargap=0.15,
        bargroupgap=0.1,
        # Legend
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        # Adjust the margins of the graph
        margin=dict(
            l=120,
            r=30,
            b=70,
            t=70,
            pad=4
        )
    )

    return fig


# GROUPED BARCHART
def grouped_bar_chart(data, x_column, currency, z_column, x_label, y_label, title, formatting=1):
    # The data
    fig = go.Figure()

    # colors
    colors_dict = {'Fresh': '#1F736A', 'Canned': '#DBD96E', 'Juice': '#6EDB7E', 'Dried': '#D98841', 'Frozen': '#F2B138'}

    for i in z_column:
        fig.add_trace(go.Bar(x=data[i],
                             y=data[x_column],
                             name=i,
                             orientation='h',
                             marker=dict(color=colors_dict[i]),
                             text=['{:,}{}'.format(round(j * formatting, 2), currency) for j in
                                   data[i]],
                             textfont=dict(color='white', size=14),
                             textposition='inside'
                             ))

    fig.update_traces(width=0.3)
    # Rotate the x-axis labels
    fig.update_xaxes(tickangle=0)
    # Layout
    fig.update_layout(
        # Graph Title
        title=dict(
            text=title,
            font=dict(size=22, color='#0C0B09'),
        ),
        # X-axis Label
        xaxis_title=dict(
            text=x_label,
            font=dict(size=14, color='#595959')
        ),
        # X-axis Label
        yaxis_title=dict(
            text=y_label,
            font=dict(size=14, color='#595959')
        ),
        # X-axis formatting
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='#D9D9D9',
            linewidth=2,
            ticks='outside',
            tickcolor='#595959',
            tickfont=dict(
                color='#595959'
            )
        ),
        # Y-axis Label
        yaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='#D9D9D9',
            linewidth=2,
            tickfont=dict(
                color='#595959'
            )
        ),
        # Plot background
        plot_bgcolor='white',
        barmode='group',
        bargap=0.25,
        bargroupgap=0.05,
        # Legend
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        # Adjust the margins of the graph
        margin=dict(
            l=120,
            r=30,
            b=70,
            t=70,
            pad=4
        )
    )

    return fig


# ------------------------------------------------------------------------------------------------------------------
# CALLBACK SECTION

# Callback for Fruits Graph 1
@callback(

    Output(component_id='v-graph-1', component_property='figure')
    ,
    [
        Input(component_id='v-category-input', component_property='value'),
        Input(component_id='v-top-input', component_property='value')
    ])
def fruits_categories_prices(category_input, top_input):
    # Colors
    all_values = ['#B4BEC9', '#B4BEC9', '#B4BEC9', '#B4BEC9', '#B4BEC9', '#B4BEC9', '#B4BEC9',
                  '#B4BEC9', '#B4BEC9', '#B4BEC9', '#B4BEC9', '#B4BEC9', '#B4BEC9', '#B4BEC9',
                  '#1F736A', '#1F736A', '#1F736A', '#1F736A', '#1F736A', '#1F736A', '#1F736A',
                  '#1F736A', '#1F736A', '#1F736A']
    top = ['#1F736A', '#1F736A', '#1F736A', '#1F736A', '#1F736A', '#1F736A', '#1F736A',
           '#1F736A', '#1F736A', '#1F736A']
    least = ['#B4BEC9', '#B4BEC9', '#B4BEC9', '#B4BEC9', '#B4BEC9', '#B4BEC9', '#B4BEC9',
             '#B4BEC9', '#B4BEC9', '#B4BEC9', '#B4BEC9', '#B4BEC9', '#B4BEC9', '#B4BEC9',
             '#1F736A', '#1F736A', '#1F736A', '#1F736A', '#1F736A', '#1F736A', '#1F736A',
             '#1F736A', '#1F736A', '#1F736A']
    # First Graph
    if top_input == 'All':
        # Group the data
        df = vegetable_prices.groupby('Vegetable Category')[['RetailPrice']].mean().reset_index().sort_values(
            by='RetailPrice')
        return bar_chart(data=df, x_column='RetailPrice', y_column='Vegetable Category',
                         x_label='Retail Price (Per Pound)', y_label='Vegetable Category',
                         title='Average Vegetable Prices by Vegetable Category', color=all_values)
    elif top_input == 'Top 7':
        df = vegetable_prices.groupby('Vegetable Category')[['RetailPrice']].mean().reset_index().sort_values(
            by='RetailPrice', ascending=False)[:7]
        df = df.sort_values(by='RetailPrice')
        return bar_chart(data=df, x_column='RetailPrice', y_column='Vegetable Category',
                         x_label='Retail Price (Per Pound)', y_label='Vegetable Category',
                         title='Average Vegetable Prices by Vegetable Category', color=top)
    elif top_input == 'Least 7':
        df = vegetable_prices.groupby('Vegetable Category')[['RetailPrice']].mean().reset_index().sort_values(
            by='RetailPrice')[:7]
        df = df.sort_values(by='RetailPrice', ascending=False)
        return bar_chart(data=df, x_column='RetailPrice', y_column='Vegetable Category',
                         x_label='Retail Price (Per Pound)', y_label='Vegetable Category',
                         title='Average Vegetable Prices by Vegetable Category', color=least)


# Callback for Fruits Graph 2
@callback(
    Output(component_id='v-graph-2', component_property='figure'),
    [
        Input(component_id='v-category-input', component_property='value'),
        Input(component_id='v-top-input', component_property='value')
    ]
)
def fruits_prices(category_input, top_input):
    if category_input:
        df = vegetable_prices[vegetable_prices['Vegetable Category'] == category_input].sort_values(by='RetailPrice')
        # Pivot the DataFrame
        df_pivoted = df.pivot_table(index='Vegetable', columns='Form', values='RetailPrice', fill_value=0)

        the_list = df['Form'].unique()

        # Reset the index to move 'Fruit' back to a column
        df_pivoted = df_pivoted.reset_index()

        # data, x_column, currency, z_column, x_label, y_label, title, formatting=1

        return stacked_bar_chart(data=df_pivoted, x_column='Vegetable', currency='$',
                                 z_column=the_list, x_label='Retail Price (Per Pound)', y_label='',
                                 title='Average Vegetable Prices' + ' ' + category_input + ' Categories')


# Callback for Fruits Graph 3
@callback(
    Output(component_id='v-graph-3', component_property='figure'),
    [
        Input(component_id='v-category-input', component_property='value'),
        Input(component_id='v-top-input', component_property='value')
    ]
)
def fruits_yield(category_input, top_input):
    if category_input:
        df = vegetable_prices[vegetable_prices['Vegetable Category'] == category_input].sort_values(by='Yield')
        # Pivot the DataFrame
        df_pivoted = df.pivot_table(index='Vegetable', columns='Form', values='Yield', fill_value=0)

        the_list = df['Form'].unique()

        # Reset the index to move 'Fruit' back to a column
        df_pivoted = df_pivoted.reset_index()

        # data, x_column, currency, z_column, x_label, y_label, title, formatting=1

        return grouped_bar_chart(data=df_pivoted, x_column='Vegetable', currency='%', z_column=the_list,
                                 x_label='Preparation Yield (%)', y_label='',
                                 title='Percentage Vegetable Yield' + ' ' + category_input + ' Categories',
                                 formatting=100)


