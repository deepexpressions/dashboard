import json
import base64
from PIL import Image

from . import dash_reusable_components as drc


########################################### LOCAL IMAGES ###########################################


DE_LOGO = base64.b64encode(open(r"de_dash/assets/images/logo2.png", "rb").read())
IMAGE = base64.b64encode(open(r"de_dash/assets/images/default.jpg", "rb").read())


############################################## COLORS ##############################################


COLORS = dict(
    lv0="#01233f",    # de logo' - darker blue
    lv1="#083b66",    # de logo' - ...
    lv2="#1761a0",    # de logo' - ...
    lv3="#4c96d7",    # de logo' - lighter blue
    bg="#E1E7E4",     # background color
    header="#66a3ff", # header bar color
)


############################################## STYLES ##############################################

# Shadow box style
SHADOW_BOX = {"box-shadow" : 
    "0 4px 5px 0 rgba(0,0,0,0.14), 0 1px 10px 0 rgba(0,0,0,0.12), 0 2px 4px -1px rgba(0,0,0,0.3)"}

# Default style with logo on background
BG_STYLE = dict(width="100%", height="100vh", top="70px", left="0px", position="fixed", 
    **{"z-index":"1000"})

# Default style for sections
SEC_STYLE = dict(padding=20, margin=5, borderRadius=5, border="thin lightgrey solid",
    marginBottom="2%", backgroundColor=COLORS["bg"], **SHADOW_BOX)

# Default style for buttons
INPUT_STYLE = dict(width="100%", fontSize=10, **SHADOW_BOX)           

# Default style for buttons
BUTTON_STYLE = dict(width="90%", color="#ffffff", fontSize=10,
    backgroundColor=COLORS["header"], **SHADOW_BOX)

# Style for download button
DOWNLOAD_BUTTON_STYLE = dict(width="90%", color="#ffffff", fontSize=10,
    backgroundColor="#0052cc", **SHADOW_BOX)

# Style for github button
GITHUB_BUTTON_STYLE = dict(width="100%", height="40px", color="#ffffff",
    marginTop="15px", backgroundColor=COLORS["header"], **SHADOW_BOX)

# Default style for color dropdown
COLOR_DROP_STYLE = dict(width="100%", fontSize=12, borderRadius=0)

# Default style for color dropdown div
COLOR_DROP_STYLE_DIV = dict(marginLeft="-10px", fontSize=12, borderRadius=0)


######################################### DASH IMAGE UTILS #########################################

