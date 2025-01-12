import time

# game.py
from archer import Archer
from paladin import Paladin
from story import print_backstory, print_battle_intro, print_intro_text
from warrior import Warrior
from mage import Mage
from evil_wizard import EvilWizard


# Function to display a character class selection menu
def show_class_menu():
    print("\nChoose your character class 🛡️: ")
    print("1. Warrior ⚔️")
    print("2. Mage 🧙‍♂️")
    print("3. Archer 🏹")
    print("4. Paladin ✨")


# Function to display a battle action selection menu
def show_battle_menu():
    print("""
╔═══════════════════════════════════════════╗
       🏴‍☠️ Your Turn, Brave Hero! 🕹️         
╚═══════════════════════════════════════════╝
1. ⚔️ Attack
2. ✨ Use Special Ability
3. 💖 Heal
4. 📊 View Stats
""")
    time.sleep(1)
    choice = input("Choose an action 🔽: ")
    return choice


# Function to handle character creation based on user input
def select_character():
    show_class_menu()

    class_choice = input("Enter the number of your class choice 📝: ")
    name = input("Enter your character's name 🦸: ")

    return create_character(class_choice, name)


def create_character(character_choice: str, name: str):
    # Define a dictionary with character choice as the key and the class & character_message as the value
    character_map = {
        '1': (Warrior, f"Ah, {name}, the mighty Warrior! ⚔️ You are a force of nature!"),
        '2': (Mage, f"Ah, {name}, the wise Mage! 🧙‍♂️ You possess the power of the arcane!"),
        '3': (Archer, f"Ah, {name}, the skilled Archer! 🏹 Your arrows never miss their mark!"),
        '4': (Paladin, f"Ah, {name}, the noble Paladin! ✨ Your faith in the light is unyielding!"),
    }

    # Handle the choice using the dictionary, defaulting to Warrior if the choice is invalid
    character_class, character_message = character_map.get(character_choice,
                                                           (Warrior, f"Invalid choice. Defaulting to Warrior. ⚔️"))

    print(f"\n{character_message}")
    time.sleep(2)  # Pause for a dramatic effect before returning the character
    return character_class(name)


def handle_player_action(choice, player, wizard):
    if choice == '1':
        print(f"\n{player.name} readies their weapon for the attack! ⚔️")
        time.sleep(1)
        player.attack(wizard)
    elif choice == '2':
        print(f"\n{player.name} is preparing to use their special ability... ✨")
        time.sleep(1)
        # Call the special ability here
        pass  # Implement this logic later
    elif choice == '3':
        print(f"\n{player.name} takes a deep breath and prepares to heal... 💖")
        time.sleep(1)
        player.heal()
    elif choice == '4':
        print(f"\n{player.name} checks their stats... 📊")
        time.sleep(1)
        player.display_stats()
    else:
        print(
            "\n🚫 That action is not recognized, brave hero! \n✨ Choose wisely, for the fate of the world depends on you! \n⚔️ Let's try again and fight with honor!")

        raise KeyError("Invalid option. Please try again. 🚫")


# Battle function with a user menu for actions
def battle(player, wizard):
    print_battle_intro(wizard)

    while wizard.health > 0 and player.health > 0:
        try:
            choice = show_battle_menu()
            handle_player_action(choice, player, wizard)

            # Evil Wizard's turn to attack and regenerate
            if wizard.health > 0:
                print(f"\n{wizard.name} is regenerating health... 🖤")
                time.sleep(1)
                wizard.regenerate()
                wizard.attack(player)

            if player.health <= 0:
                print(f"{player.name} has been defeated! 💀")
                wizard.display_stats()
                break
        except KeyError:
            continue

    if wizard.health <= 0:
        player.display_stats()
        print(f"\nThe wizard {wizard.name} has been defeated by {player.name}! 🏆")
        print(f"You have saved the world from the darkness. Congratulations, {player.name}! 🎉")
        time.sleep(2)  # Pause at the end to give time for the player to enjoy the victory


# Main function to handle the flow of the game
def main():
    print_intro_text()
    time.sleep(1)
    print_backstory()
    time.sleep(1)

    # Character creation phase
    player = select_character()

    # Evil Wizard is created
    wizard = EvilWizard("Vornath, the Doom Bringer")

    # Start the battle
    battle(player, wizard)


if __name__ == "__main__":
    main()
