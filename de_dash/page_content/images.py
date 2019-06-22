import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input


from .. import utils
from ..app import app
from . import sections
from .. import dash_reusable_components as drc


layout = [

    html.Div([
        
        # Hiperparameters and colors settings
        html.Div([
            html.Div( sections.hyperparameters, style=utils.SEC_STYLE),
            html.Div(style=dict(height="7px")),
            html.Div(sections.colors, style=utils.SEC_STYLE),
        ], className="six columns"),
    
        # Image display
        html.Div([
            html.Div(dcc.Graph(id="image", style=dict(height="70%"))),
            html.Button("UPLOAD IMAGE", type="submit", style=utils.BUTTON_STYLE),
            html.Button("DOWNLOAD IMAGE", type="submit", style=utils.BUTTON_STYLE),
        ], className="six columns", style=dict(float="right"),),

        # Empty div
        html.Div(id="_trash")

    ], style=dict(margin="10px")),
]


@app.callback(Output("_trash", "children"), [
    Input("model_dropdown", "value"),
    Input("fd_threshold_slider", "value")])
def hold_status(a, b):
    return None


@app.callback(Output("image", "children"), [
    Input("model_dropdown", "value")])
def show_image(_):
    return None
