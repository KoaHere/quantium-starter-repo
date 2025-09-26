# importing packages
import pandas as pd
from dash import Dash, dcc, html, dash_table
import plotly.express as px


# incororate data
df = pd.read_csv("data/finaloutput.csv")

# initiliasing the app
app = Dash()

fig = px.line(df, x='date', y='Sales', labels={'date': 'Dates', 'Sales': 'Sales'})

# app layout
app.layout = html.Div(children=[
    html.H1(children='Pink Morsel',
            style={
                'textAlign': 'center',
                'font-family': ['Arial']
            }),

    html.Div(children='''
             Sales over time.
             ''',
             style={
                'textAlign': 'center',
                'font-family': ['Arial']
             }),


             dcc.Graph(
                 id='example_graph',
                 figure=fig
             )
    
])

# run the app
if __name__ == '__main__':
    app.run(debug=True)