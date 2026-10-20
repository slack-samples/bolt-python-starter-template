import os
from importlib import import_module
from pkgutil import walk_packages

from slack_bolt import App

app = App(token=os.environ.get("SLACK_BOT_TOKEN"), token_verification_enabled=False)


def load_listeners() -> None:
    for module_info in walk_packages(__path__, f"{__name__}."):
        import_module(module_info.name)
