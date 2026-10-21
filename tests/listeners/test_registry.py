from unittest.mock import patch

import pytest
from slack_bolt import App
from slack_sdk import WebClient

from listeners import Registry


def make_app() -> App:
    with patch.object(WebClient, "auth_test"):
        return App(token="test-bot-token")


def app_mention_callback(say):
    say("Hi there!")


class TestRegistry:
    def test_decorator_returns_the_original_function(self):
        registry = Registry()

        assert registry.event("app_mention")(app_mention_callback) is app_mention_callback

    def test_apply_registers_the_listener_on_the_app(self):
        registry = Registry()
        registry.event("app_mention")(app_mention_callback)
        app = make_app()

        registry.apply(app)

        assert [listener.ack_function for listener in app._listeners] == [app_mention_callback]

    def test_unknown_app_method_raises_attribute_error(self):
        with pytest.raises(AttributeError):
            Registry().evnt("app_mention")
