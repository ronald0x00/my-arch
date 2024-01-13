from core import hooks
from utils.font import font
from core.groups import groups
from core.keys import keys
from core.layouts import floating_layout, layouts
from core.mouse import mouse
from core.bar import screens

widget_defaults = dict(
    **font["clear"],
)

extension_defaults = widget_defaults.copy()


__all__ = [
    "extension_defaults",
    "floating_layout",
    "groups",
    "hooks",
    "keys",
    "layouts",
    "mouse",
    "screens",
    "widget_defaults",
]
