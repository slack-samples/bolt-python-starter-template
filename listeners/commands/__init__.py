from .sample_command import sample_command_callback

def register(app):
    app.command('/sample-command')(sample_command_callback)