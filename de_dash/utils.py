import base64


# Import local images
IM_LOGO_0 = base64.b64encode(open(r"de_dash/assets/images/logo.png", "rb").read())
IM_LOGO_1 = base64.b64encode(open(r"de_dash/assets/images/small_logo.png", "rb").read())


# Default style with logo on background
BG_STYLE = {"width":"100%", "height":"100%", "top":"70px", "left":"0px", "z-index":"1000", 
            "position":"fixed", "background-image":"url('/assets/images/small_logo.png')",}

# Default style for upload sections
UP_SEC_STYLE = {"padding": 20, "margin": 5, "borderRadius": 5, "border": "thin lightgrey solid",
                "user-select": "none", "-moz-user-select": "none", "-webkit-user-select": "none", 
                "-ms-user-select": "none"}

# Default style for upload component
UP_STYLE = {"width":"100%","height":"50px","lineHeight":"50px","borderWidth":"1px",
            "borderStyle":"dashed","borderRadius":"5px","textAlign":"center"},


# # Colors
# COLORS = {
#     "lv0":"#01233f",
#     "lv1":"#083b66",
#     "lv2":"#1761a0",
#     "lv3":"#4c96d7",
# }