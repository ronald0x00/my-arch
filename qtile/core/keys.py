from libqtile.config import Key
from libqtile.lazy import lazy
from utils.window import resize, move, normalize

mod = "mod4"
terminal = "kitty"

keys = [
    Key(*key)
    for key in [
        # Switch between windows
        ([mod], "h", lazy.layout.left()),
        ([mod], "l", lazy.layout.right()),
        ([mod], "j", lazy.layout.down()),
        ([mod], "k", lazy.layout.up()),
        (
            # Move window (tiling/floating) to left
            ["shift"],
            "Left",
            lazy.layout.shuffle_left().when(layout=["monadtall", "monadwide", "bsp"]),
            move("left"),
        ),
        (
            # Move window (tiling/floating) to right
            ["shift"],
            "Right",
            lazy.layout.shuffle_right().when(layout=["monadtall", "monadwide", "bsp"]),
            move("right"),
        ),
        (
            # Move window (tiling/floating) to down
            ["shift"],
            "Down",
            lazy.layout.shuffle_down().when(layout=["monadtall", "monadwide", "bsp"]),
            move("down"),
        ),
        (
            # Move window (tiling/floating) to up
            ["shift"],
            "Up",
            lazy.layout.shuffle_up().when(layout=["monadtall", "monadwide", "bsp"]),
            move("up"),
        ),

        (

            # Increase/decrease window (tiling/floating) to left
            ["control"],
            "Left",
            lazy.layout.grow_left().when(layout=["bsp"]),
            resize("left"),
        ),
        (
            # Increase/decrease window (tiling/floating) to right
            ["control"],
            "Right",
            lazy.layout.grow_right().when(layout=["bsp"]),
            resize("right"),
        ),

        (

            # Increase/decrease window (tiling/floating) to down
            ["control"],
            "Down",
            lazy.layout.grow_down().when(layout=["bsp"]),
            lazy.layout.shrink().when(layout=["monadtall", "monadwide"]),
            resize("down"),
        ),
        (
            # Increase/decrease window (tiling/floating) to up
            ["control"],
            "Up",
            lazy.layout.grow_up().when(layout=["bsp"]),
            lazy.layout.grow().when(layout=["monadtall", "monadwide"]),
            resize("up"),
        ),
        (
                # normalize window (tiling/floating)
            [mod],
            "n",
            lazy.layout.normalize().when(layout=["monadtall", "monadwide", "bsp"]),
            normalize(),
        ),
        # Utils keybindings
        ([], "Print", lazy.spawn("xfce4-screenshooter")),
        ([mod], "t", lazy.spawn(terminal)),
        ([], "F11", lazy.window.toggle_fullscreen()),
        ([mod], "f", lazy.window.toggle_floating()),
        # Utils keys to qtile
        ([mod], "r", lazy.restart()),
        ([mod], "q", lazy.shutdown()),
        ([mod, "control"], "b", lazy.hide_show_bar()),
    ]
]
