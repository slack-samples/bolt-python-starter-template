import sys
from pkgutil import walk_packages

import listeners


class TestLoadListeners:
    def test_imports_every_listener_module(self):
        for module_info in walk_packages(listeners.__path__, f"{listeners.__name__}."):
            assert module_info.name in sys.modules

    def test_registers_every_listener_on_the_injected_app(self):
        assert len(listeners.app._listeners) == 6
