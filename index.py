#!/usr/bin/python3
import flask
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

from de_dash import page_content, utils
from de_dash.app import app


# App layout
app.layout = html.Div([

    # Header
    html.Div([
        html.Div([
            html.Img(src="data:image/png;base64,{}".format(utils.DE_LOGO.decode()), height="100%"),
        ], style=dict(float="left", height="100%")),

        html.Div([
            html.A(html.Button("View on GitHub",  style=dict(width="100%", height="40px",
                    color="#ffffff", backgroundColor=utils.COLORS["header"], marginTop="15px")), 
                href="https://github.com/deepexpressions/dashboard/", 
                target="_blank")

        ], style=dict(float="right", height="100%")),    
    ], id="header", className="header"),

    # Page content
    html.Div(id="page_content", style=utils.BG_STYLE),
    
    # Fonts
    html.Link(href="https://fonts.googleapis.com/css?family=Dosis", rel="stylesheet"),
    html.Link(href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet"),
    html.Link(href="https://fonts.googleapis.com/css?family=Open+Sans", rel="stylesheet"),
])


@app.callback(Output("page_content", "children"), [
    Input("page_content", "id")])
def route_to_content(_):
    """Route to page layout based on app_route."""
    return page_content.image_layout


# Running the server
if __name__ == "__main__":
    app.run_server(debug=True, port=8050, host="0.0.0.0")