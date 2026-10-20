import logging
import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import listeners

logging.basicConfig(level=logging.DEBUG)

# Initialization
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Load Listeners
listeners.app = app
listeners.load_listeners()

# Start Bolt app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
