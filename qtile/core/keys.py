from libqtile.config import Key
from libqtile.lazy import lazy
from utils.window import resize, move, normalize

mod = "mod4"
terminal = "kitty"

keys = [
    Key(*key)
    for key in [
        ([mod], "h", lazy.layout.left()),
        ([mod], "l", lazy.layout.right()),
        ([mod], "j", lazy.layout.down()),
        ([mod], "k", lazy.layout.up()),
        (
            ["shift"],
            "Left",
            lazy.layout.shuffle_left().when(layout=["monadtall", "monadwide", "bsp"]),
            move("left"),
        ),
        (
            ["shift"],
            "Right",
            lazy.layout.shuffle_right().when(layout=["monadtall", "monadwide", "bsp"]),
            move("right"),
        ),
        (
            ["shift"],
            "Down",
            lazy.layout.shuffle_down().when(layout=["monadtall", "monadwide", "bsp"]),
            move("down"),
        ),
        (
            ["shift"],
            "Up",
            lazy.layout.shuffle_up().when(layout=["monadtall", "monadwide", "bsp"]),
            move("up"),
        ),
        (
            ["control"],
            "Up",
            lazy.layout.grow_up().when(layout=["bsp"]),
            lazy.layout.grow().when(layout=["monadtall", "monadwide"]),
            resize("up"),
        ),
        (
            ["control"],
            "Down",
            lazy.layout.grow_down().when(layout=["bsp"]),
            lazy.layout.shrink().when(layout=["monadtall", "monadwide"]),
            resize("down"),
        ),
        (
            ["control"],
            "Left",
            lazy.layout.grow_left().when(layout=["bsp"]),
            resize("left"),
        ),
        (
            ["control"],
            "Right",
            lazy.layout.grow_right().when(layout=["bsp"]),
            resize("right"),
        ),
        (
            [mod],
            "n",
            lazy.layout.normalize().when(layout=["monadtall", "monadwide", "bsp"]),
            normalize(),
        ),
        ([], "Print", lazy.spawn("xfce4-screenshooter")),
        ([mod], "t", lazy.spawn(terminal)),
        ([], "F11", lazy.window.toggle_fullscreen()),
        ([mod], "space", lazy.window.toggle_floating()),
        ([mod], "r", lazy.restart()),
        ([mod], "q", lazy.shutdown()),
        ([mod, "control"], "b", lazy.hide_show_bar()),
    ]
]
