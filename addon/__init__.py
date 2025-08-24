from . import preferences
from . import operators
from . import panel
from . import keymap
from . import translate


modules = [preferences, operators, panel, keymap, translate]


def register():
    for module in modules:
        module.register()


def unregister():
    for module in modules:
        module.unregister()
