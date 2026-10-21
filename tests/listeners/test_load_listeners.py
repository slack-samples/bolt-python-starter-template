import sys
from pkgutil import walk_packages
from unittest.mock import patch

from slack_bolt import App
from slack_sdk import WebClient

import listeners
from listeners import load_listeners


def make_app() -> App:
    with patch.object(WebClient, "auth_test"):
        return App(token="test-bot-token")


class TestLoadListeners:
    def test_imports_every_listener_module(self):
        load_listeners(make_app())

        for module_info in walk_packages(listeners.__path__, f"{listeners.__name__}."):
            assert module_info.name in sys.modules

    def test_registers_every_listener_on_the_app(self):
        app = make_app()

        load_listeners(app)

        assert len(app._listeners) == 6

    def test_registers_every_listener_on_each_app(self):
        first_app, second_app = make_app(), make_app()

        load_listeners(first_app)
        load_listeners(second_app)

        assert len(first_app._listeners) == 6
        assert len(second_app._listeners) == 6
