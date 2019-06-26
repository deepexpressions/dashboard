import dash


# Start app
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True
app.scripts.config.serve_locally=True
app.css.config.serve_locally=True