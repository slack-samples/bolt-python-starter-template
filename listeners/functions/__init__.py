from slack_bolt import App

from .sample_function import sample_function


def register(app: App):
    app.function("sample_function")(sample_function)
