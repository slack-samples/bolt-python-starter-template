import os


def pytest_configure():
    os.environ["SLACK_BOT_TOKEN"] = "test-bot-token"
