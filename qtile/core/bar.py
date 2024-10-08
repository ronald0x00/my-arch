from libqtile import qtile, widget, bar
from qtile_extras import widget
from qtile_extras.widget import decorations
from utils.color import colors
from utils.font import font, windowname
from qtile_extras.widget.decorations import PowerLineDecoration
from libqtile.config import Screen
from libqtile.bar import CALCULATED
import subprocess

fontinfo = dict(
    font=font["secondary"]["family"],
    padding=font["secondary"]["padding"],
    fontsize=font["secondary"]["fontsize"],
)

DEFAULT_FG = colors["fg"]
DEFAULT_BG = colors["bg"]
WIDTH = 34

powerline = {
    "decorations": [PowerLineDecoration(path="forward_slash")],
}


center_spacer = [
    widget.Spacer(
        length=bar.STRETCH,
        is_spacer=True,
        inheirit=True,
        use_separator=False,
        background=colors["fg_gutter"],
        **powerline,
    ),
]

large_spacer = [
    widget.Spacer(
        length=bar.STRETCH,
        is_spacer=True,
        inheirit=True,
        use_separator=False,
        background=colors["fg_gutter"],
        **powerline,
    ),
]

spacer_minimal = [
    widget.Spacer(
        length=10,
        is_spacer=True,
        inherit=True,
        use_separator=True,
        background=colors["fg_gutter"],
    )
]

spacer_power = [
    widget.Spacer(
        length=5,
        is_spacer=True,
        inherit=True,
        use_separator=False,
        background=colors["red"],
    )
]

spacer_logo = [
    widget.Spacer(
        length=5,
        is_spacer=True,
        inherit=True,
        use_separator=False,
        background=colors["magenta"],
    )
]
groups = [
    widget.GroupBox(
        font=font["clear"]["family"],
        padding=font["clear"]["padding"],
        fontsize=font["clear"]["fontsize"],
        foreground=colors["cyan"],
        highlight_method="text",
        block_highlight_text_color=colors["white"],
        active=colors["magenta"],
        inactive=colors["cyan"],
        rounded=False,
        highlight_color=[colors["fg"], colors["yellow"]],
        urgent_alert_method="line",
        urgent_text=colors["red"],
        urgent_border=colors["red"],
        disable_drag=True,
        use_mouse_wheel=False,
        hide_unused=False,
        spacing=5,
        this_current_screen_border=colors["pink"],
        **powerline,
    )
]

logo = [
    widget.TextBox(
        padding=-1,
        font=font["clear"]["family"],
        fontsize=font["clear"]["fontsize"],
        text=" 󰌠 ",
        background=colors["magenta"],
        foreground=colors["fg"],
        **powerline,
    ),
]

power = [
    widget.TextBox(
        padding=-1,
        font=font["clear"]["family"],
        fontsize=font["clear"]["fontsize"],
        text="  󰀥",
        background=colors["red"],
        foreground=colors["fg"],
        **powerline,
    ),
]
layout = [
    widget.CurrentLayout(
        **fontinfo,
        background=colors["pink"],
        fmt="󰕘  {}",
        **powerline,
    ),
]
window = [
    widget.WindowName(
        font=windowname,
        fontsize=16,
        format="{name}",
        max_chars=20,
        widht=CALCULATED,
        background=colors["fg_gutter"],
        center_aligned=True,
        **powerline,
    ),
]

clock = [
    widget.Clock(
        **fontinfo,
        format="%d %B | %H:%M",
        background=colors["blue"],
        **powerline,
    ),
]

box = [
    widget.WidgetBox(
        font=font["clear"]["family"],
        fontsize=font["clear"]["fontsize"],
        background=colors["fg_gutter"],
        text_open="󰎟",
        text_closed="󰌼",
        **powerline,
        widgets=[
            widget.Systray(
                **fontinfo,
                background=colors["cyan"],
                foreground=colors["fg"],
                theme_path="rose-pine-gtk",
                **powerline,
            ),
            widget.TextBox(
                **fontinfo,
                background=colors["black"],
                foreground=colors["fg"],
                text="󰬬",
                **powerline,
            ),
            widget.CheckUpdates(
                **fontinfo,
                distro="Arch",
                display_format="{updates} updates",
                no_update_string="No updates",
                background=colors["black"],
                foreground=colors["fg"],
                **powerline,
            ),
            widget.GenPollText(
                **fontinfo,
                update_interval=1,
                func=lambda: subprocess.check_output(
                    "$HOME/.config/qtile/scripts/vpn.sh", shell=True
                ).decode("utf-8"),
                background=colors["pink"],
                foreground=colors["fg"],
                **powerline,
            ),
            widget.Net(
                **fontinfo,
                format="󰚷 {up:6.2f} | {down:6.2f} 󰚶",
                background=colors["magenta"],
                foreground=colors["fg"],
                prefix="k",
                **powerline,
            ),
            widget.Memory(
                **fontinfo,
                format=" 󰘚 {MemUsed:.0f}{mm}",
                background=colors["green"],
                foreground=colors["fg"],
                **powerline,
            ),
            widget.CPU(
                **fontinfo,
                format=" 󰍛 {load_percent:.0f}%",
                background=colors["blue"],
                foreground=colors["fg"],
                **powerline,
            ),
        ],
    ),
]


widgets = lambda: [
    *spacer_logo,
    *logo,
    *groups,
    *layout,
    *spacer_minimal,
    *window,
    *center_spacer,
    *clock,
    *large_spacer,
    *box,
    *power,
    *spacer_power,
]


screens = [
    Screen(
        wallpaper="~/bepop.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            widgets=widgets(),
            size=WIDTH,
            foreground=DEFAULT_FG,
            background=DEFAULT_BG,
            opacity=1.0,
        ),
    ),
]
