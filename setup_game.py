"""Handle the loading and initialization of game sessions."""
from __future__ import annotations

import lzma
import pickle
from random import randint, choices
from playsound import playsound
from typing import Optional
from configparser import ConfigParser
import numpy as np
import traceback
from multiprocessing import Process
import tcod

from engine import Engine
from level_generator import MessyBSPTree
from input_handlers import BaseEventHandler, MainGameEventHandler, PopupMessage
from level_parameters import level_params
from colour import LIGHT_MAGENTA
from player_generator import generate_player
from random import choice
from components.weapons.bullets import round_9mm_124_jhp

# for crafting testing
# from pydantic.utils import deep_update
# from components.weapons.glock17 import glock17dict

# from components.weapons.mosin import mosin_stock, mosin_archangel_stock, mosin_carbine_stock, mosin_obrez_stock, \
#    mosin_barrel, mosin_carbine_barrel, mosin_obrez_barrel, mosin_pic_scope_mount, \
#    mosin_magazine_conversion, mosin_suppressor, mosin_muzzlebreak, mosin_nagant

config = ConfigParser()
config.read('settings.ini')

music = config.getboolean('settings', 'music')


def playmusic():
    while True:
        playsound('stepinside.mp3')


class MainMenu(BaseEventHandler):
    """Handle the main menu rendering and input."""

    def __init__(self):
        self.option_selected = 0
        self.colour_mode_forward = [True, True, True]
        self.fg_colour = [randint(60, 249), randint(60, 249), randint(60, 249)]
        self.subtext = generate_subtext()

        self.music = None

        if music:
            self.music = Process(target=playmusic)
            self.music.start()

    def change_fg_colour(self):

        for i in range(3):
            reverse_direction = choices(population=(True, False), weights=(1, 600))[0]

            if self.colour_mode_forward[i - 1]:
                if reverse_direction:
                    self.colour_mode_forward[i - 1] = False
                else:
                    self.fg_colour[i - 1] += 1
                    if self.fg_colour[i - 1] >= 250:
                        self.colour_mode_forward[i - 1] = False

            else:
                if reverse_direction:
                    self.colour_mode_forward[i - 1] = True
                else:
                    self.fg_colour[i - 1] -= 1
                    if self.fg_colour[i - 1] <= 25:
                        self.colour_mode_forward[i - 1] = True

    def on_render(self, console: tcod.Console) -> None:
        """Render the main menu on a background image."""

        path = "newmenu1.xp"  # REXPaint file with one layer.
        path_ak = "akonly.xp"
        # Load a REXPaint file with a single layer.
        # The comma after console is used to unpack a single item tuple.
        console3, = tcod.console.load_xp(path_ak, order="F")
        console2, = tcod.console.load_xp(path, order="F")

        # Convert tcod's Code Page 437 character mapping into a NumPy array.
        CP437_TO_UNICODE = np.asarray(tcod.tileset.CHARMAP_CP437)

        # Convert from REXPaint's CP437 encoding to Unicode in-place.
        console3.ch[:] = CP437_TO_UNICODE[console3.ch]
        console2.ch[:] = CP437_TO_UNICODE[console2.ch]

        # Apply REXPaint's alpha key color.
        KEY_COLOR = (255, 0, 255)
        is_transparent = (console2.rgb["bg"] == KEY_COLOR).all(axis=2)
        is_transparent_3 = (console3.rgb["bg"] == KEY_COLOR).all(axis=2)
        console2.rgba[is_transparent] = (ord(" "), (0,), (0,))
        console3.rgba[is_transparent_3] = (ord(" "), (0,), (0,))

        self.change_fg_colour()
        console2.rgb["fg"] = self.fg_colour

        console3.blit(dest=console, dest_x=console.width // 2 - 43, dest_y=console.height // 2 - 31, src_x=0, src_y=0,
                      width=86,
                      height=52)

        console2.blit(dest=console, dest_x=console.width // 2 - 40, dest_y=console.height // 2 - 25, src_x=0, src_y=0,
                      width=86,
                      height=52)

        # noinspection PyTypeChecker
        console.print(
            console.width // 2,
            console.height // 2 + 19,
            self.subtext,
            fg=self.fg_colour,
            alignment=tcod.CENTER,
        )

        menu_width = 8
        for i, text in enumerate(
                ["New Game", "Continue", "  Quit"]
        ):
            # noinspection PyTypeChecker
            console.print(
                console.width // 2,
                console.height // 2 - 1 + i,
                text.ljust(menu_width),
                fg=self.fg_colour,
                alignment=tcod.CENTER,
                bg_blend=tcod.BKGND_ALPHA(64),
            )

        # noinspection PyTypeChecker
        console.print(x=console.width // 2 - 6, y=console.height // 2 - 1 + self.option_selected, string='►',
                      fg=self.fg_colour)

        # noinspection PyTypeChecker
        console.print(x=console.width // 2 + 5, y=console.height // 2 - 1 + self.option_selected, string='◄',
                      fg=self.fg_colour)

        # noinspection PyTypeChecker
        console.print(x=console.width // 2 - 6, y=console.height // 2 + 22,
                      string='Version 0.00',
                      fg=self.fg_colour)

        if music:
            # noinspection PyTypeChecker
            console.print(x=console.width // 2 - 26, y=console.height // 2 + 23,
                          string='Music by Blavatsky -- https://blavatsky.bandcamp.com',
                          fg=self.fg_colour)

    def ev_keydown(
            self, event: tcod.event.KeyDown
    ) -> Optional[BaseEventHandler]:
        # if event.sym == tcod.event.K_ESCAPE:
        #     if music:
        #         self.music.terminate()
        #     raise SystemExit()

        if event.sym == tcod.event.K_DOWN:
            if self.option_selected < 2:
                self.option_selected += 1
            else:
                self.option_selected = 0

        elif event.sym == tcod.event.K_UP:
            if self.option_selected > 0:
                self.option_selected -= 1
            else:
                self.option_selected = 2

        elif event.sym == tcod.event.K_F1:
            self.subtext = generate_subtext()

        elif event.sym == tcod.event.K_RETURN:
            # new game
            if self.option_selected == 0:
                if music:
                    self.music.terminate()
                return MainGameEventHandler(new_game())
            # continue game
            elif self.option_selected == 1:
                try:
                    # TODO show message here warning player that current save will be overwritten
                    if self.music is not None:
                        self.music.terminate()
                    return MainGameEventHandler(load_game("savegame.sav"))
                except FileNotFoundError:
                    return PopupMessage(self, "No saved game to load.", title='Error')
                except Exception as exc:
                    traceback.print_exc()  # Print to stderr.
                    return PopupMessage(self, f"Failed to load save:\n{exc}", title='Error')
                pass
            elif self.option_selected == 2:
                if music:
                    self.music.terminate()
                raise SystemExit()

        return None


def new_game() -> Engine:
    """Return a brand new game session as an Engine instance."""

    current_level = 0

    player_1 = generate_player(current_level=0, players=[])

    player_2 = generate_player(current_level=0, players=[player_1])

    engine = Engine(player_1)

    bullets = round_9mm_124_jhp
    bullets.stacking.stack_size = 50

    # inventory_items = [glock17_frame, glock17_barrel,
    #                    glock_switch, glock17_slide, glock_mag_9mm, bullets]

    # engine.crafting_recipes = deep_update(engine.crafting_recipes, glock17dict)

    # inventory_items = [glock17_frame, glock17_barrel, glock17l_barrel,
    #                   glock17_barrel_ported, glock17l_barrel_ported, glock17_slide, glock17l_slide,
    #                   glock17_slide_custom, glock17l_slide_custom,
    #                   glock_switch, glock_9mm_compensator, glock_stock, glock_pic_rail, glock_pistol_brace]

    # inventory_items = [mosin_stock, mosin_archangel_stock, mosin_carbine_stock, mosin_obrez_stock,
    #                   mosin_barrel, mosin_carbine_barrel, mosin_obrez_barrel, mosin_pic_scope_mount,
    #                   mosin_magazine_conversion, mosin_suppressor, mosin_muzzlebreak]

    # inventory_items = [mac1045_lower, mac1045_upper, mac1045_upper_tactical, mac1045_upper_max,mac1045_barrel,
    #                   mac1045_extended_barrel, mac1045_carbine_barrel, mac10_full_stock, mac10_folding_stock,
    #                   mac1045_sionics_suppressor, mac109_max_barrel, mac1045_max_barrel, mac10_vertical_grip]

    # for item in inventory_items:
    #     itemcopy = deepcopy(item)
    #     player_1.inventory.items.append(itemcopy)
    #     itemcopy.parent = player_1.inventory
    #
    #     itemcopy = deepcopy(item)
    #     player_2.inventory.items.append(itemcopy)
    #     itemcopy.parent = player_2.inventory

    engine.players.append(player_2)

    engine.game_map = MessyBSPTree(messy_tunnels=level_params[current_level][0],
                                   map_width=level_params[current_level][1],
                                   map_height=level_params[current_level][2],
                                   max_leaf_size=level_params[current_level][3],
                                   room_max_size=level_params[current_level][4],
                                   room_min_size=level_params[current_level][5],
                                   max_items_per_room=level_params[current_level][6],
                                   fov_radius=level_params[current_level][7],
                                   engine=engine,
                                   current_level=current_level,
                                   min_caverns=level_params[current_level][8],
                                   max_caverns=level_params[current_level][9],
                                   cavern_size=level_params[current_level][10],
                                   custom_room_chance=level_params[current_level][11],
                                   enclose_room_chance=level_params[current_level][12]
                                   ).generate_level()

    engine.game_map.camera_xy = (engine.player.x, engine.player.y + 3)

    engine.message_log.add_message(
        "The country has been taken over by extraterrestrial forces and their occultist supporters. Mission: destroy "
        "the underground military base!"
        , LIGHT_MAGENTA
    )

    engine.update_fov()

    return engine


def load_game(filename: str) -> Engine:
    """Load an Engine instance from a file."""
    with open(filename, "rb") as f:
        engine = pickle.loads(lzma.decompress(f.read()))
    assert isinstance(engine, Engine)
    return engine


def generate_subtext() -> str:
    verb_1 = choice(('Aquarian', 'New-Age', 'Postdiluvian', 'Cosmic', 'Mystical', 'Esoteric',
                     'Dialectical', 'Demiurgic', 'Sublime', 'Hyper-Realistic', 'Platonic', 'MK-Ultra', 'Illegal',
                     'Post-Apocalyptic', 'Morally Ambiguous', 'Atlantean', 'New World Order',
                     'Harmonic', 'Universal', 'Post-Structural', 'Archetypal', 'Scientific', 'Haunted', 'Absurdist',
                     'Philosophical', 'Angelic', 'Paranormal', 'Shamanic', 'Vampiric', 'Cryptic', 'Jungian',
                     'Reptilian', 'Lovecraftian', 'Biblical', 'Heretical', 'Heterodox', 'Theological',
                     'Cursed', 'Hegelian', 'Occult', 'Banned', 'Experimental', 'Reviled', '"Fictional"', 'CIA',
                     'Timeless', 'Theoretical', 'Runic', 'Spiritual', 'Soulful', 'Historical', 'Symbolic',
                     'Intuitive', 'Weaponized', 'Primal', 'Subconscious', 'Arthurian', 'Goetic', 'Wagnerian',
                     'Taoist', 'Dharmic', 'Practical', 'Factual', 'Numinous', 'Life-Affirming', 'Nocturnal',
                     'Ascendant', 'High Vibration', 'Malevolent', 'Benevolent', 'Blessed', 'Holy', 'Evil',
                     'Mysterious', 'Beloved', 'Romantic', 'Devious', 'Illuminati', 'Majestic', 'Sickening', 'Literal',
                     'Spooky', 'Undead', 'Criminal', 'Hyperborean', 'Forgotten', 'Perrenial', 'Latent', 'Final',
                     'Continental', 'Nihilistic', 'Eastern', 'Western', 'Sentient', 'Tragic', 'Melancholic',
                     'Infernal', 'Serbian', 'Misanthropic', 'Luminous', 'Extraterrestrial', 'Promethean',
                     'Controversial', 'Poetic', 'Intoxicated', 'Toxic'))

    verb_2 = choice(('Underground', 'Technical', 'Cyphercore', 'Advanced', 'Modern', 'Ancient', 'Post-Modern',
                     'Extreme', 'Sinister', 'Gothic', 'Revolutionary', 'Reactionary', 'Officially Licensed',
                     'Subversive', 'Covert', 'Magik', 'Chaos Magic', 'Solar', 'Lunar', 'Ideological', 'Cyclic',
                     'Meditative', 'Divine', 'Tactical', 'Forbidden', 'Psychedelic', 'Quantum', 'Etheric',
                     'Post-Industrial', 'Post-Fall', 'Hollow Earth', 'Pre-Modern', 'Introductory', 'Ritual',
                     'Cautionary', 'Transcendental', 'Chaotic', 'Perennial', 'Secret', 'Revisionist', 'Pseudo',
                     'Military', 'Sensory', 'Planetary', 'Radical', 'Chakra', 'Compassionate', 'Archaic', 'Arcane',
                     'Lawful', 'Royal', 'Sacrificial', 'Cubic', 'Elite', 'Satirical', 'Polemical', 'Sci-Fi',
                     'Fantasy', 'Post-Truth', 'Federal', 'Biographical', 'Reanimated', 'Existential', 'Paranoid',
                     'Psychic', 'Enlightenment', 'Cancelled'))

    verb_3 = choice(('Combat', 'Gun Smithing', 'UFO-ology', 'Warfare', 'Conspiracy', 'CQC', 'Harm Prevention',
                     'Self Defense', 'Horror', 'Action', 'Time-War', 'Numerology', 'Sacred Geometry',
                     'Ultra Violence', 'Tulpamancy', 'Astral Projection', 'Englightenment', 'Gun Fu',
                     'Gunplay', 'Brainwashing', 'Martial Arts', 'Hand Loading', 'Gun Design', 'Physics',
                     'Firearms Safety', 'Gun Collection', 'Ballistics', 'Gun Customization', 'Gun Building',
                     'Demonology', 'Virtual Reality', 'Lucid Dreaming', 'Remote Viewing', 'Folklore', 'Exorcism',
                     'Manifestation', 'Alien Abduction', 'Shape Shifting', 'Witchcraft', 'Predictive Programming',
                     'Terrorism', 'Mythology', 'Chemtrails', 'Worship', 'Science', 'Necromancy', 'Gangstalking',
                     'Block Chain', 'Finance', 'Arson', 'Therapy',
                     'Robbery', 'Kabbalah',
                     ))

    noun = choice(('Computer Role Playing Game', 'Simulation', 'Training Module', 'Course', 'Engine',
                   'RPG', 'Rogue Like', 'Program', 'Center', 'Game', 'Experience',
                   'Videogame Adaptation', 'Demonstration', 'Tutorial', 'Simulator', '(DO NOT RESEARCH)', 'LARP',
                   'Shooter', 'Documentary', 'Temple', 'Metaphor', 'Parable',
                   'Oracle', 'Thing', 'Infohazard', 'Psyop', 'Manual', 'Vision', 'Project', 'Transcript',
                   'In Silico', 'Matrix', 'Frequency', 'Glossary', 'Algorithm', 'Host', 'Gateway', 'Sigil', 'Nexion',
                   'Network', 'Hallucination', 'Found Footage', 'Religion', 'Trap', 'Computer',
                   'Operating System', 'Forum', 'Image Board', 'Online', 'Cabal', 'Prophecy', 'Machine', 'Life Style',
                   'Pathogen', 'Tome', 'The Movie', 'Artifact', 'Dictionary', 'For Dummies', 'System',
                   'Society'
                   ))

    subtext_str = f"{verb_1} {verb_2} {verb_3} {noun}"
    return subtext_str
