from libqtile import hook
import os
import subprocess


float_types = ["dialog"]

float_names = [
    "Calculator",
    "Bluetooth Devices",
    "Network Connections",
    "Color Picker",
    "Steam Guard - Computer Authorization Required",
]


@hook.subscribe.client_new
def browser(c):
    if c.window.get_wm_class() == ("chromium", "Chromium"):
        c.togroup(c.qtile.current_group.name)


@hook.subscribe.float_change
@hook.subscribe.client_new
@hook.subscribe.client_focus
def set_hint(window):
    window.window.set_property(
        "QTILE_FLOATING", str(window.floating), type="STRING", format=8
    )


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/utils/autostart.sh")
    subprocess.run([home])


@hook.subscribe.client_new
def dialogs(window):
    """Floating dialog"""
    if (
        window.name in float_names
        or window.window.get_wm_type() in float_types
        or window.window.get_wm_transient_for()
    ):
        window.floating = True
