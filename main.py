class Unit:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.ii = 0

class Soldier(Unit):
    def __init__(self, name, health, attack_power):
        self.attack_power = attack_power
        super().__init__(name, health)
    def atack(self, unit):
        unit.health -= self.attack_power


class Archer(Unit):
    def __init__(self, name, health, range_attack_power):
        self.range_attack_power = range_attack_power
        super().__init__(name, health)
    def atack(self, unit):
        unit.health -= self.range_attack_power

soldier1 = Soldier("1", 100, 10)
soldier2 = Soldier("2", 100, 10)
archer1 = Archer("1", 80, 15)
archer2 = Archer("2", 80, 15)
soldier1.atack(archer1)
archer1.atack(soldier2)

print(archer1.health)
print(soldier2.health)



























