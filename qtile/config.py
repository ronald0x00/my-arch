from typing import List  # noqa: F401
import os
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from keys import keys, mod
from font import font
from layouts import custom_layouts, floating
from bar import init_screens

# terminal = guess_terminal()
terminal = "kitty"

float_types = ["dialog"]

float_names = [
    "Calculator",
    "Bluetooth Devices",
    "Network Connections",
    "Color Picker",
    "Steam Guard - Computer Authorization Required",
]

# @hook.subscribe.client_new
# def float_to_front(qtile):
#    """
#    Bring all floating windows of the group to front
#    """
#    for window in qtile.currentGroup.windows:
#        if window.floating:
#            window.cmd_bring_to_front()


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
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
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


# groups = [ Group(f"{i+1}", label="♥") for i in range(5)]
groups = [Group(f"{i+1}", label="󰱺") for i in range(6)]


for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = custom_layouts
floating_layout = floating

widget_defaults = dict(
    **font["clear"],
)

extension_defaults = widget_defaults.copy()

screens = init_screens()

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# wmname = "LG3D"
wmname = "qtile"
