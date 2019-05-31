import dash_html_components as html


layout = [
    # Button for images page
    html.Div([
        html.Form([
            html.Button("IMAGES", type="submit", style=dict(width="20%", 
                color="#ffffff", backgroundColor="#2a3f5f")),
        ], action="/images", method="post"),
    ], className="row", style=dict(textAlign="center", marginTop="150px")), 

    # Button for videos page
    html.Div([
        html.Form([
            html.Button("VIDEOS", type="submit", style=dict(width="20%", 
                color="#ffffff", backgroundColor="#2a3f5f")),
        ], action="/videos", method="post"),
    ], className="row", style=dict(textAlign="center", marginTop="5px")), 
]