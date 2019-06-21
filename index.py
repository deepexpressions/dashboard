#!/usr/bin/python3
import flask
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

from de_dash import utils
from de_dash.app import app
from de_dash.pages import home, images_page, videos_page


# App layout
app.layout = html.Div([

    # Header
    html.Div([
        html.Div([
            html.Img(src="data:image/png;base64,{}".format(utils.DE_LOGO.decode()), height="100%"),
        ], style=dict(float="left", height="100%")),

        html.Div([
            html.Form([
                html.Button("HOME", type="submit", style=dict(width="100%", height="40px",
                    color="#ffffff", backgroundColor=utils.COLORS["header"], marginTop="15px")),
            ], action="/home", method="post"),
        ], style=dict(float="right"))
    
    ], id="header", className="header"),

    # Page content
    html.Div(home.layout, id="page_content", style=utils.BG_STYLE),
    
    # Fonts
    html.Link(href="https://fonts.googleapis.com/css?family=Dosis", rel="stylesheet"),
    html.Link(href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet"),
    html.Link(href="https://fonts.googleapis.com/css?family=Open+Sans", rel="stylesheet"),
])


@app.server.route("/home", methods=["POST"])
def route_to_home():
    """Redirect page to "/images."""
    rep = flask.redirect("/home")
    rep.set_cookie("app_route", "/home")
    return rep


@app.server.route("/images", methods=["POST"])
def route_to_images():
    """Redirect page to "/images."""
    rep = flask.redirect("/images")
    rep.set_cookie("app_route", "/images")
    return rep


@app.server.route("/videos", methods=["POST"])
def route_to_videos():
    """Redirect page to "/videos."""
    rep = flask.redirect("/videos")
    rep.set_cookie("app_route", "/videos")
    return rep


@app.callback(Output("page_content", "children"), [
    Input("page_content", "id")])
def route_to_content(_):
    """Route to page layout based on app_route."""
    session_cookie = flask.request.cookies.get("app_route")

    if session_cookie == "/home":
        return home.layout
        
    elif session_cookie == "/images":
        return images_page.layout

    elif session_cookie == "/videos":
        return videos_page.layout

    else:
        return home.layout


# Running the server
if __name__ == "__main__":
    app.run_server(debug=True, port=8050, host="0.0.0.0")