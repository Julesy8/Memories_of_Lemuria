import components.weapons.glock17 as glock17

guns_dict = {
    "pistols": {
        "Glock 17": {
            "required parts": ["glock17_frame", "glock17_slide", "glock17_barrel"],
            "compatible parts": ["glock_stock"],
            "parts names": ["Frame", "Slide", "Barrel", "Stock"],
            "item": glock17.glock_17
        },
    }
}

gun_parts_dict = {
    "Glock Parts": {
        "Glock 17 Barrel": {
            "required parts": ["material"],
            "compatible parts": [],
            "parts names": ["Material"],
            "item": glock17.glock_17
        },
    }
}