from logging import Logger
from slack_bolt import Complete


def sample_function(event, complete: Complete, logger: Logger):
    try:
        message = event["inputs"]["message"]
        complete(outputs={"updatedMsg": f":wave: You submitted the following message: \n\n>{message}"})
    except Exception as e:
        logger.error(e)
        complete(error="Cannot submit the message")
        raise e
