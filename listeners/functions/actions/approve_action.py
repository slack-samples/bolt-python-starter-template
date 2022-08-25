from datetime import datetime
from logging import Logger

from slack_bolt import Ack, Say, CompleteError


def approve_action(ack: Ack, say: Say, body, complete_error: CompleteError, logger: Logger):
    try:
        ack()
        inputs = body["function_data"]["inputs"]
        manager = inputs["manager"]
        end_date = datetime.fromtimestamp(inputs["end_date"]*1000.0).strptime("%m/%d/%Y %H:%M")
        start_date = datetime.fromtimestamp(inputs["start_date"]*1000.0).strptime("%m/%d/%Y %H:%M")
        say(
            text=f":white_check_mark: Time-off request for ${start_date} to ${end_date} approved by <@${manager}>",
            blocks=[
                {
                    "type": 'context',
                    "elements": [
                        {
                            "type": 'mrkdwn',
                            "text": f":white_check_mark: Time-off request for ${start_date} to ${end_date} approved by <@${manager}>",
                        },
                    ],
                }
            ]
        )
        complete_error("there is no error")
    except Exception as e:
        logger.error(e)
        complete_error("Cannot request approval")
        raise e
