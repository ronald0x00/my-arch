from libqtile.config import Group, Key, Match, DropDown, ScratchPad
from libqtile.lazy import lazy
from core.keys import keys, mod

groups = [
    Group(
        "1",
        label="󰫈",
        matches=[
            Match(wm_class="kitty"),
        ],
        layout="None",
    ),
    Group(
        "2",
        label="󰫈",
        matches=[
            Match(wm_class="nvim"),
        ],
        layout="max",
    ),
    Group(
        "3",
        label="󰫈",
        matches=[
            Match(wm_class="firefox"),
        ],
        layout="max",
    ),
    Group(
        "4",
        label="󰫈",
        matches=[
            Match(wm_class="discord"),
            Match(wm_class="telegram-desktop"),
        ],
        layout="max",
    ),
    Group(
        "5",
        label="󰫈",
        matches=[
            Match(wm_class="spotify"),
        ],
        layout="max",
    ),
    Group(
        "6",
        label="󰫈",
        layout="None",
    ),
]
for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group{i.name}",
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc=f"move focused window to group{i.name}",
            ),
        ]
    )
    groups.append(
        ScratchPad(
            "scratchpad",
            [
                DropDown(
                    "term", "kitty", width=0.4, height=0.5, x=0.3, y=0.1, opacity=1
                ),
            ],
        )
    )
