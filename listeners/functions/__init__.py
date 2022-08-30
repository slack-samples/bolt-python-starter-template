from logging import Logger
from slack_bolt import Complete
from slack_bolt import App
from .reverse_string import reverse_string
from .request_approval import request_approval
from .actions import approve_action, deny_action

from slack_bolt.function import Function


def register(app: App):

    @app.function("reverse")
    def reverse_string(event, complete: Complete, logger: Logger):
        try:
            string_to_reverse = event["inputs"]["stringToReverse"]
            complete(
                outputs={
                    "reverseString": string_to_reverse[::-1]
                }
            )
        except Exception as e:
            logger.error(e)
            complete(error="Cannot reverse string")
            raise e

    request_approval_function: Function = app.function("review_approval")(request_approval)
    request_approval_function.action("approve_action_id")(approve_action)
    request_approval_function.action("deny_action_id")(deny_action)
