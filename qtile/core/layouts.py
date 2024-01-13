from libqtile import layout
from libqtile.config import Match
from utils.color import colors

BORDER_WIDTH = 2
MARGIN = 9
SMART_GAPS = False
WINDOW_MARGIN = MARGIN
SINGLE_BORDER_WIDTH = BORDER_WIDTH
ACTIVE_COLOR = colors["magenta"]
INACTIVE_COLOR = colors["pink"]

bsp = layout.Bsp(
    border_focus=ACTIVE_COLOR,
    border_normal=INACTIVE_COLOR,
    border_width=BORDER_WIDTH,
    margin=WINDOW_MARGIN,
)

monadwide = layout.MonadWide(
    border_focus=ACTIVE_COLOR,
    border_normal=INACTIVE_COLOR,
    border_width=BORDER_WIDTH,
    margin=WINDOW_MARGIN,
    single_margin=not SMART_GAPS,
    single_border_width=SINGLE_BORDER_WIDTH,
)

monadtall = layout.MonadTall(
    border_focus=ACTIVE_COLOR,
    border_normal=INACTIVE_COLOR,
    border_width=BORDER_WIDTH,
    margin=WINDOW_MARGIN,
    single_margin=not SMART_GAPS,
    single_border_width=SINGLE_BORDER_WIDTH,
)
floating = layout.Floating(
    border_focus=colors["fg_gutter"], border_normal=colors["bg"], border_width=2
)


layouts = [bsp, monadtall, monadwide]
floating_layout = floating
