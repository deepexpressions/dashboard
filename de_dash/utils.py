import json
import base64
import de_dash.dash_reusable_components as drc
from PIL import Image



########################################### LOCAL IMAGES ###########################################


DE_LOGO = base64.b64encode(open(r"de_dash/assets/images/logo0.png", "rb").read())
GIT_LOGO = base64.b64encode(open(r"de_dash/assets/images/github0.png", "rb").read())


############################################## COLORS ##############################################


COLORS = dict(
    lv0="#01233f",    # de logo' - darker blue
    lv1="#083b66",    # de logo' - ...
    lv2="#1761a0",    # de logo' - ...
    lv3="#4c96d7",    # de logo' - lighter blue
    bg="#222222",     # background color
    header="#7B16E1", # header bar color
)

# PIL colors to draw bounding boxes
STANDARD_COLORS = [
    "AliceBlue", "Chartreuse", "Aqua", "Aquamarine", "Azure", "Beige", "Bisque",
    "BlanchedAlmond", "BlueViolet", "BurlyWood", "CadetBlue", "AntiqueWhite",
    "Chocolate", "Coral", "CornflowerBlue", "Cornsilk", "Crimson", "Cyan",
    "DarkCyan", "DarkGoldenRod", "DarkGrey", "DarkKhaki", "DarkOrange",
    "DarkOrchid", "DarkSalmon", "DarkSeaGreen", "DarkTurquoise", "DarkViolet",
    "DeepPink", "DeepSkyBlue", "DodgerBlue", "FireBrick", "FloralWhite",
    "ForestGreen", "Fuchsia", "Gainsboro", "GhostWhite", "Gold", "GoldenRod",
    "Salmon", "Tan", "HoneyDew", "HotPink", "IndianRed", "Ivory", "Khaki",
    "Lavender", "LavenderBlush", "LawnGreen", "LemonChiffon", "LightBlue",
    "LightCoral", "LightCyan", "LightGoldenRodYellow", "LightGray", "LightGrey",
    "LightGreen", "LightPink", "LightSalmon", "LightSeaGreen", "LightSkyBlue",
    "LightSlateGray", "LightSlateGrey", "LightSteelBlue", "LightYellow", "Lime",
    "LimeGreen", "Linen", "Magenta", "MediumAquaMarine", "MediumOrchid",
    "MediumPurple", "MediumSeaGreen", "MediumSlateBlue", "MediumSpringGreen",
    "MediumTurquoise", "MediumVioletRed", "MintCream", "MistyRose", "Moccasin",
    "NavajoWhite", "OldLace", "Olive", "OliveDrab", "Orange", "OrangeRed",
    "Orchid", "PaleGoldenRod", "PaleGreen", "PaleTurquoise", "PaleVioletRed",
    "PapayaWhip", "PeachPuff", "Peru", "Pink", "Plum", "PowderBlue", "Purple",
    "Red", "RosyBrown", "RoyalBlue", "SaddleBrown", "Green", "SandyBrown",
    "SeaGreen", "SeaShell", "Sienna", "Silver", "SkyBlue", "SlateBlue",
    "SlateGray", "SlateGrey", "Snow", "SpringGreen", "SteelBlue", "GreenYellow",
    "Teal", "Thistle", "Tomato", "Turquoise", "Violet", "Wheat", "White",
    "WhiteSmoke", "Yellow", "YellowGreen"
]


############################################## STYLES ##############################################


# Default style with logo on background
BG_STYLE = dict(width="100%", height="100%", top="70px", left="0px", position="fixed", 
                **{"z-index":"1000", })#"background-image":"url('/assets/images/small_logo4.png')"})


# Default style for sections
SEC_STYLE = dict(padding=20, margin=5, borderRadius=5, border="thin lightgrey solid",
                 backgroundColor=COLORS["header"],)

# Default style for upload component
UP_STYLE = dict(width="100%", height="50px", lineHeight="50px", borderWidth="1px", 
                borderStyle="dashed", borderRadius="5px", textAlign="center")

# Default style for buttons
BUTTON_STYLE = dict(width="100%", marginTop="5px", color="#ffffff", backgroundColor=COLORS["header"])


######################################### DASH IMAGE UTILS #########################################

