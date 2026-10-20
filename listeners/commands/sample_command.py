from logging import Logger

from slack_bolt import Ack, Respond

from bolt_app import app


@app.command("/sample-command")
def sample_command_callback(command, ack: Ack, respond: Respond, logger: Logger):
    try:
        ack()
        respond(f"Responding to the sample command! Your command was: {command['text']}")
    except Exception:
        logger.exception("Error responding to sample command")
