import logging
import os

from slack_bolt.adapter.socket_mode import SocketModeHandler

from listeners import app, load_listeners

logging.basicConfig(level=logging.DEBUG)

# Load Listeners
load_listeners()

# Start Bolt app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
