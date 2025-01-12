# Function to print the intro text
from characters.character import Character


# Function to print the introductory text of the game
def print_intro_text():
    print("\n--- The Abyssal Sea Adventure Begins! --- 🌊")
    print("A great storm is raging. The wind howls, and the waves crash against the ship. ⚓")
    print(
        "An ancient evil stirs beneath the surface, and only you can stop the Abyssal Wizard from plunging the world into darkness. 🌑")


# Function to print the backstory of the game
def print_backstory():
    print("\nWelcome to the world of the Abyssal Sea! 🌊")
    print(
        "A dark force threatens the balance of the seas, controlled by the Abyssal Wizard, a sorcerer who uses dark magic to summon storms and drag ships to their doom.")
    print(
        "The crew of the *Sea Wanderer* has sailed into these cursed waters, and now, only the bravest adventurers can stand against him.")


# Function to print the battle introduction
def print_battle_intro(character: Character):
    print("\nThe battle begins... 🏴‍☠️")
    print(
        f"\nThe evil wizard, {character.name}, stands before you, his dark magic swirling around him, threatening to consume the world! ⚡")
    print(
        "The fate of the seas and the world rests on your shoulders. Will you be the hero who vanquishes this dark sorcerer? 💥")
