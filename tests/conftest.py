from slack_bolt import App

import listeners

listeners.app = App(token="test-bot-token", token_verification_enabled=False)
listeners.load_listeners()
