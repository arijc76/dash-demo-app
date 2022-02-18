import dash
import dash_html_components as html
from dash.dependencies import Output, Input
import altair as alt
from vega_datasets import data
import dash_core_components as dcc
import numpy as np

# Read in global data
gap = data.gapminder()

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1('Changes in life expectancy versus fertility'),
    html.Iframe(
        id='scatter',
        style={'border-width': '0px', 'width':'100%', 'height':'500px'}
        ),
    dcc.Dropdown(id = 'year_input', 
                value = 1970,
                options=[{'label': year, 'value': year}
                        for year in np.unique(gap['year']) ])
])

# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('year_input', 'value'))
def plot_chart(year):
    scatter_pop_lifeexp = alt.Chart(gap[gap['year'] == year]).mark_circle().encode(
        x=alt.X('fertility', title='Fertility'),
        y=alt.Y('life_expect', title='Life Expectancy'),
        color='pop',
        size='pop')
    return scatter_pop_lifeexp.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)
