from slack_bolt import App

from listeners import load_listeners

load_listeners(App(token="test-bot-token", token_verification_enabled=False))
