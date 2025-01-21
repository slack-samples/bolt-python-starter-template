import logging
from unittest.mock import Mock

from slack_bolt import Ack
from slack_sdk import WebClient

from listeners.actions.sample_action import sample_action_callback

test_logger = logging.getLogger(__name__)


class TestSampleAction:
    def setup_method(self):
        self.fake_ack = Mock(Ack)
        self.fake_body = {"view": {"id": "test_id", "hash": "156772938.1827394"}}

        self.fake_client = Mock(WebClient)
        self.fake_client.views_update = Mock(WebClient.views_update)

    def test_sample_action_callback(self):
        sample_action_callback(
            ack=self.fake_ack,
            body=self.fake_body,
            client=self.fake_client,
            logger=test_logger,
        )

        self.fake_ack.assert_called_once()

        self.fake_client.views_update.assert_called_once()
        kwargs = self.fake_client.views_update.call_args.kwargs
        assert kwargs["view_id"] == self.fake_body["view"]["id"]
        assert kwargs["hash"] == self.fake_body["view"]["hash"]
        assert kwargs["view"] is not None

    def test_ack_exception(self, caplog):
        self.fake_ack.side_effect = Exception("test exception")
        sample_action_callback(
            ack=self.fake_ack,
            body=self.fake_body,
            client=self.fake_client,
            logger=test_logger,
        )

        self.fake_ack.assert_called_once()
        assert str(self.fake_ack.side_effect) in caplog.text
