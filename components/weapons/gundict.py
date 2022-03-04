import components.weapons.glock17 as glock17

guns_dict = {
    "pistols": {
        "Glock 17": {
            "required parts": {
                "glock17_frame": 1,
                "glock17_slide": 1,
                "glock17_barrel": 1,
                               },
            "compatible parts": {
                "glock_stock": 1,
                                 },
            "parts names": ["Frame", "Slide", "Barrel", "Stock"],
            "item": glock17.glock_17
        },
    }
}

gun_parts_dict = {
    "Glock Parts": {
        "Glock 17 Barrel": {
            "required parts": {
                "steel": 1,
                            },
            "compatible parts": {},
            "parts names": ["Material"],
            "item": glock17.glock17_barrel
        },
        "Glock 17 Frame": {
            "required parts": {
                "polymer": 1,
            },
            "compatible parts": {},
            "parts names": ["Material"],
            "item": glock17.glock17_frame
        },
        "Glock 17 Slide": {
            "required parts": {
                "steel": 1,
            },
            "compatible parts": {},
            "parts names": ["Material"],
            "item": glock17.glock17_slide
        },
        "Glock Stock": {
            "required parts": {
                "polymer": 2,
            },
            "compatible parts": {},
            "parts names": ["Material"],
            "item": glock17.glock17_barrel
        },
    }
}