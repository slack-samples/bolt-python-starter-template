from .sample_action import sample_action_callback

def register(app):
    app.action('sample_action_id')(sample_action_callback)