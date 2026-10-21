from collections.abc import Callable
from importlib import import_module
from pkgutil import walk_packages

from slack_bolt import App


class Registry:
    def __init__(self) -> None:
        self._registrations: list[Callable[[App], None]] = []

    def __getattr__(self, method: str) -> Callable[..., Callable[[Callable], Callable]]:
        if not hasattr(App, method):
            raise AttributeError(method)

        def decorator_factory(*args, **kwargs):
            def decorator(func):
                self._registrations.append(lambda app: getattr(app, method)(*args, **kwargs)(func))
                return func

            return decorator

        return decorator_factory

    def apply(self, app: App) -> None:
        for register in self._registrations:
            register(app)


registry = Registry()


def load_listeners(app: App) -> None:
    for module_info in walk_packages(__path__, f"{__name__}."):
        import_module(module_info.name)
    registry.apply(app)
