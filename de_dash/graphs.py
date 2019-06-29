import requests
from PIL import Image
from io import BytesIO
from PIL.ImageColor import colormap
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


def _generate_figure_with_hover(im, boxes=None, scores=None, colors=None):
    """Generates Plotly figure given a PIL image."""
    
    width, height = im.size
    encoded_image = drc.pil_to_b64(im)

    boxes = [[37,  24, 135, 120], [ 15, 108,  75, 216]]
    scores = [[9.4943964e-01, 7.6841045e-04, 4.1072398e-02, 9.1929114e-06,
               7.6404614e-03, 6.1861333e-04, 4.5129244e-04], [
               4.5129244e-04, 7.6841045e-04, 4.1072398e-02, 9.1929114e-06, 
               7.6404614e-03, 6.1861333e-04, 9.4943964e-01]]
    colors = {0: "magenta", 1: "cornflowerBlue", 2: "darkturquoise",
              3: "green", 4: "red", 5: "mediumorchid", 6: "khaki"}                 


    detections=[
        go.Scatter(
            x=[box[2], box[0], box[0], box[2], box[2]],
            y=[ height- box[3], height- box[3], 
                height- box[1], height- box[1], 
                height- box[3]],
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
            line = dict(width=0, color=colormap[colors[score.index(max(score))]]),
            showlegend = False
        ) 
    for box, score in zip(boxes, scores)]

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

    return go.Figure(data=detections, layout=layout)


def submit_image_from_url(image_url):
    try:
        response = requests.get(image_url)
        im = Image.open(BytesIO(response.content))
        return im, _generate_figure(im)
    
    except IOError:
        return None, None
    

def submit_local_image(content):
    try:
        string = content.split(';base64,')[-1]
        im = drc.b64_to_pil(string)
        return im, _generate_figure(im)
    
    except IOError:
        return None, None


# Default figure to show
DEFAULT_IMAGE = drc.pil_to_b64(Image.open("de_dash/assets/images/cat_test.png"))
DEFAULT_FIGURE = _generate_figure_with_hover(Image.open("de_dash/assets/images/cat_test.png"))
