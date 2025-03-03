class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Character:
    def __init__(self, name, health, attack, defence, x=0, y=0):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def is_alive(self):
        return self.health > 0

class Plains(MapTile):
    pass

class Forest(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)

class Warrior(Character):
    def attack(self, enemy):
        damage = max(self.attack - enemy.defence, 0)  # Ensure damage is not negative
        enemy.health = enemy.health - damage

class Archer(Character):
    def ranged_attack(self, enemy):
        damage = max(self.attack - enemy.defence, 0)  # Ensure damage is not negative
        enemy.health = enemy.health - damage

# Create the map
map = [
    [Plains(0, 0), Forest(1, 0), Plains(2, 0)],
    [Forest(0, 1), Plains(1, 1), Plains(2, 1)],
    [Plains(0, 2), Plains(1, 2), Plains(2, 2)]
]

# Create characters
warrior = Warrior("Ankit", 100, 20, 10)
archer = Archer("Anjali", 80, 15, 5)

# Game loop
while True:
    warrior.move(1, 0)
    archer.ranged_attack(warrior)

    if not warrior.is_alive():
        print("Game Over!!")
        break
    
    


