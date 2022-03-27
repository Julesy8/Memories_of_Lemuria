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
                "gun_accessory": 1,
                "muzzle_device_9mm": 1,
                "optic": 1
                                 },
            "parts names": ["Frame",
                            "Slide",
                            "Barrel",
                            "Stock",
                            "Muzzle Device"
                            ],
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
        "Glock 17L Barrel": {
            "required parts": {
                "steel": 1,
            },
            "compatible parts": {},
            "parts names": ["Material"],
            "item": glock17.glock17l_barrel
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
        "Glock 17L Slide": {
            "required parts": {
                "steel": 1,
            },
            "compatible parts": {},
            "parts names": ["Material"],
            "item": glock17.glock17l_slide
        },
        "Glock Stock": {
            "required parts": {
                "polymer": 2,
            },
            "compatible parts": {},
            "parts names": ["Material"],
            "item": glock17.glock17_barrel
        },
        "Glock Compensator": {
            "required parts": {
                "steel": 1,
            },
            "compatible parts": {},
            "parts names": ["Material"],
            "item": glock17.glock_9mm_compensator
        },
    }
}