from libqtile import qtile, widget, bar
from qtile_extras import widget
from qtile_extras.widget import decorations
from utils.color import colors
from utils.font import font, windowname
from qtile_extras.widget.decorations import PowerLineDecoration
from libqtile.config import Screen
from libqtile.bar import CALCULATED

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

spacer_logo = [
    widget.Spacer(
        length=5,
        is_spacer=True,
        inherit=True,
        use_separator=False,
        background=colors["magenta"],
    )
]

logo = [
    widget.TextBox(
        padding=6,
        font=font["clear"]["family"],
        fontsize=font["clear"]["fontsize"],
        text="󰨑",
        background=colors["magenta"],
        foreground=colors["fg"],
        **powerline,
    ),
]

layout = [
    widget.CurrentLayout(
        **fontinfo,
        background=colors["pink"],
        **powerline,
    ),
]

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
window = [
    widget.WindowName(
        font=windowname,
        fontsize=16,
        format="{name}",
        max_chars=60,
        widht=CALCULATED,
        background=colors["fg_gutter"],
        center_aligned=True,
        **powerline,
    ),
]

clock = [
    widget.Clock(
        **fontinfo,
        format="%I:%M %p ",
        background=colors["blue"],
        **powerline,
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
