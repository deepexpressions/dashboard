#!/usr/bin/python3
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

from de_dash.app import app
from de_dash import page_content, utils


# App layout
app.layout = html.Div([

    # Header
    html.Div([
        html.Div([
            html.Img(src="data:image/png;base64,{}".format(utils.DE_LOGO.decode()), height="100%"),
        ], style=dict(float="left", height="100%")),

        html.Div([
            html.A(html.Button("View on GitHub", style=utils.GITHUB_BUTTON_STYLE), 
                href="https://github.com/deepexpressions/dashboard/", 
                target="_blank")
        ], style=dict(float="right", height="100%")),   

    ], className="header"),

    # Page content
    html.Div(page_content.layout, style=utils.BG_STYLE),
    
    # Fonts
    html.Link(href="https://fonts.googleapis.com/css?family=Dosis", rel="stylesheet"),
    html.Link(href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet"),
    html.Link(href="https://fonts.googleapis.com/css?family=Open+Sans", rel="stylesheet"),
])


# Running the server
if __name__ == "__main__":
    app.run_server(debug=True, port=8050, host="0.0.0.0")