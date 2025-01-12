import time

from characters.archer import Archer
from menus import show_battle_menu
from actions import handle_player_action
from story import display_defeat_message, display_victory_message


def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        try:
            show_battle_menu()
            handle_player_action(player, wizard)

            if wizard.health > 0:
                print(f"\n{wizard.name} is regenerating health... 🖤")
                time.sleep(1)
                wizard.regenerate()

                if isinstance(player, Archer) and player.evasion_status:
                    print(f"\nWith a swift roll, {player.name} dodges the incoming strike! 💨")
                    player.reset_evasion()
                    continue  # Skip the wizard's attack for this round

                wizard.attack(player)

            if player.health <= 0:
                display_defeat_message(player, wizard)
                wizard.display_stats()
                break

        except KeyError:
            continue

    if wizard.health <= 0:
        display_victory_message(player, wizard)
