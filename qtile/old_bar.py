from libqtile import qtile, widget, bar
from libqtile.lazy import lazy
from font import font, windowname
from color import colors
from layouts import MARGIN, BORDER_WIDTH
import os
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

CENTER_SPACERS = 100

fontinfo = dict(
    font=font["secondary"]["family"],
    padding=font["secondary"]["padding"],
    fontsize=font["secondary"]["fontsize"],
)

DEFAULT_FG = colors["fg"]
DEFAULT_BG = colors["bg"]
WIDTH = 34


def launcher(qtile):
    lazy.spawn("sh " + os.path.expanduser("~/.scripts/rofi-launchpad.sh"))


groupbox = [
    widget.GroupBox,
    {
        "font": font["clear"]["family"],
        "padding": font["clear"]["padding"],
        "fontsize": font["clear"]["fontsize"],
        "foreground": colors["cyan"],
        "highlight_method": "text",
        "block_highlight_text_color": colors["white"],
        "active": colors["magenta"],
        "inactive": colors["cyan"],
        "rounded": False,
        "highlight_color": [colors["fg"], colors["yellow"]],
        "urgent_alert_method": "line",
        "urgent_text": colors["red"],
        "urgent_border": colors["red"],
        "disable_drag": True,
        "use_mouse_wheel": False,
        "hide_unused": False,
        "spacing": 5,
        "this_current_screen_border": colors["pink"],
    },
]


windowname = [
    widget.WindowName,
    {
        "font": windowname,
        "fontsize": 16,
        "padding": 3,
        "format": "{name}",
        "background": colors["fg_gutter"],
        "center_aligned": True,
    },
]
#
# systray = [
#     widget.Systray,
#     {
#         "background": colors["orange"],
#         "foreground": colors["black"],
#         "theme_path": "rose-pine-gtk",
#     },
# ]
#
spacer_small = [
    widget.Spacer,
    {
        "length": 5,
        # these values are used by style func, not qtile
        "is_spacer": True,
        "inheirit": True,
        "use_separator": False,
    },
]
spacer_medium = [
    widget.Spacer,
    {
        "length": bar.STRETCH,
        "is_spacer": True,
        "inheirit": True,
        "use_separator": False,
        "background": colors["fg_gutter"],
    },
]
#
#
logo = [
    widget.TextBox,
    {
        # text="  ",
        # "font": "Font Awesome 6 Brands",
        "padding": 6,
        "font": font["clear"]["family"],
        "fontsize": font["clear"]["fontsize"],
        "text": "󰨑",
        "background": colors["magenta"],
        "foreground": colors["fg"],
        "mouse_callbacks": {
            "Button1": lazy.spawn(
                "sh " + os.path.expanduser("~/.scripts/rofi-launchpad.sh")
            )
        },
    },
]
#
#
layout = [
    widget.CurrentLayout,
    {
        **fontinfo,
        "background": colors["pink"],
    },
]
time = [
    widget.Clock,
    {
        **fontinfo,
        "format": "%I:%M %p ",
        "background": colors["blue"],
    },
]


def widgetlist():
    return [
        spacer_small,
        logo,
        groupbox,
        layout,
        spacer_medium,
        windowname,
        time,
    ]


def style(widgetlist):
    # adds separator widgets in between the initial widget list
    styled = widgetlist[:]

    for index, wid in enumerate(widgetlist):
        end_sep = {
            "font": "Iosevka Nerd Font",
            "text": "",
            "fontsize": WIDTH,
            "padding": -1,
        }

        if index < len(widgetlist) - 1:
            # end_sep["background"]=widgetlist[index+1][1].get("background", DEFAULT_BG)
            # end_sep["foreground"]=wid[1].get("background", DEFAULT_BG)

            end_sep["foreground"] = widgetlist[index + 1][1].get(
                "background", DEFAULT_BG
            )
            end_sep["background"] = wid[1].get("background", DEFAULT_BG)
            if wid[1].get("is_spacer") and wid[1].get("inheirit"):
                bg = widgetlist[index + 1][1].get("background", DEFAULT_BG)
                wid[1]["background"] = bg
                end_sep["background"] = bg
            # insert separator before current
            if wid[1].get("use_separator", True):
                styled.insert(styled.index(wid) + 1, (widget.TextBox, end_sep))

    return [w[0](**w[1]) for w in styled]


def my_bar():
    return bar.Bar(
        [*style(widgetlist())],
        WIDTH,
        foreground=DEFAULT_FG,
        background=DEFAULT_BG,
        opacity=1.0,
    )
