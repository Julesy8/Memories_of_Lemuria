import traceback
from configparser import ConfigParser
from multiprocessing import active_children, freeze_support
import exceptions
import input_handlers
from setup_game import MainMenu
import colour
import statistics
import time
from collections import deque
from typing import Deque, Optional

import tcod
import tcod.sdl.video

# pyinstaller -F -i "mol48.ico" main.py

# to profile run times:
# python -m cProfile main.py > cprofile_output.txt
# kernprof -l -v main.py

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
max_fps = config.getint('settings', 'max_fps')


class Clock:
    # https://github.com/libtcod/python-tcod/blob/main/examples/framerate.py
    """Measure framerate performance and sync to a given framerate.

    Everything important is handled by `Clock.sync`.  You can use the fps
    properties to track the performance of an application.
    """

    def __init__(self) -> None:
        """Initialize this object with empty data."""
        self.last_time = time.perf_counter()  # Last time this was synced.
        self.time_samples: Deque[float] = deque()  # Delta time samples.
        self.max_samples = 64  # Number of fps samples to log.  Can be changed.
        self.drift_time = 0.0  # Tracks how much the last frame was overshot.

    def sync(self, fps: Optional[float] = None) -> float:
        """Sync to a given framerate and return the delta time.

        `fps` is the desired framerate in frames-per-second.  If None is given
        then this function will track the time and framerate without waiting.

        `fps` must be above zero when given.
        """
        if fps is not None:
            # Wait until a target time based on the last time and framerate.
            desired_frame_time = 1 / fps
            target_time = self.last_time + desired_frame_time - self.drift_time
            # Sleep might take slightly longer than asked.
            sleep_time = max(0, target_time - self.last_time - 0.001)
            if sleep_time:
                time.sleep(sleep_time)
            # Busy wait until the target_time is reached.
            while (drift_time := time.perf_counter() - target_time) < 0:
                pass
            self.drift_time = min(drift_time, desired_frame_time)

        # Get the delta time.
        current_time = time.perf_counter()
        delta_time = max(0, current_time - self.last_time)
        self.last_time = current_time

        # Record the performance of the current frame.
        self.time_samples.append(delta_time)
        while len(self.time_samples) > self.max_samples:
            self.time_samples.popleft()

        return delta_time

    @property
    def min_fps(self) -> float:
        """The FPS of the slowest frame."""
        try:
            return 1 / max(self.time_samples)
        except (ValueError, ZeroDivisionError):
            return 0

    @property
    def max_fps(self) -> float:
        """The FPS of the fastest frame."""
        try:
            return 1 / min(self.time_samples)
        except (ValueError, ZeroDivisionError):
            return 0

    @property
    def mean_fps(self) -> float:
        """The FPS of the sampled frames overall."""
        if not self.time_samples:
            return 0
        try:
            return 1 / statistics.fmean(self.time_samples)
        except ZeroDivisionError:
            return 0

    @property
    def median_fps(self) -> float:
        """The FPS of the median frame."""
        if not self.time_samples:
            return 0
        try:
            return 1 / statistics.median(self.time_samples)
        except ZeroDivisionError:
            return 0

    @property
    def last_fps(self) -> float:
        """The FPS of the most recent frame."""
        if not self.time_samples or self.time_samples[-1] == 0:
            return 0
        return 1 / self.time_samples[-1]


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
    handler: input_handlers.BaseEventHandler = MainMenu()

    screen_width = screen_pix_width
    screen_height = screen_pix_height

    tileset = tcod.tileset.load_tilesheet(font, font_char_width, font_char_height, tcod.tileset.CHARMAP_CP437)
    with tcod.context.new(
            width=screen_width,
            height=screen_height,
            tileset=tileset,
            title="Memories of Lemuria",
            renderer=tcod.RENDERER_SDL2,
            vsync=False,
    ) as context:
        clock = Clock()
        console = tcod.Console(*context.recommended_console_size(), order="F")
        if maximize_window_on_start:
            toggle_maximized(context)
        if fullscreen_on_start:
            toggle_fullscreen(context)
        try:
            while True:
                console.clear()
                handler.on_render(console=console)
                context.present(console, keep_aspect=True, integer_scaling=True)
                clock.sync(fps=max_fps)

                try:
                    for event in tcod.event.get():
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
                except exceptions.QuitToMenu:
                    save_game(handler, "savegame.sav")
                    handler = MainMenu()
                except exceptions.QuitToMenuWithoutSaving:
                    handler = MainMenu()
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
            try:
                handler.engine.squad_mode = False
            except AttributeError:
                pass
            save_game(handler, "savegame.sav")
            for child in active_children():
                child.kill()
            raise
        except BaseException:  # Save on any other unexpected exception.
            save_game(handler, "savegame.sav")
            raise


if __name__ == "__main__":
    main()
