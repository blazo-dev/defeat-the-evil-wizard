import time
from story import print_intro_text, print_backstory
from character import select_character
from characters.evil_wizard import EvilWizard
from battle import battle


def main():
    print_intro_text()
    time.sleep(1)
    print_backstory()
    time.sleep(1)
    player = select_character()
    wizard = EvilWizard("Vornath, the Doom Bringer")
    battle(player, wizard)


if __name__ == "__main__":
    main()
