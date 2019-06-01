import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

from de_dash import utils
from de_dash.app import app


layout = [

    html.Div([

        html.Div([
            dcc.Dropdown(
                id="model_dropdown", 
                placeholder="FER Model",
                options=[dict(label="xception-512-256", value="xception-512-256"),]
            ),

        ], className="five columns", style=utils.SEC_STYLE),
    
        # Image display
        html.Div([
            html.Div([
                dcc.Graph(id="interactive-image", style=dict(height="70%")),
            ]),

            html.Button("DOWNLOAD IMAGE", type="submit", style=dict(width="100%", 
                marginTop="5px", color="#ffffff", backgroundColor=utils.COLORS["header"])),

        ], className="six columns", style=dict(float="right"),),

    ], style=dict(margin="10px")),

]