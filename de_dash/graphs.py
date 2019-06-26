import requests
from PIL import Image
from io import BytesIO
from plotly import graph_objs as go
from . import dash_reusable_components as drc


HTML_IMG_SRC_PARAMETERS = "data:image/png;base64, "


def _generate_figure(im):
    """Generates Plotly figure given a PIL image."""
    
    width, height = im.size
    encoded_image = drc.pil_to_b64(im)

    layout = go.Layout(

        margin = dict(l=0, r=0, t=0, b=0),

        xaxis = go.layout.XAxis(
            scaleratio = 1,
            visible = False,
            scaleanchor = "y",
            range = [0, width],            
        ),

        yaxis = go.layout.YAxis(
            visible = False,
            range = [0, height]
        ),

        images = [
            go.layout.Image(
                x = 0,
                y = 0,
                xref = "x",
                yref = "y",
                sizex = width,
                sizey = height,
                opacity = 1.0,
                yanchor = "bottom",
                layer = "below",
                sizing = "stretch",
                source = HTML_IMG_SRC_PARAMETERS + encoded_image
            )
        ]
    )

    return go.Figure(data=[], layout=layout)


def submit_image_from_url(image_url):
    """Show image given an url."""

    response = requests.get(image_url)
    im = Image.open(BytesIO(response.content))
    return _generate_figure(im)
    

# Default figure to show
DEFAULT_FIGURE = _generate_figure(Image.open("de_dash/assets/images/default.jpg"))