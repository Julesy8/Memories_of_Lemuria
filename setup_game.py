"""Handle the loading and initialization of game sessions."""
from __future__ import annotations

import lzma
import pickle

import colour
from engine import Engine
from entity import Actor
from level_generator import MessyBSPTree
from level_parameters import level_params
from components.inventory import Inventory
from components.ai import BaseAI
from components.npc_templates import GunFighter
from components.bodyparts import Body, Arm, Leg, Head
from random import choice

from copy import deepcopy

from components.weapons.glock17 import glock_17

from components.weapons.glock17 import glock17_frame, glock17_barrel, glock17_slide, glock17_slide_optic, \
    glock_switch, glock_9mm_compensator, glock_stock, glock_pic_rail, suppressor_surefire_9mm

# for crafting testing
from pydantic.utils import deep_update
from components.weapons.glock17 import glock17dict

#from components.weapons.mosin import mosin_stock, mosin_archangel_stock, mosin_carbine_stock, mosin_obrez_stock, \
#    mosin_barrel, mosin_carbine_barrel, mosin_obrez_barrel, mosin_pic_scope_mount, \
#    mosin_magazine_conversion, mosin_suppressor, mosin_muzzlebreak, mosin_nagant


def new_game() -> Engine:
    """Return a brand new game session as an Engine instance."""
    current_level = 1

    # initialises player entity
    fighter_component = GunFighter(unarmed_meat_damage=10, unarmed_armour_damage=5)

    Head_part = Head(hp=40, protection_ballistic=50, protection_physical=50, depth=20, width=20, height=26)
    Body_part = Body(hp=100, protection_ballistic=50, protection_physical=50, depth=20, width=35, height=56)
    R_Arm = Arm(hp=70, protection_ballistic=50, protection_physical=50, name='right arm', depth=10, width=10, height=78)
    L_Arm = Arm(hp=70, protection_ballistic=50, protection_physical=50, name='left arm', depth=10, width=10, height=78)
    R_Leg = Leg(hp=75, protection_ballistic=50, protection_physical=50, name='right leg', depth=12, width=15,
                height=100)
    L_Leg = Leg(hp=75, protection_ballistic=50, protection_physical=50, name='left leg', depth=12, width=15, height=100)

    # Head_part = Head(hp=40, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=26)
    # Body_part = Body(hp=100, protection_ballistic=0, protection_physical=0, depth=20, width=35, height=56)
    # R_Arm = Arm(hp=70, protection_ballistic=0, protection_physical=0, name='right arm', depth=10, width=10, height=78)
    # L_Arm = Arm(hp=70, protection_ballistic=0, protection_physical=0, name='left arm', depth=10, width=10, height=78)
    # R_Leg = Leg(hp=75, protection_ballistic=0, protection_physical=0, name='right leg', depth=12, width=15,
    #             height=100)
    # L_Leg = Leg(hp=75, protection_ballistic=0, protection_physical=0, name='left leg', depth=12, width=15, height=100)

    body_parts = (Body_part, Head_part, R_Arm, L_Arm, R_Leg, L_Leg)

    player = Actor(0,
                   0,
                   '@',
                   colour.GREEN,
                   'Player',
                   ai=BaseAI,
                   fighter=fighter_component,
                   bodyparts=body_parts,
                   player=True,
                   inventory=Inventory(capacity=15),
                   )

    engine = Engine(player=player, current_level=current_level, current_floor=0)

    #inventory_items = [mac1045,]

    #inventory_items = [glock_17, glock17_frame, glock17_barrel, glock17_slide, glock17_slide_optic,
    #                   glock_switch, glock_9mm_compensator, glock_stock, glock_pic_rail, suppressor_surefire_9mm]

    inventory_items = [glock_17, glock17_frame, glock17_barrel, glock17_slide_optic,
                       glock_switch, glock_9mm_compensator, glock_stock, glock_pic_rail, suppressor_surefire_9mm]

    engine.crafting_recipes = deep_update(engine.crafting_recipes, glock17dict)

    #inventory_items = [glock17_frame, glock17_barrel, glock17l_barrel,
    #                   glock17_barrel_ported, glock17l_barrel_ported, glock17_slide, glock17l_slide,
    #                   glock17_slide_custom, glock17l_slide_custom,
    #                   glock_switch, glock_9mm_compensator, glock_stock, glock_pic_rail, glock_pistol_brace]

    #inventory_items = [mosin_stock, mosin_archangel_stock, mosin_carbine_stock, mosin_obrez_stock,
    #                   mosin_barrel, mosin_carbine_barrel, mosin_obrez_barrel, mosin_pic_scope_mount,
    #                   mosin_magazine_conversion, mosin_suppressor, mosin_muzzlebreak]

    #inventory_items = [mac1045_lower, mac1045_upper, mac1045_upper_tactical, mac1045_upper_max,mac1045_barrel,
    #                   mac1045_extended_barrel, mac1045_carbine_barrel, mac10_full_stock, mac10_folding_stock,
    #                   mac1045_sionics_suppressor, mac109_max_barrel, mac1045_max_barrel, mac10_vertical_grip]

    for item in inventory_items:
        itemcopy = deepcopy(item)
        player.inventory.items.append(itemcopy)
        itemcopy.parent = player.inventory

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
                                   ).generateLevel()

    engine.game_map.camera_xy = (engine.player.x, engine.player.y)

    engine.update_fov()

    # engine.message_log.add_message(
    #     "You lose your footing and fall deep into the caverns below... You can't see any way to get back to the surface"
    #     , colour.LIGHT_MAGENTA
    # )

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
                     'Reptilian', 'Lovecraftian', 'Biblical', 'Heretical', 'Heterodox', 'Theological', 'Religious',
                     'Cursed', 'Hegelian', 'Occult', 'Banned', 'Experimental', 'Reviled', '"Fictional"', 'CIA',
                     'Timeless', 'Theoretical', 'Runic', 'Spiritual', 'Soulful', 'Historical', 'Symbolic',
                     'Intuitive', 'Weaponized', 'Primal', 'Subconscious', 'Arthurian', 'Goetic', 'Wagnerian',
                     'Tantric'))

    verb_2 = choice(('Deep Underground', 'Technical', 'Cyphercore', 'Advanced', 'Modern', 'Ancient', 'Post-Modern',
                     'Extreme', 'Sinister', 'Gothic', 'Revolutionary', 'Reactionary', 'Officially Licensed',
                     'Subversive', 'Covert', 'Magik', 'Chaos Magic', 'Solar', 'Lunar', 'Ideological', 'Cyclic',
                     'Meditative', 'Divine', 'Tactical', 'Forbidden', 'Psychedelic', 'Quantum', 'Etheric',
                     'Post-Industrial', 'Post-Fall', 'Hollow Earth', 'Pre-Modern', 'Introductory', 'Ritual',
                     'Cautionary', 'Transcendental', 'Chaotic', 'Perennial', 'Secret', 'Revisionist', 'Pseudo',
                     'Military', 'Sensory', 'Planetary', 'Radical', 'Chakra', 'Compassionate', 'Archaic', 'Arcane',
                     'Lawful', 'Royal', 'Sacrificial', 'Cubic', 'Elite', 'Satirical', 'Polemical'))

    verb_3 = choice(('Combat', 'Gun Smithing', 'UFO-ology', 'Warfare', 'Conspiracy', 'CQC', 'Harm Prevention',
                     'Self Defense', 'Horror', 'Action', 'Time-War', 'Numerology', 'Sacred Geometry',
                     'Ultra Violence', 'Tulpamancy', 'Astral Projection', 'Psychic', 'Englightenment', 'Gun Fu',
                     'Gunplay', 'Brainwashing', 'Martial Arts', 'Hand Loading', 'Gun Design', 'Physics',
                     'Firearms Safety', 'Gun Collection', 'Ballistics', 'Gun Customization', 'Gun Building',
                     'Demonology', 'Virtual Reality', 'Lucid Dreaming', 'Remote Viewing', 'Folklore', 'Exorcism',
                     'Manifestation', 'Alien Abduction', 'Shape Shifting', 'Witchcraft', 'Predictive Programming',
                     'Terrorism', 'Mythology', 'Chemtrails'))

    noun = choice(('Computer Role Playing Game', 'Simulation', 'Training Module', 'Course', 'Engine',
                   'RPG', 'Rogue Like', 'Rogue Lite', 'Program', 'Center', 'Game', 'Experience', 'Proof-of-Concept',
                   'Videogame Adaptation', 'Demonstration', 'Tutorial', 'Simulator', '(DO NOT RESEARCH)', 'LARP',
                   'Survival Game', 'Shooter', '-Hack Like', 'Documentary', 'Temple', 'Metaphor', 'Parable',
                   'Oracle', 'Thing', 'Infohazard', 'Psyop', 'Manual', 'Vision', 'Project', 'Transcript',
                   'In Silico', 'Matrix', 'Frequency', 'Glossary', 'Algorithm', 'Host', 'Gateway'))

    subtext_str = f"{verb_1} {verb_2} {verb_3} {noun}"
    return subtext_str

