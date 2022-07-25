from Entity import Info, Check, Spell, Salve, Sword

#Player
class Human(Info, Check, Spell, Salve, Sword):


    def __str__(self):
        return (self.name + " the " + self.nickname)
