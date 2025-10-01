# importing packages
import pandas as pd
from dash import Dash, dcc, html, dash_table, Output, Input
import plotly.express as px

colors = {
    'black': '#111111',
    'beige': '#9A6242'
}

# incororate data
df = pd.read_csv("data/finaloutput.csv")

# initiliasing the app
app = Dash()

# app layout
app.layout = html.Div(style={'backgroundColor': colors['black']}, children=[

    html.H1(children='Pink Morsel',
            style={
                'padding-top': '15px',
                'padding-left': '20px',
                'textAlign': 'left',
                'font-family': ['Georgia'],
                'color' : ['#9A6242']
            }),
    
    html.Div(children='''
             Sales over time.
             ''',
             style={
                'textAlign': 'center',
                
                'font-family': ['Arial'],
                'color' : ['#9A6242']
             }),

    html.Div(
        dcc.RadioItems(['west','south','north','east','all'], 'all',
                       id='region_selector',
                       inline=True,
                       style={'textAlign': 'center',
                       'padding-top': '20px',
                              'color': ['#9A6242'],
                              'font-family': ['Arial']}
                       
                       )

    ),


    dcc.Graph(id = "px-line")
    
])
 
@app.callback(Output(component_id='px-line', component_property='figure'),
              [Input(component_id='region_selector', component_property='value')])

def update_output_div(contintent):

    if contintent == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == contintent]

    fig = px.line(filtered_df, x='date', y='Sales',
                color='region', 
                color_discrete_sequence=['#9A6242'],
                labels={'date': 'Dates', 'Sales': 'Sales'})

    fig.update_layout(
        plot_bgcolor=colors['black'],
        paper_bgcolor=colors['black'],
        font_color=colors['beige']

    )

    return fig
    

# run the app
if __name__ == '__main__':
    app.run(debug=True)