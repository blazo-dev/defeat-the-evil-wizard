# paladin.py

from characters.character import Character
import time
import random


class Paladin(Character):
    def __init__(self, name: str, defense_status: bool = False):
        super().__init__(name, health=160, attack_power=20, healing_capacity=30)
        self.defense_status = defense_status

    def special_ability(self, opponent):
        print(f"\n{self.name}, it's time to unleash your special ability! 🔥")
        print("1. Holy Strike - Double the attack damage for one turn ⚡")
        print("2. Divine Shield - Avoid the next incoming attack ⏳")

        choice = input("Choose an option: ")

        if choice == '1':
            self.holy_strike(opponent)
        elif choice == '2':
            print(f"\n{self.name} prepares to evade the next attack with divine protection! ⏳")
            self.divine_shield()
        else:
            print(f"⚠️ That choice is not recognized, {self.name}. Choose wisely, for your enemies grow stronger! ⚔️")

    def holy_strike(self, opponent):
        print(
            f"\n🔥 The power of the Holy Strike surges through your weapon! A strike of light that deals double damage! ⚡")
        time.sleep(1)
        attack_amount = random.randint(5, self.attack_power) * 2
        opponent.health -= attack_amount
        print(f"\n{self.name} attacks {opponent.name} for {attack_amount} damage! 💔")

    def divine_shield(self):
        print(f"\n🛡️ You raise your shield high! The divine protection envelops you, ready to block the next attack! ⏳")
        self.defense_status = True
        super().heal()

    def reset_defense(self):
        self.defense_status = False
