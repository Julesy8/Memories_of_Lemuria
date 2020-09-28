import tcod as libtcod


def render_all(con, entities, fov_map, fov_recompute, game_map, screen_width, screen_height, camera):
    # Draw all the tiles in the game map
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible = libtcod.map_is_in_fov(fov_map, x, y)

                x_in_camera, y_in_camera = camera.apply(x, y)
                # If the tile is within players FOV, draws tile with light colours, if outside FOV and has been
                # explored, draws dark colours. If neither, draws 
                if visible:
                    libtcod.console_put_char_ex(con, x_in_camera, y_in_camera, game_map.tiles[x][y].char,
                                                game_map.tiles[x][y].fg_colour,
                                                game_map.tiles[x][y].bg_colour)
                    game_map.tiles[x][y].explored = True

                elif game_map.tiles[x][y].explored:
                    libtcod.console_put_char_ex(con, x_in_camera, y_in_camera, game_map.tiles[x][y].char,
                                                game_map.tiles[x][y].fg_colour_dark,
                                                game_map.tiles[x][y].bg_colour_dark)

    # Draw all entities in the list
    for entity in entities:
        draw_entity(con, entity, fov_map, camera)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity, fov_map, camera):
    if libtcod.map_is_in_fov(fov_map, entity.x, entity.y):
        x, y = camera.apply(entity.x, entity.y)
        libtcod.console_set_default_foreground(con, entity.fg_colour)
        libtcod.console_put_char(con, x, y, entity.char, entity.bg_colour)


def clear_entity(con, entity):
    # erase the character that represents this object
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)
