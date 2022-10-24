from logging import Logger

from slack_bolt import BoltContext, Say


def sample_message_callback(context: BoltContext, say: Say, logger: Logger):
    try:
        greeting = context["matches"][0]
        say(f"{greeting}, how are you?")
    except Exception as e:
        logger.error(e)
