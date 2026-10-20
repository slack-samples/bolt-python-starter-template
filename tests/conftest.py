from unittest.mock import patch

from slack_bolt import App
from slack_sdk import WebClient

import listeners

with patch.object(WebClient, "auth_test"):
    listeners.app = App(token="test-bot-token")
listeners.load_listeners()
