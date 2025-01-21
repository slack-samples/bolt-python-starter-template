import logging
from unittest.mock import Mock

from slack_bolt import Ack
from slack_sdk import WebClient

from listeners.views.sample_view import sample_view_callback


test_logger = logging.getLogger(__name__)


class TestSampleView:
    def setup_method(self):
        self.fake_ack = Mock(Ack)
        self.fake_body = {"user": {"id": "U1234"}}
        self.fake_view = {
            "state": {
                "values": {
                    "input_block_id": {"sample_input_id": {"value": "test value"}},
                    "select_channel_block_id": {"sample_dropdown_id": {"selected_conversation": "C1234"}},
                }
            }
        }
        self.fake_client = Mock(WebClient)
        self.fake_client.chat_postMessage = Mock(WebClient.chat_postMessage)

    def test_sample_view_callback(self):
        sample_view_callback(
            self.fake_view,
            ack=self.fake_ack,
            body=self.fake_body,
            client=self.fake_client,
            logger=test_logger,
        )

        self.fake_ack.assert_called_once()

        self.fake_client.chat_postMessage.assert_called_once()
        kwargs = self.fake_client.chat_postMessage.call_args.kwargs
        assert (
            kwargs["channel"]
            == self.fake_view["state"]["values"]["select_channel_block_id"]["sample_dropdown_id"]["selected_conversation"]
        )
        assert self.fake_view["state"]["values"]["input_block_id"]["sample_input_id"]["value"] in kwargs["text"]
        assert self.fake_body["user"]["id"] in kwargs["text"]

    def test_ack_exception(self, caplog):
        self.fake_ack.side_effect = Exception("test exception")
        sample_view_callback(
            self.fake_view,
            ack=self.fake_ack,
            body=self.fake_body,
            client=self.fake_client,
            logger=test_logger,
        )

        self.fake_ack.assert_called_once()
        assert str(self.fake_ack.side_effect) in caplog.text
