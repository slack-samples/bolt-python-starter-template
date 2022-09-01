from slack_sdk import WebClient
from slack_bolt import Complete, Ack
from logging import Logger


APPROVE_ID = "approve_action_id"
DENY_ID = "deny_action_id"


def approve_me(event, client: WebClient, complete: Complete, logger: Logger):
    try:
        client.chat_postMessage(
            channel=event["inputs"]["channel"],
            text='Approve me please',
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                    	"text": "*Approve me please* :wink:"
                    }
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
                            "action_id": APPROVE_ID,
                            "style": 'primary',
                        },
                        {
                            "type": 'button',
                            "text": {
                                "type": 'plain_text',
                                "text": 'Deny',
                            },
                            "action_id": DENY_ID,
                            "style": 'danger',
                        }
                    ]
                }
            ])
    except Exception as e:
        logger.error(e)
        complete(error="Cannot request approval")
        raise e


def approve_action(ack: Ack, client: WebClient, body, complete: Complete, logger: Logger):
    try:
        ack()
        blocks = body["message"]["blocks"][:-1]
        blocks.append(_get_context_block(":white_check_mark: I have been approved"))
        client.chat_update(
            channel=body["container"]["channel_id"],
            ts=body["container"]["message_ts"],
            text="I have been approved",
            blocks=blocks
        )
        complete()
    except Exception as e:
        logger.error(e)
        complete(error="Cannot request approval")
        raise e


def deny_action(ack: Ack, client: WebClient, body, complete: Complete, logger: Logger):
    try:
        ack()
        blocks = body["message"]["blocks"][:-1]
        blocks.append(_get_context_block(":no_entry: I have been denied"))
        client.chat_update(
            channel=body["container"]["channel_id"],
            ts=body["container"]["message_ts"],
            text="I have been denied",
            blocks=blocks
        )
        complete()
    except Exception as e:
        logger.error(e)
        complete(error="Cannot request approval")
        raise e


def _get_context_block(mrkdwn):
    return {
        "type": 'context',
        "elements": [
                {
                    "type": 'mrkdwn',
                    "text": mrkdwn,
                },
        ],
    }
