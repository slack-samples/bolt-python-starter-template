import logging
from unittest.mock import Mock

from slack_bolt import Ack, Respond

from listeners.commands.sample_command import sample_command_callback


test_logger = logging.getLogger(__name__)


class TestSampleCommands:
    def setup_method(self):
        self.fake_ack = Mock(Ack)
        self.fake_respond = Mock(Respond)
        self.fake_command = {"text": "test command"}

    def test_sample_command_callback(self):
        sample_command_callback(
            self.fake_command,
            ack=self.fake_ack,
            respond=self.fake_respond,
            logger=test_logger,
        )

        self.fake_ack.assert_called_once()

        self.fake_respond.assert_called_once()
        args = self.fake_respond.call_args.args
        assert self.fake_command["text"] in args[0]

    def test_ack_exception(self, caplog):
        self.fake_ack.side_effect = Exception("test exception")
        sample_command_callback(
            self.fake_command,
            ack=self.fake_ack,
            respond=self.fake_respond,
            logger=test_logger,
        )

        self.fake_ack.assert_called_once()
        assert str(self.fake_ack.side_effect) in caplog.text
