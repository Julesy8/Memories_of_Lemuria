import traceback
from configparser import ConfigParser
from multiprocessing import active_children, freeze_support
import exceptions
import input_handlers
import colour

import tcod
import tcod.sdl.video

# pyinstaller -F -i "new_icon.ico" main.py

freeze_support()

config = ConfigParser()
config.read('settings.ini')

font = config.get('settings', 'font')
maximize_window_on_start = config.getboolean('settings', 'maximize_window_on_start')
fullscreen_on_start = config.getboolean('settings', 'fullscreen_on_start')
font_char_width = config.getint('settings', 'font_char_width')
font_char_height = config.getint('settings', 'font_char_height')
screen_pix_width = config.getint('settings', 'screen_pix_width')
screen_pix_height = config.getint('settings', 'screen_pix_height')


def toggle_maximized(context: tcod.context.Context) -> None:
    """Toggle a context window between fullscreen and windowed modes."""
    window = context.sdl_window
    if not window:
        return
    window.maximize()


def toggle_fullscreen(context: tcod.context.Context) -> None:
    """Toggle a context window between fullscreen and windowed modes."""
    if not context.sdl_window_p:
        return
    fullscreen = tcod.lib.SDL_GetWindowFlags(context.sdl_window_p) & (
            tcod.lib.SDL_WINDOW_FULLSCREEN | tcod.lib.SDL_WINDOW_FULLSCREEN_DESKTOP
    )
    tcod.lib.SDL_SetWindowFullscreen(
        context.sdl_window_p,
        0 if fullscreen else tcod.lib.SDL_WINDOW_FULLSCREEN_DESKTOP,
    )


def save_game(handler: input_handlers.BaseEventHandler, filename: str) -> None:
    """If the current event handler has an active Engine then save it."""
    if isinstance(handler, input_handlers.EventHandler):
        handler.engine.save_as(filename)
        print("Game saved.")


def main() -> None:
    handler: input_handlers.BaseEventHandler = input_handlers.MainMenu()

    screen_width = screen_pix_width
    screen_height = screen_pix_height

    tileset = tcod.tileset.load_tilesheet(font, font_char_width, font_char_height, tcod.tileset.CHARMAP_CP437)
    with tcod.context.new(
            width=screen_width,
            height=screen_height,
            tileset=tileset,
            title="Memories of Lemuria",
            renderer=tcod.RENDERER_SDL2,
            vsync=True,
    ) as context:
        console = tcod.Console(*context.recommended_console_size(), order="F")
        if maximize_window_on_start:
            toggle_maximized(context)
        if fullscreen_on_start:
            toggle_fullscreen(context)
        try:
            while True:
                console.clear()
                handler.on_render(console=console)
                context.present(console)

                try:
                    for event in tcod.event.wait():
                        if event.type == "WINDOWRESIZED":
                            console = tcod.Console(*context.recommended_console_size(), order="F")

                        try:
                            if event.sym == tcod.event.K_F11 and not event.repeat:
                                if isinstance(event, tcod.event.KeyDown):
                                    toggle_fullscreen(context=context)
                        except AttributeError:
                            pass

                        context.convert_event(event)
                        handler = handler.handle_events(event)

                except Exception:  # Handle exceptions in game.
                    traceback.print_exc()  # Print error to stderr.
                    # Then print the error to the message log.
                    if isinstance(handler, input_handlers.EventHandler):
                        handler.engine.message_log.add_message(
                            traceback.format_exc(), colour.RED
                        )
        except exceptions.QuitWithoutSaving:
            raise
        except SystemExit:  # Save and quit.
            save_game(handler, "savegame.sav")
            for child in active_children():
                child.kill()
            raise
        except BaseException:  # Save on any other unexpected exception.
            save_game(handler, "savegame.sav")
            raise


if __name__ == "__main__":
    main()
