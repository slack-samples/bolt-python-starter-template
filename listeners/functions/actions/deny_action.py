from datetime import datetime
from difflib import context_diff
from logging import Logger

from slack_bolt import Ack, CompleteError
from slack_sdk import WebClient


def deny_action(ack: Ack, client: WebClient, body, complete_error: CompleteError, logger: Logger):
    try:
        ack()
        inputs = body["function_data"]["inputs"]
        manager = inputs["manager"]
        employee = inputs["employee"]
        end_date = datetime.fromtimestamp(inputs["end_date"]).strftime("%m/%d/%Y %H:%M")
        start_date = datetime.fromtimestamp(inputs["start_date"]).strftime("%m/%d/%Y %H:%M")

        context_block = get_context_block(start_date, end_date, manager)

        updated_blocks = body["message"]["blocks"][:-1]
        updated_blocks.append(context_block)

        text = f"Time-off request for {end_date} to {start_date} denied by <@{manager}>"

        client.chat_postMessage(
            channel=employee,
            text=text,
            blocks=[context_block]
        )

        client.chat_update(
            channel=body["container"]["channel_id"],
            ts=body["container"]["message_ts"],
            text=text,
            blocks=updated_blocks
        )
        complete_error("there is no error")
    except Exception as e:
        logger.error(e)
        complete_error("Cannot request approval")
        raise e


def get_context_block(start_date, end_date, manager):
    return {
        "type": 'context',
        "elements": [
            {
                "type": 'mrkdwn',
                "text": f":no_entry: Time-off request for _{start_date}_ :arrow_right: _{end_date}_ denied by <@{manager}>",
            },
        ],
    }
