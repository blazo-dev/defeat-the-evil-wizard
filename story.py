# Function to print the intro text
from characters.character import Character
import time


def print_intro_text():
    """Prints the introductory text of the game"""
    print("\n--- The Abyssal Sea Adventure Begins! --- 🌊")
    print("A great storm is raging. The wind howls, and the waves crash against the ship. ⚓")
    print(
        "An ancient evil stirs beneath the surface, and only you can stop the Abyssal Wizard from plunging the world into darkness. 🌑")


def print_backstory():
    """Prints the backstory of the game"""
    print("\nWelcome to the world of the Abyssal Sea! 🌊")
    print(
        "A dark force threatens the balance of the seas, controlled by the Abyssal Wizard, a sorcerer who uses dark magic to summon storms and drag ships to their doom.")
    print(
        "The crew of the *Sea Wanderer* has sailed into these cursed waters, and now, only the bravest adventurers can stand against him.")


def print_battle_intro(character: Character):
    """Prints the battle introduction"""
    print("\nThe battle begins... 🏴‍☠️")
    print(
        f"\nThe evil wizard, {character.name}, stands before you, his dark magic swirling around him, threatening to consume the world! ⚡")
    print(
        "The fate of the seas and the world rests on your shoulders. Will you be the hero who vanquishes this dark sorcerer? 💥")


def display_defeat_message(player, wizard):
    """Displays a defeat message when the player is defeated."""
    print(f"\n💀 {player.name} has been defeated by {wizard.name}! The battle is lost.")
    print(f"The shadows have claimed another soul. {player.name}'s journey ends here... ⚔️")
    print("May their spirit rest in peace, as the wizard's dark reign continues. 🖤")
    time.sleep(2)


def display_victory_message(player, wizard):
    """Displays a victory message when the player defeats the wizard."""
    player.display_stats()
    print(f"\n✨ Victory! The mighty {player.name} has triumphed over {wizard.name}! 🏆")
    print(f"The darkness has been vanquished, and the world is safe once more. 🌍")
    print(f"Brave hero, your name will be sung in tales for generations to come! 🎶")
    print(f"Congratulations, {player.name}! 🎉")
    time.sleep(2)
