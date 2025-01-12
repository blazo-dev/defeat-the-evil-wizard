# character.py
import random


class Character:
    def __init__(self, name: str, health: int, attack_power: int, healing_capacity: int = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.healing_capacity = healing_capacity

    def attack(self, opponent):
        attack_amount = random.randint(5, self.attack_power)
        opponent.health -= attack_amount
        print(f"\n{self.name} attacks {opponent.name} for {attack_amount} damage! ⚔️")

    def display_stats(self):
        print(f"""
📊 {self.name}'s Stats
─────────────────────────────
💖 Health: {self.health}/{self.max_health}
⚔️ Attack Power: {self.attack_power}
✨ Healing Capacity: {self.healing_capacity}
─────────────────────────────
        """)

    def heal(self):
        heal_amount = random.randint(5, 20)
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"\n{self.name}'s Health: {self.health}/{self.max_health} 💖")
