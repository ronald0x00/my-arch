from libqtile import layout
from utils.color import colors

BORDER_WIDTH = 2
MARGIN = 9
SMART_GAPS = False
WINDOW_MARGIN = MARGIN
SINGLE_BORDER_WIDTH = BORDER_WIDTH
ACTIVE_COLOR = colors["magenta"]
INACTIVE_COLOR = colors["pink"]

floating = layout.Floating(
    border_focus=ACTIVE_COLOR, border_normal=INACTIVE_COLOR, border_width=2
)
tile = layout.Tile(
    border_width=BORDER_WIDTH,
    margin=WINDOW_MARGIN,
    margin_on_single=not SMART_GAPS,
    border_focus=ACTIVE_COLOR,
    border_normal=INACTIVE_COLOR,
    expand=True,
    border_on_single=True,
    ratio=0.5,
    ratio_increment=0.01,
    shift_windows=True,
    master_length=1,
    add_after_last=True,
)

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
layouts = [tile, bsp, monadwide, monadtall]
