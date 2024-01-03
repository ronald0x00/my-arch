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
        ([mod], "t", lazy.spawn("kitty")),
        ([], "Print", lazy.spawn("xfce4-screenshooter")),
        ([], "F11", lazy.window.toggle_fullscreen()),
        ([mod], "r", lazy.restart()),
        ([mod], "q", lazy.shutdown()),
    ]
]
