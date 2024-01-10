from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"
terminal = "kitty"

keys = [
    Key(*key)
    for key in [
        ([mod], "h", lazy.layout.left()),
        ([mod], "l", lazy.layout.right()),
        ([mod], "j", lazy.layout.down()),
        ([mod], "k", lazy.layout.up()),
        (["shift"], "Left", lazy.layout.shuffle_left()),
        (["shift"], "Right", lazy.layout.shuffle_right()),
        (["shift"], "Up", lazy.layout.shuffle_up()),
        (["shift"], "Down", lazy.layout.shuffle_down()),
        (
            ["control"],
            "Up",
            lazy.layout.grow().when(layout=["monadtall", "monawide"]),
            lazy.layout.grow_up().when(layout=["bsp"]),
        ),
        (
            ["control"],
            "Down",
            lazy.layout.shrink().when(layout=["monadtall", "monawide"]),
            lazy.layout.grow_down().when(layout=["bsp"]),
        ),
        (["control"], "Left", lazy.layout.grow_left().when(layout=["bsp"])),
        (["control"], "Right", lazy.layout.grow_right().when(layout=["bsp"])),
        ([], "Print", lazy.spawn("xfce4-screenshooter")),
        ([mod], "t", lazy.spawn(terminal)),
        ([], "F11", lazy.window.toggle_fullscreen()),
        ([mod], "space", lazy.window.toggle_floating()),
        ([mod], "r", lazy.restart()),
        ([mod], "q", lazy.shutdown()),
        ([mod, "control"], "b", lazy.hide_show_bar()),
    ]
]
