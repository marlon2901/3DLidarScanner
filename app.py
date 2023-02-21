from dash import Dash, dcc, html, Input, Output
from dash.exceptions import PreventUpdate
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)
#df = pd.read_csv("https://raw.githubusercontent.com/marlon2901/3DLidarScanner/main/LMSM360_9.csv")
def layout_function():
    
    return html.Div([
        html.H1("Lidar Scanner", style = {'text-align': 'center'}),
        html.Button("Update Graph", id = "UpdateGraph", n_clicks = 0,
                    style = {'width':'100%','display':'flex',
                             'align-items':'center',
                             'justify-content':'center'}),
        html.Br(),
        dcc.Graph(id ='Scatter', figure = {})
        ])

app.layout = layout_function

@app.callback(
    Output(component_id = 'Scatter'    , component_property = 'figure'),
    Input (component_id = 'UpdateGraph', component_property = 'n_clicks')
)
def update_graph(n_clicks):
    
    df = pd.read_csv("LMSM360_9.csv")
    rangeLoop = int(df.size/3)
    print(df.size)
    size1 = []
    for i in range (rangeLoop):
        size1.append(0.000001)

    fig = px.scatter_3d(df, 
    x='X', y='Y', z='Z',
    color='X', size = size1)
    #   fig.write_html("3DLidarScannerPlotlyDash.html")
    return fig

app.run_server(debug=True)
