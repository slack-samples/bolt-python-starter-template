def sample_message_callback(context, client, say, logger):
    try:
        greeting = context['matches'][0]
        say(f"{greeting}, how are you?")
    except Exception as e:
        logger.error(e)