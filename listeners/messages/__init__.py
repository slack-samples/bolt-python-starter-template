import re

from .sample_message import sample_message_callback

# To receive messages from a channel or dm your app must be a member!
def register(app):
    app.message(re.compile("(hi|hello|hey)"))(sample_message_callback)