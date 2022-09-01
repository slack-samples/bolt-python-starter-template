import os
import logging
from copy import deepcopy

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from listeners import register_listeners


# Initialization
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
logging.basicConfig(level=logging.DEBUG)

# Register Listeners
register_listeners(app)


@app.middleware  # or app.use(log_request)
def log_request(client, logger, body, next):
    logger.info(f"this is my token: {client.token}")
    logger.debug(body)
    return next()


# Start Bolt app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
