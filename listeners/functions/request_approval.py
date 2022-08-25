from slack_sdk import WebClient
from slack_bolt import CompleteError
from logging import Logger

from datetime import datetime


def request_approval(event, client: WebClient, complete_error: CompleteError, logger: Logger):
    try:
        inputs = event["inputs"]
        manager = inputs["manager"]
        employee = inputs["employee"]
        end_date = datetime.fromtimestamp(inputs["end_date"]).strftime("%m/%d/%Y %H:%M")
        start_date = datetime.fromtimestamp(inputs["start_date"]).strftime("%m/%d/%Y %H:%M")

        client.chat_postMessage(
            channel=manager,
            text='A new time-off request has been submitted.',
            blocks=[
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "A new time-off request has been submitted"
                    }
                },
                {
                    "type": 'section',
                    "text": {
                        "type": 'mrkdwn',
                        "text": f"*From: * < @${employee} >",
                    },
                },
                {
                    "type": 'section',
                    "text": {
                        "type": 'mrkdwn',
                        "text": f"*Dates: * ${start_date} to ${end_date}",
                    },
                },
                {
                    "type": 'actions',
                    "block_id": 'approve-deny-buttons',
                    "elements": [
                        {
                            "type": 'button',
                            "text": {
                                "type": 'plain_text',
                                "text": 'Approve',
                            },
                            "action_id": 'approve_action_id',
                            "style": 'primary',
                        },
                        {
                            "type": 'button',
                            "text": {
                                "type": 'plain_text',
                                "text": 'Deny',
                            },
                            "action_id": 'deny_action_id',
                            "style": 'danger',
                        }
                    ]
                }
            ])

    except Exception as e:
        logger.error(e)
        complete_error("Cannot request approval")
        raise e
