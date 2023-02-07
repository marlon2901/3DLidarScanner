from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)
server = app.server

# Import data
df = pd.read_csv("LMSM360_9.csv")

app.layout = html.Div([
    html.H1("Lidar Scanner", style = {'text-align': 'center'}),
    dcc.Dropdown(id = "Vertical_Increment",
        options = [
            {"label": "1.8", "value": 1.8},
            {"label": "9"  , "value": 9  },
            {"label": "18" , "value": 18 },
            {"label": "27" , "value": 27 }],
        value = 1.8),
    html.Div(id ='Output_box', children =[]),
    html.Br(),
    dcc.Graph(id ='Scatter', figure = {})])

@app.callback(
    [Output(component_id = 'Output_box'        , component_property = 'children'),
     Output(component_id = 'Scatter'           , component_property = 'figure')],
    [Input (component_id = 'Vertical_Increment', component_property = 'value')]
)
def update_graph(option_degree):
    
    container = "The vertical increment chosen was: {}".format(option_degree)
    size1 = []
    for i in range (2433):
        size1.append(0.000001)
    fig = px.scatter_3d(df, 
        x='X', y='Y', z='Z',
        color="X", size = size1)
    fig.write_html("3DLidarScannerPlotlyDash.html")
    return container, fig

app.run_server(debug=False)
