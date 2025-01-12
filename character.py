from characters.warrior import Warrior
from characters.mage import Mage
from characters.archer import Archer
from characters.paladin import Paladin
import time
from menus import show_class_menu


def create_character(character_choice: str, name: str):
    character_map = {
        '1': (Warrior, f"Ah, {name}, the mighty Warrior! ⚔️ You are a force of nature!"),
        '2': (Mage, f"Ah, {name}, the wise Mage! 🧙‍♂️ You possess the power of the arcane!"),
        '3': (Archer, f"Ah, {name}, the skilled Archer! 🏹 Your arrows never miss their mark!"),
        '4': (Paladin, f"Ah, {name}, the noble Paladin! ✨ Your faith in the light is unyielding!"),
    }
    character_class, character_message = character_map.get(character_choice,
                                                           (Warrior, "Invalid choice. Defaulting to Warrior. ⚔️"))
    print(f"\n{character_message}")
    time.sleep(2)
    return character_class(name)


def select_character():
    show_class_menu()
    class_choice = input("Enter the number of your class choice 📝: ")
    name = input("Enter your character's name 🦸: ")
    return create_character(class_choice, name)
