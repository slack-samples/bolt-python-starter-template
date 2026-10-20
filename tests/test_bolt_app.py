import sys
from pkgutil import walk_packages

import listeners
from bolt_app import load_listeners, oauth_settings


class TestBoltApp:
    def test_load_listeners_imports_every_listener_module(self):
        load_listeners()

        for module_info in walk_packages(listeners.__path__, f"{listeners.__name__}."):
            assert module_info.name in sys.modules

    def test_oauth_settings_without_client_id(self, monkeypatch):
        monkeypatch.delenv("SLACK_CLIENT_ID", raising=False)

        assert oauth_settings() is None

    def test_oauth_settings_with_client_id(self, monkeypatch):
        monkeypatch.setenv("SLACK_CLIENT_ID", "test-client-id")
        monkeypatch.setenv("SLACK_CLIENT_SECRET", "test-client-secret")

        settings = oauth_settings()

        assert settings.client_id == "test-client-id"
        assert settings.scopes == ["channels:history", "chat:write", "commands"]
