from logging import Logger
from slack_bolt import Complete
from slack_bolt import App
from .approve_me import approve_me, approve_action, deny_action, APPROVE_ID, DENY_ID

from slack_bolt.function import Function


def register(app: App):

    @app.function("reverse")
    def reverse_string(event, context, complete: Complete, logger: Logger):
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

    approve_me_function: Function = app.function("approve_me")(approve_me)
    approve_me_function.action(APPROVE_ID)(approve_action)
    approve_me_function.action(DENY_ID)(deny_action)
