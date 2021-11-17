from .app_home_opened import app_home_opened_callback

def register(app):
    app.event("app_home_opened")(app_home_opened_callback)