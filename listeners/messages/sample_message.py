import re
from logging import Logger

from slack_bolt import BoltContext, Say

from bolt_app import app


# To receive messages from a channel or dm your app must be a member!
@app.message(re.compile("(hi|hello|hey)"))
def sample_message_callback(context: BoltContext, say: Say, logger: Logger):
    try:
        greeting = context["matches"][0]
        say(f"{greeting}, how are you?")
    except Exception:
        logger.exception("Error responding to sample message")
