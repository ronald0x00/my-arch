from libqtile.config import DropDown, Group, Key, ScratchPad
from libqtile.lazy import lazy
from core.keys import mod, keys

groups = [Group(f"{i+1}", label="󰱺") for i in range(6)]


for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                ["mod1"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown("term", "kitty", width=0.4, height=0.5, x=0.3, y=0.1, opacity=1),
        ],
    )
)

keys.extend(
    [
        Key(["control"], "1", lazy.group["scratchpad"].dropdown_toggle("term")),
    ]
)
