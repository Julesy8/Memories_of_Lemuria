class Impossible(Exception):
    """Exception raised when an action is impossible to be performed.

    The reason is given as the exception message.
    """
class GameOver(Exception):
    """show game over screen"""

class QuitToMenu(Exception):
    """quit game to menu"""

class QuitToMenuWithoutSaving(Exception):
    """quit game to menu without creating a save file"""

class QuitWithoutSaving(SystemExit):
    """Can be raised to exit the game without automatically saving."""
