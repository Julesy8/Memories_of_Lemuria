def level_dependent_import(level):
    # This is an awful way of doing this, but I couldn't figure out a better one and I couldn't figure out how to
    # implement a switch case for importing ;(

    if level == 0:
        from colours_and_chars import level_0
        return level_0
