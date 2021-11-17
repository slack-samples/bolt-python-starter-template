from .sample_view import sample_view_callback

def register(app):
    app.view('sample_view_id')(sample_view_callback)