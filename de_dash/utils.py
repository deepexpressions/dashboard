import json
import base64
import de_dash.dash_reusable_components as drc
from PIL import Image



########################################### LOCAL IMAGES ###########################################


DE_LOGO = base64.b64encode(open(r"de_dash/assets/images/logo2.png", "rb").read())
GIT_LOGO = base64.b64encode(open(r"de_dash/assets/images/github-black.png", "rb").read())


############################################## COLORS ##############################################


COLORS = {
    "lv0":"#01233f",    # de - darker blue
    "lv1":"#083b66",    # de - ...
    "lv2":"#1761a0",    # de - ...
    "lv3":"#4c96d7",    # de - lighter blue
    "bg":"#cbd6e7",     # background 
    "header":"#6600cc", # header bar color
}


############################################## STYLES ##############################################


# Default style with logo on background
BG_STYLE = {"width":"100%", "height":"100%", "top":"70px", "left":"0px", "z-index":"1000", 
            "position":"fixed", "background-image":"url('/assets/images/small_logo4.png')",}

# Default style for sections
SEC_STYLE = {"padding":20, "margin":5, "borderRadius":5, "border":"thin lightgrey solid",
            "user-select":"none", "-moz-user-select":"none", "-webkit-user-select":"none", 
            "-ms-user-select":"none", "backgroundColor":COLORS["header"], "marginLeft":"4.15%"}

# Default style for upload component
UP_STYLE = {"width":"100%","height":"50px","lineHeight":"50px","borderWidth":"1px",
            "borderStyle":"dashed","borderRadius":"5px","textAlign":"center"},


######################################### DASH IMAGE UTILS #########################################

