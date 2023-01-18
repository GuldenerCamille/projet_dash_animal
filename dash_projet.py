
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_csv("Health_AnimalBites.csv")

fig1 = px.histogram(df, x="SpeciesIDDesc")





app.layout = html.Div(children=[
    html.H2(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig1



    )
,
html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig1



    )


])

if __name__ == '__main__':
    app.run_server(debug=True)
