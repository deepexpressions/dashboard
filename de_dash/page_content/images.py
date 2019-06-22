import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

from PIL import Image
from plotly import graph_objs as go

from de_dash import utils
from de_dash.app import app
from .. import dash_reusable_components as drc


layout = [

    html.Div([

        html.Div([
            html.Div([
                html.Div(dcc.Markdown("**HYPERPARAMETERS:**\n\n---"), style=dict(color="#ffffff")),
                
                html.Div([
                    dcc.Dropdown(
                        id="model_dropdown", 
                        placeholder="FER Model",
                        clearable=False,
                        options=[dict(label="vggface_ce", value="vggface_ce"),]
                    ),

                    html.Div([
                        html.Div([
                            dcc.Markdown("**FD confidence:**"),
                        ], className="three columns", style=dict(color="#ffffff")),

                        html.Div([               
                            dcc.Slider(
                                id="fd_threshold_slider",
                                min=10, max=90,
                                step=0.1, value=0.5,
                                updatemode="drag",
                                marks={i: dict(label=f'{i}%', style=dict(
                                    color="#ffffff")) for i in range(10, 91, 10)},
                            ),
                        ], className="nine columns"),

                    ], className="row", style=dict(marginTop="10px", marginBottom="10px")),
                ], style=dict(marginTop="-10px")) 
            ], style=utils.SEC_STYLE),

            html.Div(style=dict(height="5px")),

            html.Div([
                html.Div(dcc.Markdown("**BOUNDING BOXES COLORS:**\n\n---"), style=dict(color="#ffffff")),

                html.Div([
                    html.Div([
                        html.Div([
                            dcc.Markdown("* **Anger:**"),
                        ], className="two columns", style=dict(color="#ffffff", fontSize=12)),

                        html.Div([
                            dcc.Dropdown(
                                id="anger_color", 
                                clearable=False,
                                value="Red",
                                options=[dict(label=c, value=c) for c in utils.STANDARD_COLORS]
                            ),
                        ], className="four columns", style=dict(marginLeft="-10px", fontSize=12)),

                        html.Div([
                            dcc.Markdown("* **Disgust:**"),
                        ], className="two columns", style=dict(color="#ffffff", fontSize=12, marginLeft="15px")),

                        html.Div([
                            dcc.Dropdown(
                                id="disgust_color", 
                                clearable=False,
                                value="Gold",
                                options=[dict(label=c, value=c) for c in utils.STANDARD_COLORS]
                            ),
                        ], className="four columns", style=dict(marginLeft="-10px", fontSize=12)),
                    ], className="row"),

                    html.Div([
                        html.Div([
                            dcc.Markdown("* **Fear:**"),
                        ], className="two columns", style=dict(color="#ffffff", fontSize=12)),

                        html.Div([
                            dcc.Dropdown(
                                id="fear_color", 
                                clearable=False,
                                value="LightYellow",
                                options=[dict(label=c, value=c) for c in utils.STANDARD_COLORS]
                            ),
                        ], className="four columns", style=dict(marginLeft="-10px", fontSize=12)),

                        html.Div([
                            dcc.Markdown("* **Happiness:**"),
                        ], className="two columns", style=dict(color="#ffffff", fontSize=12, marginLeft="15px")),

                        html.Div([
                            dcc.Dropdown(
                                id="happiness_color", 
                                clearable=False,
                                value="HotPink",
                                options=[dict(label=c, value=c) for c in utils.STANDARD_COLORS]
                            ),
                        ], className="four columns", style=dict(marginLeft="-10px", fontSize=12)),
                    ], className="row", style=dict(marginTop="10px")),

                    html.Div([
                        html.Div([
                            dcc.Markdown("* **Neutral:**"),
                        ], className="two columns", style=dict(color="#ffffff", fontSize=12)),

                        html.Div([
                            dcc.Dropdown(
                                id="neutral_color", 
                                clearable=False,
                                value="DarkGrey",
                                options=[dict(label=c, value=c) for c in utils.STANDARD_COLORS]
                            ),
                        ], className="four columns", style=dict(marginLeft="-10px", fontSize=12)),

                        html.Div([
                            dcc.Markdown("* **Sadness:**"),
                        ], className="two columns", style=dict(color="#ffffff", fontSize=12, marginLeft="15px")),

                        html.Div([
                            dcc.Dropdown(
                                id="sadness_color", 
                                clearable=False,
                                value="DodgerBlue",
                                options=[dict(label=c, value=c) for c in utils.STANDARD_COLORS]
                            ),
                        ], className="four columns", style=dict(marginLeft="-10px", fontSize=12)),
                    ], className="row", style=dict(marginTop="10px")),

                    html.Div([
                        html.Div([
                            dcc.Markdown("* **Surprise:**"),
                        ], className="two columns", style=dict(color="#ffffff", fontSize=12)),

                        html.Div([
                            dcc.Dropdown(
                                id="surprise_color", 
                                clearable=False,
                                value="LimeGreen",
                                options=[dict(label=c, value=c) for c in utils.STANDARD_COLORS]
                            ),
                        ], className="four columns", style=dict(marginLeft="-10px", fontSize=12)),
                    ], className="row", style=dict(marginTop="10px")),
                ], style=dict(marginTop="-10px")), 
            ], style=utils.SEC_STYLE),

        ], className="six columns"),
    
        # Image display
        html.Div([
            html.Div([
                dcc.Graph(id="image", style=dict(height="70%")),
            ]),

            html.Button("UPLOAD IMAGE", type="submit", style=utils.BUTTON_STYLE),
            html.Button("DOWNLOAD IMAGE", type="submit", style=utils.BUTTON_STYLE),

        ], className="six columns", style=dict(float="right"),),

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
