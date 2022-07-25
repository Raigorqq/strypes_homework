#2.Entity
class Entity:
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def get_health(self):
        return self.health

    def take_damage(self, damage_points):
        self.health -= damage_points

    def take_healing(self, healing_points):
        self.health += healing_points
        if self.health > 100:
            self.health = 100

#0.Hero
class Hero(Entity):

    def __init__(self, name, nickname, health, damage):
        self.name = name
        self.nickname = nickname
        self.health = health
        self.damage = damage

    def __str__(self):
        return ("Hero: " + self.name + " the " + self.nickname)

    

h = Hero("Bron", "Dragonslayer", 100, 24)

print(h.name)
print(h.nickname)
print(h.health)

print(h)

print(h.is_alive())

h.take_damage(50)
print(h.health)

h.take_healing(20)
print(h.health)

#1.Orc
class Orc(Entity):
    def __init__(self, name, health, berserk_factor, damage):
        self.name = name
        self.health = health
        self.berserk_factor = berserk_factor
        self.damage = damage

    def __str__(self):
        return ("Orc:" + self.name)
    
    def berserker_mod(self):
        if self.berserk_factor is True:
            self.damage *= 2

o = Orc("Muha", 101, 1, 25)

print(o)
