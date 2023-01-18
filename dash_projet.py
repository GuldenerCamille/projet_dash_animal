import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import dash
from dash import html, dcc
from dash.dash_table import DataTable
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv("steam.csv")
df['release_date'] = pd.to_datetime(df['release_date'])
date_chose = 2017

df_date = df[df['release_date'].dt.year== date_chose]

df_date = df_date.sort_values(['owners', 'median_playtime'],
              ascending = [False, False]).head(10)
df_date_full = df_date.sort_values(['owners', 'median_playtime'],
              ascending = [False, False])

game_year =px.histogram(df, x=df["release_date"].dt.year)
game_year.update_layout(
    title_text='Game per year', # title of plot
    xaxis_title_text='Year', # xaxis label
    yaxis_title_text='Count', # yaxis label
    bargap=0.2, # gap between bars of adjacent location coordinates
    bargroupgap=0.1, # gap between bars of the same location coordinates

)


@app.callback(
        Output('tableau', 'figure'),
        Output('cercle','figure'),
        Input('dropdown', 'value')
    )
def update_output(value):
    filtered_df = df[df['release_date'].dt.year== value]
    filtered_df = filtered_df.sort_values(['owners', 'median_playtime'],
              ascending = [False, False])
    filtered_df_8 = filtered_df.head(8)
    cercle = px.pie(filtered_df, values="required_age", names="required_age", title="Age requis pour jouer par année")

    tablo = go.Figure(data=[go.Table(
    header=dict(values=["Name","Editeur","Prix"],
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[filtered_df_8.name,filtered_df_8.developer,
                       filtered_df_8.price],
               fill_color='lavender',
               align='left'))
])
    return tablo,cercle

row_summary_metrics = dbc.Row(
    [
        dbc.Col("", width=1),

        dbc.Col(dcc.Graph(figure=game_year), width=12),
        dbc.Col("", width=1),
    ],
)
row_2 = dbc.Row(
    [
        dbc.Col("", width=0.5),
        dbc.Col(dcc.Graph(id="cercle") ,width=4),
        dbc.Col(dcc.Graph(id="tableau"), width=8),
        dbc.Col("", width=0.5),
    ],
)
app.layout = html.Div(
    [

        html.H1("STEAM Camille , Kamel , Morgan"),
        html.H2("STEAM Dataset"),
        html.Label('Listes des dates'),
        dcc.Dropdown(df.release_date.sort_values().dt.year.unique(),id="dropdown",value=2015),

        html.Br(),
        row_2,
        row_summary_metrics

    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
