from Entity import Info, Check, Spell

#Troll
class Troll(Info, Check, Spell):
    

    def __str__(self):
        return ("Troll:" + self.name)

#Ogre
class Ogre(Info, Check, Spell):
    def __str__(self):
       return ("Ogre:" + self.name)


#BOSS

#Dragon
class Dragon(Info, Check, Spell):

    def __str__(self):
        return (self.name)