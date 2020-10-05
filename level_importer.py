"""
This is an awful way of doing this, but I couldn't figure out a better one and I couldn't figure out how to
implement a switch case for importing ;( but it should still be faster than importing every the colours and
characters for every single level when more are added
"""


def level_dependent_import(level):  # imports the tiles and characters for a given level
    if level == 0:
        from colours_and_chars import level_0
        return level_0
