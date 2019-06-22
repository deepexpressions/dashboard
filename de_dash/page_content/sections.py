import dash_core_components as dcc
import dash_html_components as html
from PIL.ImageColor import colormap

from .. import utils


hyperparameters = [
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
                    step=5, value=50,
                    updatemode="drag",
                    marks={i: dict(label=f'{i}%', style=dict(
                        color="#ffffff")) for i in range(10, 91, 10)},
                ),
            ], className="nine columns"),

        ], className="row", style=dict(marginTop="10px", marginBottom="10px")),
    ], style=dict(marginTop="-10px")) 
]


colors = [
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
                    value="red",
                    options = [dict(label=c, value=c, style=dict(backgroundColor=colormap[c])) for c in colormap]
                ),
            ], className="four columns", style=utils.COLOR_DROP_STYLE),

            html.Div([
                dcc.Markdown("* **Disgust:**"),
            ], className="two columns", style=dict(color="#ffffff", fontSize=12, marginLeft="15px")),

            html.Div([
                dcc.Dropdown(
                    id="disgust_color", 
                    clearable=False,
                    value="goldenrod",
                    options = [dict(label=c, value=c, style=dict(backgroundColor=colormap[c])) for c in colormap]
                ),
            ], className="four columns", style=utils.COLOR_DROP_STYLE),
        ], className="row"),

        html.Div([
            html.Div([
                dcc.Markdown("* **Fear:**"),
            ], className="two columns", style=dict(color="#ffffff", fontSize=12)),

            html.Div([
                dcc.Dropdown(
                    id="fear_color", 
                    clearable=False,
                    value="mediumpurple",
                    options = [dict(label=c, value=c, style=dict(backgroundColor=colormap[c])) for c in colormap]
                ),
            ], className="four columns", style=utils.COLOR_DROP_STYLE),

            html.Div([
                dcc.Markdown("* **Happiness:**"),
            ], className="two columns", style=dict(color="#ffffff", fontSize=12, marginLeft="15px")),

            html.Div([
                dcc.Dropdown(
                    id="happiness_color", 
                    clearable=False,
                    value="yellow",
                    options = [dict(label=c, value=c, style=dict(backgroundColor=colormap[c])) for c in colormap]
                ),
            ], className="four columns", style=utils.COLOR_DROP_STYLE),
        ], className="row", style=dict(marginTop="10px")),

        html.Div([
            html.Div([
                dcc.Markdown("* **Neutral:**"),
            ], className="two columns", style=dict(color="#ffffff", fontSize=12)),

            html.Div([
                dcc.Dropdown(
                    id="neutral_color", 
                    clearable=False,
                    value="darkgrey",
                    options = [dict(label=c, value=c, style=dict(backgroundColor=colormap[c])) for c in colormap]
                ),
            ], className="four columns", style=utils.COLOR_DROP_STYLE),

            html.Div([
                dcc.Markdown("* **Sadness:**"),
            ], className="two columns", style=dict(color="#ffffff", fontSize=12, marginLeft="15px")),

            html.Div([
                dcc.Dropdown(
                    id="sadness_color", 
                    clearable=False,
                    value="dodgerblue",
                    options = [dict(label=c, value=c, style=dict(backgroundColor=colormap[c])) for c in colormap]
                ),
            ], className="four columns", style=utils.COLOR_DROP_STYLE),
        ], className="row", style=dict(marginTop="10px")),

        html.Div([
            html.Div([
                dcc.Markdown("* **Surprise:**"),
            ], className="two columns", style=dict(color="#ffffff", fontSize=12)),

            html.Div([
                dcc.Dropdown(
                    id="surprise_color", 
                    clearable=False,
                    value="limegreen",
                    options = [dict(label=c, value=c, style=dict(backgroundColor=colormap[c])) for c in colormap]
                ),
            ], className="four columns", style=utils.COLOR_DROP_STYLE),
        ], className="row", style=dict(marginTop="10px")),
    ], style=dict(marginTop="-10px")), 
]