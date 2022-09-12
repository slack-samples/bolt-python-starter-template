import os
import logging

from slack_sdk import WebClient
from slack_bolt import Complete, Ack


def sample_view(event, client: WebClient, complete: Complete, logger: logging.Logger):
    try:
        interactivity_pointer = event["inputs"]["interactivity.interactivity_pointer"]
        client.views_open(
            interactivity_pointer=interactivity_pointer,
            trigger_id=None,
            view={
                "type": "modal",
                "callback_id": "func_sample_view_id",
                "title": {"type": "plain_text", "text": "Sample modal title"},
                "blocks": [
                    {
                        "type": "input",
                        "block_id": "input_block_id",
                        "label": {
                            "type": "plain_text",
                            "text": "What are your hopes and dreams?",
                        },
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "sample_input_id",
                            "multiline": True,
                        },
                    },
                ],
                "submit": {"type": "plain_text", "text": "Submit"},
                "notify_on_close": True,
            },
        )
    except Exception as e:
        logger.error(e)
        complete(error="Cannot create view")
        raise e


def sample_view_submission(ack: Ack, view, complete: Complete, logger: logging.Logger):
    try:
        ack()
        message = view["state"]["values"]["input_block_id"]["sample_input_id"]["value"]
        complete(outputs={"markdown": f":wave: You submitted the following message: \n\n>{message}"})
    except Exception as e:
        logger.error(e)
        complete(error="Cannot submit form")
        raise e


def sample_view_closed(ack: Ack, complete: Complete, logger: logging.Logger):
    try:
        ack()
        complete(outputs={"markdown": f"You closed the form"})
    except Exception as e:
        logger.error(e)
        complete(error="Cannot close form")
        raise e
