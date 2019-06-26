import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State

from .app import app
from . import  utils
from . import  graphs
from . import  menu_sections
from . import  dash_reusable_components as drc

from time import sleep


layout = [

    html.Div([
      
        # Hiperparameters and colors settings
        html.Div([
            html.Div(menu_sections.hyperparameters, style=utils.SEC_STYLE),
            # html.Div(style=dict(height="1%")),
            html.Div(menu_sections.colors, style=utils.SEC_STYLE),
            # html.Div(style=dict(height="1%")),
            html.Div(menu_sections.upload, style=dict(margin=5)),
        ], className="six columns"),
    
        # Image display
        html.Div([
            dcc.Graph(figure=graphs.DEFAULT_FIGURE, id="image", style=dict(width="100%", marginTop="5px"))
        ], id="image_div", className="six columns", style=dict(height="100vh", float="right")),

        # html.Div(id="reset", style=dict(display="none")),

    ], style=dict(margin="10px")),
]


@app.callback(Output("image", "figure"), [
    Input("model_dropdown", "value"),
    Input("fd_threshold_slider", "value"),
    Input("anger_color_drop", "value"),
    Input("disgust_color_drop", "value"),
    Input("fear_color_drop", "value"),
    Input("happiness_color_drop", "value"),
    Input("neutral_color_drop", "value"),
    Input("sadness_color_drop", "value"),
    Input("surprise_color_drop", "value"),
    Input("submit_url", "n_clicks"),
    Input("upload_image", "n_clicks")], [
    State("input_url", "value"),
    State("image", "figure")])
def update_and_apply_image(model_name, threshold, c_an, c_di, c_fe, c_ha, 
                           c_ne, c_sa, c_su, bt_submit, bt_upload, url, fig):
    """Upload and return image."""

    print(bt_submit, url)

    if url is not None and bt_submit == 1 :
        return graphs.submit_image_from_url(url)

    return fig


@app.callback(Output("submit_url", "n_clicks"), [
    Input("input_url", "value")], [
    State("submit_url", "n_clicks")])
def reset_input_components(_, bt_submit):
    return 0 if bt_submit > 0 else bt_submit