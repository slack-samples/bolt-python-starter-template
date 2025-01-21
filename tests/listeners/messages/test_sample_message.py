import logging
from unittest.mock import Mock

from slack_bolt import BoltContext, Say

from listeners.messages.sample_message import sample_message_callback


test_logger = logging.getLogger(__name__)


class TestSampleMessage:
    def setup_method(self):
        self.fake_say = Mock(Say)
        self.fake_context = BoltContext(matches=["hello"])

    def test_sample_message_callback(self):
        sample_message_callback(
            context=self.fake_context,
            say=self.fake_say,
            logger=test_logger,
        )

        self.fake_say.assert_called_once()
        args = self.fake_say.call_args.args
        assert self.fake_context.matches[0] in args[0]

    def test_say_exception(self, caplog):
        self.fake_say.side_effect = Exception("test exception")
        sample_message_callback(
            context=self.fake_context,
            say=self.fake_say,
            logger=test_logger,
        )

        self.fake_say.assert_called_once()
        assert str(self.fake_say.side_effect) in caplog.text
