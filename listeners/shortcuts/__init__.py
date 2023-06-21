from slack_bolt import App
from .forward_msg import forward_message_callback


def register(app: App):
    app.shortcut("report_message")(forward_message_callback)