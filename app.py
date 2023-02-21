from dash import Dash, dcc, html, Input, Output
from dash.exceptions import PreventUpdate
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)
#csvPath = "https://raw.githubusercontent.com/marlon2901/3DLidarScanner/main/LMSM360_9.csv"

def layout_function():
    
    global df
    df = pd.read_csv("LMSM360_9.csv")
    print (df)
    
    return html.Div([
        html.H1("Lidar Scanner", style = {'text-align': 'center'}),
        dcc.Dropdown(
            id = "Vertical_Increment",
            options = [
                {"label": "1.8", "value": 1.8},
                {"label": "9"  , "value": 9  },
                {"label": "18" , "value": 18 },
                {"label": "27" , "value": 27 }],
                value = 1.8),
        html.Div(id ='Output_box', children =[]),
        html.Br(),
        dcc.Graph(id ='Scatter', figure = {})
        ])

app.layout = layout_function

@app.callback(
    [Output(component_id = 'Output_box'        , component_property = 'children'),
     Output(component_id = 'Scatter'           , component_property = 'figure')],
    [Input (component_id = 'Vertical_Increment', component_property = 'value')]
)
def update_graph(option_degree):
    
    container = "The vertical increment chosen was: {}".format(option_degree)
    rangeLoop = int(df.size/3)
    print(df.size)
    size1 = []
    for i in range (rangeLoop):
        size1.append(0.000001)

    fig = px.scatter_3d(df, 
    x='X', y='Y', z='Z',
    color='X', size = size1)
    #   fig.write_html("3DLidarScannerPlotlyDash.html")
    return container, fig

app.run_server(debug=True)


