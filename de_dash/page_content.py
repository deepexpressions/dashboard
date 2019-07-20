import DeepExpressions as de
import dash_core_components as dcc
import dash_html_components as html
from plotly import graph_objs as go
from dash.exceptions import PreventUpdate
from dash.dependencies import Output, Input, State

from .app import app
from . import  menu_sections
from . import  figure_graphs as fg
from . import  default_styles as stl
from . import  dash_reusable_components as drc



# OpenCV Face Detector
face_detector = de.face.Detector()
# Load default FER Model
fer_model = de.models.FERModel("vggface_ce")


@app.server.route("/download_figure/<path:file>")
def download(file):
    print(file)
    return send_file(file, attachment_filename="image.png", as_attachment=True)
    

layout = [

    html.Div([
      
        # Hiperparameters and colors settings
        html.Div([
            html.Div(menu_sections.hyperparameters, style=stl.section),
            # html.Div(style=dict(height="1%")),
            html.Div(menu_sections.colors, style=stl.section),
            # html.Div(style=dict(height="1%")),
            html.Div(menu_sections.upload, style=dict(margin=5)),
        ], className="six columns"),
    
        # Image display
        html.Div([
            dcc.Loading([
                dcc.Graph(figure=fg.default_figure, id="figure_graph", 
                          style=dict(width="100%", marginTop="5px")),
            ], type="graph", style=dict(marginTop="15vh")),

        ], id="image_div", className="six columns", style=dict(
            height="100vh", float="right")),

        # Confirm Dialogs
        html.Div([
            dcc.ConfirmDialog(id="im_failed", message="Failed to load the image."),
        ]),

        # Storage
        dcc.Store(id="store_boxes", data=[]),
        dcc.Store(id="store_scores", data=[]),
        dcc.Store(id="store_colors", data=[]),
        dcc.Store(id="store_figure_data", data=[]),
        dcc.Store(id="store_figure_layout", data=[]),
        dcc.Store(id="store_image", data=fg.default_raw_image),
        dcc.Store(id="store_image_shape", data=dict(height=400, width=680)),

    ], style=dict(margin="10px")),
]


def compute_fer(im, threshold):
    """Compute Facial Expressions probabilities from an image."""

    np_im = drc.b64_to_numpy(im, to_scalar=False)
    threshold /= 100

    # Compute faces locations
    boxes = face_detector.compute(np_im, threshold=threshold)
    # Stop process if no face is detected ...
    if boxes == []:
        return [], []

    # Extract detected faces
    rois = de.image_utils.extract_rois(np_im, boxes, method="min", square_box=True)
    rois = fer_model.preprocess_input(rois, normalize="norm_p")

    # Classify facial expressions
    _, scores = fer_model.predict(rois, return_scores=True)
    return boxes, scores


### COMPUTE AND SHOW IMAGE ###
@app.callback(Output("store_collection", "data"), [
    Input("model_dropdown", "value")])
def load_fer_model(model_name):
    """Load FERModel."""

    global fer_model
    fer_model = de.models.FERModel(model_name)
    return dict(model_name=model_name)


@app.callback([Output("store_image_shape", "data"),
    Output("store_image", "data")], [
    Input("submit_url", "n_clicks"),
    Input("upload_image", "contents")], [
    State("input_url", "value")])
def update_raw_image(bt_submit, up_contents, url):
    """Update raw image by upload or link."""

    # Retrive image from upload
    if up_contents is not None:
        raw_image = fg.submit_local_image(up_contents)

        # Encode raw_image and get its shape
        if raw_image is not None:
            w, h = raw_image.size
            im_shape = dict(height=h, width=w)
            b64_im = drc.pil_to_b64(raw_image)
            return im_shape, b64_im
    
        # If some error, Prevent updates
        else:
            raise PreventUpdate

    # Retrive image from url
    elif url is not None and bt_submit >= 1:
        raw_image = fg.submit_url_image(url)

        # Encode raw_image and get its shape
        if raw_image is not None:
            w, h = raw_image.size
            im_shape = dict(height=h, width=w)
            b64_im = drc.pil_to_b64(raw_image)
            return im_shape, b64_im

        # If some error, Prevent updates
        else:
            raise PreventUpdate

    # If some error, Prevent updates
    else:
        raise PreventUpdate


@app.callback([Output("store_boxes", "data"), 
    Output("store_scores", "data")], [
    Input("store_image", "data"),
    Input("store_collection", "data"),
    Input("fd_threshold_slider", "value")])
def compute_boxes_and_scores(raw_image, _, threshold):
    """Compute Facial Expressions probabilities from an image."""

    try:
        boxes, scores = compute_fer(raw_image, threshold)
        return boxes, scores
    except:
        raise PreventUpdate


@app.callback(Output("store_colors", "data"), [
    Input("anger_color_drop", "value"),
    Input("disgust_color_drop", "value"),
    Input("fear_color_drop", "value"),
    Input("happiness_color_drop", "value"),
    Input("neutral_color_drop", "value"),
    Input("sadness_color_drop", "value"),
    Input("surprise_color_drop", "value")])
def update_colors_storage(c_an, c_di, c_fe, c_ha, c_ne, c_sa, c_su):
    """Get bounding boxes colors and pass it to a dict storage."""

    return {k:v for k,v in enumerate([
        c_an, c_di, c_fe, c_ha, c_ne, c_sa, c_su])}


@app.callback(Output("store_figure_layout", "data"), [
    Input("store_image", "data")], [
    State("store_image_shape", "data")])
def update_figure_layout(raw_image, im_shape):
    """Update figure graph layout."""

    return fg.generate_figure_layout(raw_image, im_shape)


@app.callback(Output("store_figure_data", "data"), [
    Input("store_boxes", "data"),
    Input("store_scores", "data"),
    Input("store_colors", "data")], [
    State("store_image_shape", "data")])
def update_figure_layout(boxes, scores, colors, im_shape):
    """Update figure graph data (bounding_boxes)."""

    if boxes is None or scores is None:
        raise PreventUpdate

    return fg.generate_figure_data(boxes, scores, colors, im_shape)


@app.callback(Output("figure_graph", "figure"), [
    Input("store_figure_data", "data"),
    Input("store_figure_layout", "data")])
def update_figure(data, layout):
    """Return Plotly graph with figure and boxes.""" 
    
    return go.Figure(data=data, layout=layout)


### DOWNLOAD IMAGE ###
@app.callback(Output("download_image", "href"), [
    Input("store_image", "data")])
def download_image(raw_fig):
    media_type = "images/png"
    href = f"data:{media_type};base64,{raw_fig}"
    return href



### RESET BUTTONS AND CONTENTS ###
@app.callback(Output("submit_url", "n_clicks"), [
    Input("store_image", "data")], [
    State("submit_url", "n_clicks")])
def reset_submit_button(_, bt_submit):
    if bt_submit > 0:
        return 0
    else:
        raise PreventUpdate


@app.callback(Output("upload_image", "contents"), [
    Input("store_image", "data")], [
    State("upload_image", "contents")])
def reset_upload_content(_, up_contents):
    if up_contents is not None:
        return None
    else:
        raise PreventUpdate


@app.callback(Output("input_url", "value"), [
    Input("store_image", "data"),
    Input("submit_url", "n_clicks")], [
    State("input_url", "value")])
def reset_input_value(_, bt_submit, image_url):
    if image_url is not None:
        return ''

    else:
        raise PreventUpdate