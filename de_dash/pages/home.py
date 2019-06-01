import dash_html_components as html
from de_dash.utils import COLORS


layout = [
    # Button for images page
    html.Div([
        html.Form([
            html.Button("IMAGES", type="submit", style=dict(width="20%", 
                color="#ffffff", backgroundColor=COLORS["header"])),
        ], action="/images", method="post"),
    ], className="row", style=dict(textAlign="center", marginTop="150px")), 

    # Button for videos page
    html.Div([
        html.Form([
            html.Button("VIDEOS", type="submit", style=dict(width="20%", 
                color="#ffffff", backgroundColor=COLORS["header"])),
        ], action="/videos", method="post"),
    ], className="row", style=dict(textAlign="center", marginTop="5px")), 
]