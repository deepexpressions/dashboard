import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

from .. import utils
from ..app import app
from PIL.ImageColor import colormap


hyperparameters = [
    html.Div(dcc.Markdown("**__HYPERPARAMETERS:__**"), style=dict(color="#000000")),
    
    html.Div([
        dcc.Dropdown(
            id="model_dropdown", 
            placeholder="FER Model",
            clearable=False,
            options=[dict(label="vggface_ce", value="vggface_ce"),]
        ),

        html.Div([
            html.Div([
                dcc.Markdown("FD confidence:"),
            ], className="three columns", style=dict(color="#000000")),

            html.Div([               
                dcc.Slider(
                    id="fd_threshold_slider",
                    min=10, max=90,
                    step=5, value=50,
                    updatemode="drag",
                    marks={i: dict(label=f'{i}%', style=dict(
                        color="#000000")) for i in range(10, 91, 10)},
                ),
            ], className="nine columns"),

        ], className="row", style=dict(marginTop="10px", marginBottom="10px")),
    ]),#, style=dict(marginTop="-10px")) 
]


colors = [
    html.Div(dcc.Markdown("**__BOUNDING BOXES COLORS:__**"), style=dict(color="#000000")),

    html.Div([
        html.Div([
            html.Div([
                dcc.Markdown("* Anger:"),
            ], className="two columns", style=dict(color="#000000", fontSize=12, **{'vertical-align': 'middle'})),

            html.Div([
                html.Div(id="anger_color_bar", className="one columns"),

                dcc.Dropdown(
                    id="anger_color_drop", 
                    clearable=False,
                    value="red",
                    options = [dict(label=c, value=c) for c in colormap],
                    style=utils.COLOR_DROP_STYLE
                ),

            ], className="four columns", style=utils.COLOR_DROP_STYLE_DIV),

            html.Div([
                dcc.Markdown("* Disgust:"),
            ], className="two columns", style=dict(color="#000000", fontSize=12, marginLeft="15px")),

            html.Div([
                html.Div(id="disgust_color_bar", className="one columns"),

                dcc.Dropdown(
                    id="disgust_color_drop", 
                    clearable=False,
                    value="goldenrod",
                    options = [dict(label=c, value=c) for c in colormap],
                    style=utils.COLOR_DROP_STYLE
                ),
            ], className="four columns", style=utils.COLOR_DROP_STYLE_DIV),
        ], className="row"),

        html.Div([
            html.Div([
                dcc.Markdown("* Fear:"),
            ], className="two columns", style=dict(color="#000000", fontSize=12)),

            html.Div([
                html.Div(id="fear_color_bar", className="one columns"),
                
                dcc.Dropdown(
                    id="fear_color_drop", 
                    clearable=False,
                    value="mediumpurple",
                    options = [dict(label=c, value=c) for c in colormap],
                    style=utils.COLOR_DROP_STYLE
                ),
            ], className="four columns", style=utils.COLOR_DROP_STYLE_DIV),

            html.Div([
                dcc.Markdown("* Happiness:"),
            ], className="two columns", style=dict(color="#000000", fontSize=12, marginLeft="15px")),

            html.Div([
                html.Div(id="happiness_color_bar", className="one columns"),
                
                dcc.Dropdown(
                    id="happiness_color_drop", 
                    clearable=False,
                    value="yellow",
                    options = [dict(label=c, value=c) for c in colormap],
                    style=utils.COLOR_DROP_STYLE
                ),
            ], className="four columns", style=utils.COLOR_DROP_STYLE_DIV),
        ], className="row", style=dict(marginTop="10px")),

        html.Div([               
            html.Div([
                dcc.Markdown("* Neutral:"),
            ], className="two columns", style=dict(color="#000000", fontSize=12)),

            html.Div([
                html.Div(id="neutral_color_bar", className="one columns"),
                
                dcc.Dropdown(
                    id="neutral_color_drop", 
                    clearable=False,
                    value="darkgrey",
                    options = [dict(label=c, value=c) for c in colormap],
                    style=utils.COLOR_DROP_STYLE
                ),
            ], className="four columns", style=utils.COLOR_DROP_STYLE_DIV),

            html.Div([               
                dcc.Markdown("* Sadness:"),
            ], className="two columns", style=dict(color="#000000", fontSize=12, marginLeft="15px")),

            html.Div([
                html.Div(id="sadness_color_bar", className="one columns"),
                
                dcc.Dropdown(
                    id="sadness_color_drop", 
                    clearable=False,
                    value="royalblue",
                    options = [dict(label=c, value=c) for c in colormap],
                    style=utils.COLOR_DROP_STYLE
                ),
            ], className="four columns", style=utils.COLOR_DROP_STYLE_DIV),
        ], className="row", style=dict(marginTop="10px")),

        html.Div([
            html.Div([
                dcc.Markdown("* Surprise:"),
            ], className="two columns", style=dict(color="#000000", fontSize=12)),

            html.Div([
                html.Div(id="surprise_color_bar", className="one columns"),
                
                dcc.Dropdown(
                    id="surprise_color_drop", 
                    clearable=False,
                    value="limegreen",
                    options = [dict(label=c, value=c) for c in colormap],
                    style=utils.COLOR_DROP_STYLE
                ),
            ], className="four columns", style=utils.COLOR_DROP_STYLE_DIV),
        ], className="row", style=dict(marginTop="10px")),
    ]),#, style=dict(marginTop="-10px")) 
]


upload = [
    html.Div([

        html.Div([
            dcc.Input(id="input_url", type="text", placeholder="Image URL", style=utils.INPUT_STYLE),
        ], className="four columns"),

        html.Div([
            html.Div([

                html.Div([
                    dcc.Upload(html.Button("SUBMIT", type="submit", style=utils.BUTTON_STYLE), id="submit_url"),
                ], className="four columns"),

                html.Div([
                    dcc.Upload(html.Button("BROWSE", type="submit", style=utils.BUTTON_STYLE), id="upload_image"),
                ], className="four columns"),

                html.Div([
                    html.Button("DOWNLOAD", id="download_image", type="submit", style=utils.DOWNLOAD_BUTTON_STYLE),
                ], className="four columns"),

            ], className="row", style=dict(marginLeft="10px")),
        ], className="eight columns"),

    ], className="row", style=dict(marginLeft="2.5%"))
]


@app.callback(Output("anger_color_bar", "style"), [
    Input("anger_color_drop", "value")])
def update_anger_color_bar(c):
    return dict(height="2px", width="100%", backgroundColor=colormap[c]) 


@app.callback(Output("disgust_color_bar", "style"), [
    Input("disgust_color_drop", "value")])
def update_disgust_color_bar(c):
    return dict(height="2px", width="100%", backgroundColor=colormap[c]) 


@app.callback(Output("fear_color_bar", "style"), [
    Input("fear_color_drop", "value")])
def update_fear_color_bar(c):
    return dict(height="2px", width="100%", backgroundColor=colormap[c]) 


@app.callback(Output("happiness_color_bar", "style"), [
    Input("happiness_color_drop", "value")])
def update_happiness_color_bar(c):
    return dict(height="2px", width="100%", backgroundColor=colormap[c]) 


@app.callback(Output("neutral_color_bar", "style"), [
    Input("neutral_color_drop", "value")])
def update_neutral_color_bar(c):
    return dict(height="2px", width="100%", backgroundColor=colormap[c]) 


@app.callback(Output("sadness_color_bar", "style"), [
    Input("sadness_color_drop", "value")])
def update_sadness_color_bar(c):
    return dict(height="2px", width="100%", backgroundColor=colormap[c]) 


@app.callback(Output("surprise_color_bar", "style"), [
    Input("surprise_color_drop", "value")])
def update_surprise_color_bar(c):
    return dict(height="2px", width="100%", backgroundColor=colormap[c]) 