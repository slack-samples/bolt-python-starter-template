import logging
from unittest.mock import Mock

from slack_bolt import Ack
from slack_sdk import WebClient

from listeners.shortcuts.sample_shortcut import sample_shortcut_callback


test_logger = logging.getLogger(__name__)


class TestSampleShortcut:
    def setup_method(self):
        self.fake_ack = Mock(Ack)
        self.fake_body = {"trigger_id": "t1234"}
        self.fake_client = Mock(WebClient)
        self.fake_client.views_open = Mock(WebClient.views_open)

    def test_sample_shortcut_callback(self):
        sample_shortcut_callback(body=self.fake_body, ack=self.fake_ack, client=self.fake_client, logger=test_logger)

        self.fake_ack.assert_called_once()

        self.fake_client.views_open.assert_called_once()
        kwargs = self.fake_client.views_open.call_args.kwargs
        assert kwargs["trigger_id"] == self.fake_body["trigger_id"]
        assert kwargs["view"] is not None

    def test_ack_exception(self, caplog):
        self.fake_ack.side_effect = Exception("test exception")
        sample_shortcut_callback(body=self.fake_body, ack=self.fake_ack, client=self.fake_client, logger=test_logger)

        self.fake_client.views_open.assert_not_called()
        self.fake_ack.assert_called_once()
        assert str(self.fake_ack.side_effect) in caplog.text
