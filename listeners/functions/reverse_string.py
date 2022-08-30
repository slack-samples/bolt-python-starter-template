from slack_bolt import Complete
from logging import Logger


def reverse_string(event, complete: Complete, logger: Logger):
    try:
        string_to_reverse = event["inputs"]["stringToReverse"]
        complete(
            outputs={
            "reverseString": string_to_reverse[::-1]
        })
    except Exception as e:
        logger.error(e)
        complete(error="Cannot reverse string")
        raise e
