from slack_bolt import CompleteSuccess
from slack_bolt import CompleteError
from logging import Logger


def reverse_string(event, complete_success: CompleteSuccess, complete_error: CompleteError, logger: Logger):
    try:
        string_to_reverse = event["inputs"]["stringToReverse"]
        complete_success({
            "reverseString": string_to_reverse[::-1]
        })
    except Exception as e:
        logger.error(e)
        complete_error("Cannot reverse string")
        raise e
