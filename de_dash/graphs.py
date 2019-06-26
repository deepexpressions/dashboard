import plotly.plotly as py
import plotly.graph_objs as go
from . import dash_reusable_components as drc
from PIL import Image


HTML_IMG_SRC_PARAMETERS = 'data:image/png;base64, '


im = Image.open("de_dash/assets/images/default.jpg")
width, height = im.size
encoded_image = drc.pil_to_b64(im)


layout = go.Layout(

    xaxis = go.layout.XAxis(
        visible = False,
        scaleanchor = "y",
        scaleratio = 1,
        range = [0, width]),

    yaxis = go.layout.YAxis(
        visible=False,
        range = [0, height],),

    margin = {'l': 0, 'r': 0, 't': 0, 'b': 0},

    images = [go.layout.Image(
        x=0,
        y=0,
        xref="x",
        yref="y",
        sizex=width,
        sizey=height,
        opacity=1.0,
        yanchor="bottom",
        layer="below",
        sizing="stretch",
        source=HTML_IMG_SRC_PARAMETERS + encoded_image)]
)

# we add a scatter trace with data points in opposite corners to give the Autoscale feature a reference point
fig = go.Figure(data=[],layout = layout)