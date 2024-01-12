from libqtile.command import lazy

default_directions = {
    "left": (-10, 0),
    "up": (0, -10),
    "right": (10, 0),
    "down": (0, 10),
}


@lazy.function
def move(qtile, direction):
    if qtile.current_window.floating:
        qtile.current_window.cmd_move_floating(*default_directions[direction])


@lazy.function
def resize(qtile, direction):
    if qtile.current_window.floating:
        qtile.current_window.cmd_resize_floating(*default_directions[direction])
