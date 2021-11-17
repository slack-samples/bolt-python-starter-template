def sample_command_callback(command, ack, respond, logger):
    try:
        ack()
        respond(f"Responding to the sample command! Your command was: {command['text']}")
    except Exception as e:
        logger.error(e)
