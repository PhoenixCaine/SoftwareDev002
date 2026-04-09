import os
from pyfiglet import Figlet


def titleScreen():
    MAGENTA = "\033[95m"
    RESET = "\033[0m"

    os.system('cls' if os.name == 'nt' else 'clear')


    f = Figlet(font="ansi_shadow")

    ascii_title = f.renderText("MAGIC MAZE")

    print(MAGENTA + ascii_title + RESET)

    print(MAGENTA + "               M I N D   Y O U R   O W N   M A Z E" + RESET)

    input("Press ENTER to begin...")



if __name__ == "__main__":
    titleScreen()
