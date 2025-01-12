import time

from characters.character import Character
from characters.evil_wizard import EvilWizard


def handle_player_action(player: Character, wizard: EvilWizard):
    choice = input("\nChoose an action 🔽: ")

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
        time.sleep(1)
        raise KeyError("Invalid option. Please try again. 🚫")
