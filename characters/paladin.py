# paladin.py

from characters.character import Character


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)
