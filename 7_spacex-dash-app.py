# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                
                                # TÂCHE 1 : Ajouter un composant d’entrée déroulant (Dropdown)
                                dcc.Dropdown(
                                    id='site-dropdown',
                                    options=[
                                        {'label': 'All Sites', 'value': 'ALL'},
                                        {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                        {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                        {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                        {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
                                    ],
                                    value='ALL',
                                    placeholder="Select a Launch Site here",
                                    searchable=True
                                ),
                                html.Br(),

                                # TÂCHE 2 : Ajouter un graphique circulaire (Pie chart)
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                
                                # TÂCHE 3 : Ajouter un curseur de plage (Range Slider)
                                dcc.RangeSlider(
                                    id='payload-slider',
                                    min=0, 
                                    max=10000, 
                                    step=1000,
                                    marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
                                    value=[min_payload, max_payload]
                                ),

                                # TÂCHE 4 : Ajouter un graphique de dispersion (Scatter chart)
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TÂCHE 2 : Callback pour le graphique circulaire (Pie Chart)
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        # Si ALL, on utilise toutes les données pour montrer la contribution de chaque site au succès total
        fig = px.pie(spacex_df, values='class', 
                     names='Launch Site', 
                     title='Total Success Launches By Site')
        return fig
    else:
        # Si un site spécifique, on filtre et on montre Succès (1) vs Échec (0)
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        # On compte les occurrences de chaque classe (0 et 1)
        filtered_counts = filtered_df['class'].value_counts().reset_index()
        filtered_counts.columns = ['class', 'count']
        fig = px.pie(filtered_counts, 
                     values='count', 
                     names='class', 
                     title=f'Total Success Launches for site {entered_site}')
        return fig

# TÂCHE 4 : Callback pour le graphique de dispersion (Scatter Chart)
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'), 
               Input(component_id="payload-slider", component_property="value")])
def get_scatter_chart(entered_site, slider_range):
    # 1. On filtre d'abord les données en fonction du Slider (charge utile)
    low, high = slider_range
    mask = (spacex_df['Payload Mass (kg)'] > low) & (spacex_df['Payload Mass (kg)'] < high)
    range_df = spacex_df[mask]

    # 2. On vérifie ensuite le Dropdown (Site)
    if entered_site == 'ALL':
        # Affichage pour tous les sites
        fig = px.scatter(range_df, x='Payload Mass (kg)', y='class', 
                         color="Booster Version Category",
                         title='Correlation between Payload and Success for all Sites')
        return fig
    else:
        # Affichage pour un site spécifique
        site_df = range_df[range_df['Launch Site'] == entered_site]
        fig = px.scatter(site_df, x='Payload Mass (kg)', y='class', 
                         color="Booster Version Category",
                         title=f'Correlation between Payload and Success for site {entered_site}')
        return fig


if __name__ == '__main__':
    app.run()