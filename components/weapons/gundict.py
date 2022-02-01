from components.weapons.glock17 import glock_17

guns_dict = {
    "Glock 17": {
        "required parts": ["glock17_frame", "glock17_slide", "glock17_barrel"],
        "compatible parts": ["glock_stock"],
        "parts names": ["Frame", "Slide", "Barrel", "Stock" ],
        "item": glock_17
    },
}