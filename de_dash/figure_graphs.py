import numpy as np
import requests
from PIL import Image
from io import BytesIO
from PIL.ImageColor import colormap
from plotly import graph_objs as go

from . import dash_reusable_components as drc


_HTML_IMG_SRC_PARAMETERS = "data:image/png;base64, "


def submit_url_image(image_url):
    """Open Image from url."""

    try:
        response = requests.get(image_url)
        im = Image.open(BytesIO(response.content))
        return im
    
    except IOError:
        return None
    

def submit_local_image(content):
    """Open Image from upload."""

    try:
        string = content.split(';base64,')[-1]
        im = drc.b64_to_pil(string)
        return im
    
    except IOError:
        return None


def generate_figure_layout(encoded_image, im_shape):
    """Generate figure layout."""

    height, width = im_shape["height"], im_shape["width"]

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
                source = _HTML_IMG_SRC_PARAMETERS + encoded_image
            )
        ]
    )

    return layout


def generate_figure_data(boxes, scores, colors, im_shape):
    """Generate figure data (bouding boxes)."""

    height, width = im_shape["height"], im_shape["width"]

    if boxes is None or scores is None:
        return []
    
    data = [
        go.Scatter(
            x=[box[2], box[0], box[0], box[2], box[2]],
            y=[height - box[3], height - box[3], 
               height - box[1], height - box[1], 
               height - box[3]],

            hoveron = 'fills',
            name = '',
            text = ["".join(t) for t in [
                    ("{}Angry: {:.2f}%{}<br>".format(
                        "<b>" if score.index(max(score)) == 0 else "", 
                        score[0]*100, "</b>" if score.index(max(score)) == 0 else ""),
                    "{}Disgust: {:.2f}%{}<br>".format(
                        "<b>" if score.index(max(score)) == 1 else "", 
                        score[1]*100, "</b>" if score.index(max(score)) == 1 else ""),
                    "{}Fear: {:.2f}%{}<br>".format(
                        "<b>" if score.index(max(score)) == 2 else "", 
                        score[2]*100, "</b>" if score.index(max(score)) == 2 else ""),
                    "{}Happiness: {:.2f}%{}<br>".format(
                        "<b>" if score.index(max(score)) == 3 else "", 
                        score[3]*100, "</b>" if score.index(max(score)) == 3 else ""),
                    "{}Neutral: {:.2f}%{}<br>".format(
                        "<b>" if score.index(max(score)) == 4 else "", 
                        score[4]*100, "</b>" if score.index(max(score)) == 4 else ""),
                    "{}Sadness: {:.2f}%{}<br>".format(
                        "<b>" if score.index(max(score)) == 5 else "", 
                        score[5]*100, "</b>" if score.index(max(score)) == 5 else ""),
                    "{}Surprise: {:.2f}%{}<br>".format(
                        "<b>" if score.index(max(score)) == 6 else "", 
                        score[6]*100, "</b>" if score.index(max(score)) == 6 else ""),
                    )]][0],

            mode='lines',
            line = dict(width=2, color=colormap[colors[str(score.index(max(score)))]]),
            showlegend = False
        ) 
    for box, score in zip(boxes, scores)]

    return data

# Default figure to show
default_raw_image = drc.pil_to_b64(Image.open("de_dash/assets/images/default.jpg"))
default_figure = go.Figure(data=[], layout=go.Layout())