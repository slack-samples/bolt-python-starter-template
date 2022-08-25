from logging import Logger
from slack_bolt import CompleteError
from slack_bolt import CompleteSuccess
from slack_bolt import App
from .reverse_string import reverse_string
from .request_approval import request_approval
from .actions import approve_action, deny_action

from slack_bolt.function import Function


def register(app: App):

    # @app.function("reverse")
    # def reverse_string(event, complete_success: CompleteSuccess, complete_error: CompleteError, logger: Logger):
    #     try:
    #         string_to_reverse = event["inputs"]["stringToReverse"]
    #         complete_success({
    #             "reverseString": string_to_reverse[::-1]
    #         })
    #     except Exception as e:
    #         logger.error(e)
    #         complete_error("Cannot reverse string")
    #         raise e

    # @reverse_string.action("hello")
    # def hello():
    #     pass

    # app.function("reverse")(reverse_string)

    request_approval_function: Function = app.function("review_approval")(request_approval)
    request_approval_function.action("approve_action_id")(approve_action)
    request_approval_function.action("deny_action_id")(deny_action)
