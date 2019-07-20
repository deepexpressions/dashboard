import dash
import logging
from absl import logging as log


# Minimize logs
log._warn_preinit_stderr = 0
logging.getLogger('werkzeug').setLevel(logging.ERROR)


# Start app
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True
app.scripts.config.serve_locally=True
app.css.config.serve_locally=True