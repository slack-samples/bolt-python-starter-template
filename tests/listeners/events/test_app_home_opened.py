import logging
from unittest.mock import Mock

from slack_sdk import WebClient

from listeners.events.app_home_opened import app_home_opened_callback

test_logger = logging.getLogger(__name__)


class TestAppHomeOpened:
    def setup_method(self):
        self.fake_event = {"tab": "home", "user": "U123"}

        self.fake_client = Mock(WebClient)
        self.fake_client.views_publish = Mock(WebClient.views_publish)

    def test_app_home_opened_callback(self):
        app_home_opened_callback(client=self.fake_client, event=self.fake_event, logger=test_logger)

        self.fake_client.views_publish.assert_called_once()
        kwargs = self.fake_client.views_publish.call_args.kwargs
        assert kwargs["user_id"] == self.fake_event["user"]
        assert kwargs["view"] is not None

    def test_event_tab_not_home(self):
        self.fake_event["tab"] = "about"
        app_home_opened_callback(client=self.fake_client, event=self.fake_event, logger=test_logger)

        self.fake_client.views_publish.assert_not_called()

    def test_views_publish_exception(self, caplog):
        self.fake_client.views_publish.side_effect = Exception("test exception")
        app_home_opened_callback(client=self.fake_client, event=self.fake_event, logger=test_logger)

        self.fake_client.views_publish.assert_called_once()
        assert str(self.fake_client.views_publish.side_effect) in caplog.text
