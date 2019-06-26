import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

import base64
from matplotlib import pyplot as plt

from .. import utils
from .. import graphs
from ..app import app
from . import sections
from .. import dash_reusable_components as drc


layout = [

    html.Div([
      
        # Hiperparameters and colors settings
        html.Div([
            html.Div(sections.hyperparameters, style=utils.SEC_STYLE),
            html.Div(style=dict(height="7px")),
            html.Div(sections.colors, style=utils.SEC_STYLE),
            html.Div(style=dict(height="7px")),
            html.Div(sections.upload, style=dict(margin=5)),

        ], className="six columns"),
    
        # Image display
        html.Div([
            dcc.Graph(figure=graphs.fig, id="image", style=dict(height="100vh", width="100%", marginTop="5px"))
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
    Input("upload_image", "contents")])
def show_image(im):
    # im = drc.b64_to_pil(im)
    # plt.imshow(im)
    # plt.show()
    return None
