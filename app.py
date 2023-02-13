from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Import data
df = pd.read_csv("LMSM360_9.csv")

app.layout = html.Div([
    #Interval
    dcc.Interval(id = 'my_interval',
                 disabled = False,
                 interval = 1 * 4000,
                 n_intervals = 0,
                 max_intervals = 4,
    ),
    
    html.H1("Lidar Scanner", style = {'text-align': 'center'}),
    html.Br(),
    dcc.Graph(id ='Scatter', figure = {})])

@app.callback(
    [Output(component_id = 'Scatter'     , component_property = 'figure')],
    [Input (component_id = 'my_interval' , component_property = 'n_intervals')]
)
def update_graph(num):
    
    if num == 0:
        raise PreventUpdate
    else:
        size1 = []
        for i in range (988):
            size1.append(0.000001)
        fig = px.scatter_3d(df, 
            x='X', y='Y', z='Z',
            color="X", size = size1)
        fig.write_html("3DLidarScannerPlotlyDash.html")
    return fig

app.run_server(debug=True)
