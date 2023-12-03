from colorama import init as colorama_init
from colorama.ansi import Cursor, clear_line
from colorama import Fore
import keyboard

colorama_init()


class CTermMenu:

    def __init__(self, options: list[str] = None):
        self.__options = options
        self.__selected = 0
        self.__is_choice = False
