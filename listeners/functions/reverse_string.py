from slack_bolt import Success
from slack_bolt import Error
from logging import Logger


def reverse_string(event, success: Success, err: Error, logger: Logger):
    try:
        logger.info(str(event))
        string_to_reverse = event["inputs"]["stringToReverse"]
        success({
            "reverseString": string_to_reverse[::-1]
        })
    except Exception as e:
        logger.error(e)
        err("Cannot reverse string")
        raise e
