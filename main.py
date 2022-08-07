import traceback

import setup_game
import exceptions
import input_handlers
import colour

import tcod


def save_game(handler: input_handlers.BaseEventHandler, filename: str) -> None:
    """If the current event handler has an active Engine then save it."""
    if isinstance(handler, input_handlers.EventHandler):
        handler.engine.save_as(filename)
        print("Game saved.")


def main() -> None:

    handler: input_handlers.BaseEventHandler = setup_game.MainMenu()

    screen_width = 720
    screen_height = 480

    tileset = tcod.tileset.load_tilesheet("cp437_10x10.png", 16, 16, tcod.tileset.CHARMAP_CP437)
    with tcod.context.new(
        width=screen_width,
        height=screen_height,
        tileset=tileset,
        title="Age of Aquarius",
        renderer=tcod.RENDERER_SDL2,
        vsync=True,
    ) as context:
        console = tcod.Console(*context.recommended_console_size(), order="F")
        try:
            while True:
                console.clear()
                handler.on_render(console=console)
                context.present(console)

                try:
                    for event in tcod.event.wait():
                        if event.type == "WINDOWRESIZED":
                            console = tcod.Console(*context.recommended_console_size(), order="F")
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
            raise
        except BaseException:  # Save on any other unexpected exception.
            save_game(handler, "savegame.sav")
            raise


if __name__ == "__main__":
    main()
