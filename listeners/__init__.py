from importlib import import_module
from pkgutil import walk_packages

from slack_bolt import App

app: App


def load_listeners(bolt_app: App) -> None:
    global app
    app = bolt_app
    for module_info in walk_packages(__path__, f"{__name__}."):
        import_module(module_info.name)
