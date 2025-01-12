import time
from menus import show_battle_menu
from actions import handle_player_action


def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        try:
            show_battle_menu()

            handle_player_action(player, wizard)

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
        time.sleep(2)
