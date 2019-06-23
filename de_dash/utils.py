import json
import base64
import de_dash.dash_reusable_components as drc
from PIL import Image



########################################### LOCAL IMAGES ###########################################


DE_LOGO = base64.b64encode(open(r"de_dash/assets/images/logo0.png", "rb").read())
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


# Default style with logo on background
BG_STYLE = dict(width="100%", height="100%", top="70px", left="0px", position="fixed", 
                **{"z-index":"1000", })#"background-image":"url('/assets/images/small_logo4.png')"})


# Default style for sections
SEC_STYLE = dict(padding=20, margin=5, borderRadius=5, border="thin lightgrey solid",
                 backgroundColor=COLORS["bg"], **{"box-shadow" : 
                 "0 4px 5px 0 rgba(0,0,0,0.14), 0 1px 10px 0 rgba(0,0,0,0.12), 0 2px 4px -1px rgba(0,0,0,0.3)"})

# Default style for upload component
UP_STYLE = dict(width="100%", height="50px", lineHeight="50px", borderWidth="1px", 
                borderStyle="dashed", borderRadius="5px", textAlign="center")

# Default style for buttons
BUTTON_STYLE = dict(width="100%", marginTop="5px", color="#ffffff", backgroundColor=COLORS["header"], **{"box-shadow" : 
                 "0 4px 5px 0 rgba(0,0,0,0.14), 0 1px 10px 0 rgba(0,0,0,0.12), 0 2px 4px -1px rgba(0,0,0,0.3)"})

# Default style for color dropdown
COLOR_DROP_STYLE = dict(width="100%", fontSize=12, borderRadius=0) #, border="#ff0000")
COLOR_DROP_STYLE_DIV = dict(marginLeft="-10px", fontSize=12, borderRadius=0)#, border="thin lightgrey solid")


######################################### DASH IMAGE UTILS #########################################

