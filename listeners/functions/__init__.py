from slack_bolt import App
from .reverse_string import reverse_string


def register(app: App):
    app.function("reverse")(reverse_string)
