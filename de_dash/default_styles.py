import json
import base64


########################################### LOCAL IMAGES ###########################################


DE_LOGO = base64.b64encode(open(r"de_dash/assets/images/logo2.png", "rb").read())


############################################## _COLORS ##############################################


_COLORS = dict(
    lv0="#01233f",    # de logo' - darker blue
    lv1="#083b66",    # de logo' - ...
    lv2="#1761a0",    # de logo' - ...
    lv3="#4c96d7",    # de logo' - lighter blue
    bg="#E1E7E4",     # background color
    header="#66a3ff", # header bar color
)


############################################## STYLES ##############################################

# Shadow box style
_shadow_box = {"box-shadow" : 
    "0 4px 5px 0 rgba(0,0,0,0.14), 0 1px 10px 0 rgba(0,0,0,0.12), 0 2px 4px -1px rgba(0,0,0,0.3)"}

# Default style with logo on background
background = dict(width="100%", height="100vh", top="70px", left="0px", position="fixed", 
    **{"z-index":"1000"})

# Default style for sections
section = dict(padding=20, margin=5, borderRadius=5, border="thin lightgrey solid",
    marginBottom="2%", backgroundColor="#00000000", **_shadow_box)

# Default style for buttons
inputs = dict(width="100%", fontSize=10, **_shadow_box)           

# Default style for buttons
button = dict(width="90%", color="#ffffff", fontSize=10,
    backgroundColor=_COLORS["header"], **_shadow_box)

# Style for download button
download_button = dict(width="90%", color="#ffffff", fontSize=10,
    backgroundColor="#0052cc", **_shadow_box)

# Style for github button
github_button = dict(width="100%", height="40px", color="#ffffff",
    marginTop="15px", backgroundColor=_COLORS["header"], **_shadow_box)

# Default style for color dropdown
color_drop = dict(width="100%", fontSize=12, borderRadius=0)

# Default style for color dropdown div
color_drop_div = dict(marginLeft="-10px", fontSize=12, borderRadius=0)
