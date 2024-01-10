from libqtile.config import Key
from libqtile.lazy import lazy
from utils.window import (
    move_left,
    move_right,
    move_down,
    move_up,
    normalize_window,
    resize_left,
    resize_right,
    resize_down,
    resize_up,
)

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
            lazy.layout.shuffle_left().when(layout=["monadtall", "monawide", "bsp"]),
            lazy.function(move_left).when(layout=["floating"]),
        ),
        (
            ["shift"],
            "Right",
            lazy.layout.shuffle_right().when(layout=["monadtall", "monawide", "bsp"]),
            lazy.function(move_right).when(layout=["floating"]),
        ),
        (
            ["shift"],
            "Down",
            lazy.layout.shuffle_down().when(layout=["monadtall", "monawide", "bsp"]),
            lazy.function(move_down).when(layout=["floating"]),
        ),
        (
            ["shift"],
            "Up",
            lazy.layout.shuffle_up().when(layout=["monadtall", "monawide", "bsp"]),
            lazy.function(move_up).when(layout=["floating"]),
        ),
        (
            ["control"],
            "Up",
            lazy.layout.grow().when(layout=["monadtall", "monawide"]),
            lazy.layout.grow_up().when(layout=["bsp"]),
            lazy.function(resize_up).when(layout=["floating"]),
        ),
        (
            ["control"],
            "Down",
            lazy.layout.shrink().when(layout=["monadtall", "monawide"]),
            lazy.layout.grow_down().when(layout=["bsp"]),
            lazy.function(resize_down).when(layout=["floating"]),
        ),
        (
            ["control"],
            "Left",
            lazy.layout.grow_left().when(layout=["bsp"]),
            lazy.function(resize_left).when(layout=["floating"]),
        ),
        (
            ["control"],
            "Right",
            lazy.layout.grow_right().when(layout=["bsp"]),
            lazy.function(resize_right).when(layout=["floating"]),
        ),
        (
            [mod],
            "n",
            lazy.layout.normalize().when(layout=["monadtall", "monawide", "bsp"]),
            lazy.function(normalize_window).when(layout=["floating"]),
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
