from logging import Logger

from slack_bolt import Ack
from slack_sdk import WebClient


def forward_message_callback(body: dict, ack: Ack, client: WebClient, logger: Logger):
    try:
        report_channel_id="GNE44K8P7"
        ack()
        msg_link = client.chat_getPermalink(
            channel=body["channel"]["id"],
            message_ts=body["message_ts"]
        )["permalink"]
        client.chat_postMessage(
            channel=report_channel_id,
            blocks=[
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"<@{body['user']['id']}> reported the following message."
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"<@{body['message']['user']}> said:"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"{body['message']['text']}"
                        }
                    },
                    {
                        "type": "context",
                        "elements": [
                            {
                                "type": "mrkdwn",
                                "text": f"Posted at: `{msg_link}`",
                            }
                        ]
                    },
                    {
                        "type": "divider"
                    }
                ])
    except Exception as e:
        logger.error(e)