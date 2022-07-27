from Entity import Info, Check, Spell, Salve, Sword

#Player
class Human(Info, Check, Spell, Salve, Sword):


    def __str__(self):
        return (self.name + " the " + self.nickname)

h = Human("Pudge", "Butcher", 250, 25)
h.health_salve("Healing Salve", 125, 5)
h.potion(0)
