from unittest.mock import patch

from slack_bolt import App
from slack_sdk import WebClient

from listeners import load_listeners

with patch.object(WebClient, "auth_test"):
    load_listeners(App(token="test-bot-token"))
