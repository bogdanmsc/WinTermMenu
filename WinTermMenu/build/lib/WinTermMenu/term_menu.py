from colorama import init as colorama_init          # for initialization
from colorama.ansi import Cursor, clear_line        # to delete some lines in cmd
from colorama import Fore                           # to change the color in cmd
import keyboard                                     # to track keystrokes

colorama_init()


class CTermMenu:

    def __init__(self,
                 options: list[str] = None,
                 symbol: str = '><'):
        self.__options = options
        self.__selected = 0
        self.__is_choice = False
        self.__symbol = symbol

    @property
    def options(self):
        return self.__options

    @options.setter
    def options(self, new_options: list[str]):
        self.__options = new_options

    def show(self):
        for i, option in enumerate(self.__options):
            if i == self.__selected:
                print(Fore.GREEN + f' {self.__symbol[0]} {option} {self.__symbol[1]} ')
            else:
                print(Fore.CYAN + f'   {option}   ')

    def get_value(self):
        while not self.__is_choice:

            for i in range(len(self.__options)):
                print(Cursor.UP(1),
                      end=clear_line(),
                      flush=True)

            self.show()
            event = keyboard.read_event()

            if event.name == 'up' and event.event_type == 'up':
                if (self.__selected - 1) < 0:
                    self.__selected = len(self.__options) - 1
                else:
                    self.__selected -= 1

            elif event.name == 'down' and event.event_type == 'up':
                if (self.__selected + 1) > len(self.__options) - 1:
                    self.__selected = 0
                else:
                    self.__selected += 1

            elif event.name == 'enter' and event.event_type == 'up':
                self.__is_choice = True
                return self.__selected
