import dash_core_components as dcc
import dash_html_components as html
from dash.exceptions import PreventUpdate
from dash.dependencies import Output, Input, State

from .app import app
from . import  utils
from . import  graphs
from . import  menu_sections
from . import  dash_reusable_components as drc


@app.server.route("/download_figure/<path:file>")
def download(file):
    print(file)
    return send_file(file, attachment_filename="image.png", as_attachment=True)
    

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
            dcc.Graph(figure=graphs.DEFAULT_FIGURE, id="image", style=dict(width="100%", marginTop="5px")),
            html.Div(graphs.DEFAULT_IMAGE, id="raw_image", style=dict(display="none")),
        ], id="image_div", className="six columns", style=dict(height="100vh", float="right")),

        # Confirm Dialogs
        html.Div([
            dcc.ConfirmDialog(id="im_failed", message="Failed to load the image."),
            dcc.Interval(id="reset", interval=1*1000, n_intervals=0),
        ]),

    ], style=dict(margin="10px")),
]


@app.callback([Output("image", "figure"),
    Output("raw_image", "children"),
    Output("im_failed", "displayed")], [
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
    Input("upload_image", "contents")], [
    State("input_url", "value"),
    State("im_failed", "displayed"), 
    State("image", "figure"),
    State("raw_image", "children")])
def update_and_apply_image(model_name, threshold, c_an, c_di, c_fe, c_ha, 
                           c_ne, c_sa, c_su, bt_submit, up_contents, url, 
                           im_failed, fig, raw_fig):

    # Bounding boxes colors
    colors = {k:v for k,v in enumerate([c_an, c_di, c_fe, 
        c_ha, c_ne, c_sa, c_su])}


    # Retrive image from url
    if url is not None and bt_submit == 1 :
        raw_fig2, fig2 = graphs.submit_image_from_url(url)
        if fig2 is None:
            return fig, raw_fig, True
        else:
            return fig2, drc.pil_to_b64(raw_fig2), False


    # Retrive image from upload
    elif up_contents is not None:
        raw_fig2, fig2 = graphs.submit_local_image(up_contents)
        if fig2 is None:
            return fig, raw_fig, True
        else:
            return fig2, drc.pil_to_b64(raw_fig2), False

    else:
        raise PreventUpdate


@app.callback(Output("download_image", "href"), [
    Input("raw_image", "children")])
def download_image(raw_fig):
    media_type = "images/png"
    href = f"data:{media_type};base64,{raw_fig}"
    return href


@app.callback(Output("submit_url", "n_clicks"), [
    Input("raw_image", "children")], [
    State("submit_url", "n_clicks")])
def reset_submit_button(_, bt_submit):
    if bt_submit > 0:
        return 0
    else:
        raise PreventUpdate


@app.callback(Output("upload_image", "contents"), [
    Input("raw_image", "children")], [
    State("upload_image", "contents")])
def reset_upload_content(_, up_contents):
    if up_contents is not None:
        return None
    else:
        raise PreventUpdate


@app.callback(Output("input_url", "value"), [
    Input("raw_image", "children")], [
    State("input_url", "value")])
def reset_input_value(_, image_url):
    if image_url is not None:
        return ''
    else:
        raise PreventUpdate