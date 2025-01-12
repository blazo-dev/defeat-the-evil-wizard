# archer.py
from characters.character import Character
import time


class Archer(Character):

    def __init__(self, name: str, evasion_status: bool = False):
        super().__init__(name, health=120, attack_power=35)
        self.evasion_status = evasion_status

    def special_ability(self, opponent):
        print(f"\n{self.name}, it's time to unleash your special ability! 🔥")
        print("1. Quick Shot - Double the attack damage for one turn ⚡")
        print("2. Evade - Avoid the next incoming attack ⏳")

        choice = input("Choose an option: ")

        if choice == '1':
            self.quick_shots(opponent)
        elif choice == '2':
            print(f"\n{self.name} prepares to evade the next attack! ⏳")
            self.evade()
        else:
            print(f"{self.name}, that is not a valid option! Choose wisely! ⚔️")

    def quick_shots(self, opponent):
        print(f"\n{self.name} unleashes a Quick Shot! Double arrows fly toward {opponent.name}! 🏹")
        time.sleep(1)
        self.attack(opponent)
        self.attack(opponent)
        pass

    def evade(self):
        print(f"\n{self.name} prepares to evade the next attack! 💨️")
        self.evasion_status = True
        pass

    def reset_evasion(self):
        self.evasion_status = False
