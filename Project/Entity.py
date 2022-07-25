class Info:
    def __init__(self, name, nickname, health, damage):
        self.name = name
        self.nickname = nickname
        self.health = health
        self.damage = damage


class Spell:
    def spell(self, spell_name, info, idk):
        self.spell_name = spell_name
        self.info = info
        self.idk = idk

class Check:
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

class Salve:
    def health_salve(self, salve_name, healing_points):
        self.salve_name = salve_name
        self.healing_points = healing_points

class Sword:
    def potion(self, sword_status):
        self.sword_status = sword_status