def move_left(qtile):
    return qtile.current_window.move_floating(-100, 0)


def move_right(qtile):
    return qtile.current_window.move_floating(100, 0)


def move_down(qtile):
    return qtile.current_window.move_floating(0, 100)


def move_up(qtile):
    return qtile.current_window.move_floating(0, -100)


def normalize_window(qtile):
    return qtile.current_window.set_size_floating(1000, 1000)
