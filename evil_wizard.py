# evil_wizard.py
from character import Character


class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power

    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        regeneration_amount = 5

        self.health += regeneration_amount
        print(f"{self.name} regenerates {regeneration_amount} health! Current health: {self.health}")
