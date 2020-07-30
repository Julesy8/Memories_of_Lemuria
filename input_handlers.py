import tcod as libtcod


def handle_keys(key):
    key_char = chr(key.c)

    # Movement keys
    if key.vk == libtcod.KEY_UP or key.vk == libtcod.KEY_KP8:  # up
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN or key.vk == libtcod.KEY_KP2:  # down
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT or key.vk == libtcod.KEY_KP4:  # left
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT or key.vk == libtcod.KEY_KP6:  # right
        return {'move': (1, 0)}
    elif key_char == 'j' or key.vk == libtcod.KEY_KP7:  # up left
        return {'move': (-1, -1)}
    elif key_char == 'k' or key.vk == libtcod.KEY_KP9:  # up right
        return {'move': (1, -1)}
    elif key_char == 'n' or key.vk == libtcod.KEY_KP1:  # down left
        return {'move': (-1, 1)}
    elif key_char == 'm' or key.vk == libtcod.KEY_KP3:  # down right
        return {'move': (1, 1)}

    if key.vk == libtcod.KEY_F11:
        # enter full screen
        return {'fullscreen': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}