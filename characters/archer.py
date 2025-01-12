# archer.py
from characters.character import Character


class Archer(Character):

    def __init__(self, name):
        super().__init__(name,health=120,attack_power=35 )