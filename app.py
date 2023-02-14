from dash import Dash, dcc, html, Input, Output
from dash.exceptions import PreventUpdate
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    dcc.Interval( id = 'my_interval',
                  disabled = False,
                  interval = 1 * 3000,
                  n_intervals = 0,
                  max_intervals = 4,
        ),
    
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
    dcc.Store(id = "store"),
    html.Div(id = "trigger"),
    dcc.Graph(id ='Scatter', figure = {})])

@app.callback(Output('store','data'), [Input('trigger','children')], prevent_initial_call=False)
def update_data(children):
    # Import data
    df = pd.read_csv("LMSM360_9.csv")
    return df.to_json()

@app.callback(
    [Output(component_id = 'Output_box'        , component_property = 'children'),
     Output(component_id = 'Scatter'           , component_property = 'figure')],
    [Input (component_id = 'Vertical_Increment', component_property = 'value')],
    [State (component_id = 'store'              , component_property = 'data')]
)
def update_graph(option_degree, data):
    
    container = "The vertical increment chosen was: {}".format(option_degree)
    rangeLoop = int(df.size/3)
    print(df.size)
    size1 = []
    for i in range (rangeLoop):
        size1.append(0.000001)
        
    if data is None:
        raise PreventUpdate
    else:
        df = pd.read_json(data)
        fig = px.scatter_3d(df, 
        x='X', y='Y', z='Z',
        color="X", size = size1)
    fig.write_html("3DLidarScannerPlotlyDash.html")
    return container, fig

app.run_server(debug=True)

