from Entity import Salve
from Player import Human
from Enemies import Ogre, Troll, Dragon



class Fight(Human, Ogre, Troll, Dragon, Salve):
    def EnemyFight(self):

        if int(number) == 1:
            location = "Forest"
            enemy = ogre
        if int(number) == 2:
            location = "Cave"
            enemy = troll
        
        print("An ",enemy.name," lives in this" + location + ", fight!\n")
        while(h.health >= 0) or (enemy.health >= 0):
                hw = input(h.name +", 1.Attack or 2.Heal?:" )

                if hw == "1":
                    enemy.take_damage(h.damage)
                    print(enemy.name," health:", enemy.health)

                if hw == "2":
                    while h.snumber > 0:
                        h.take_healing(h.healing_points)
                        h.snumber -= 1
                        print(h.name, " health: ", h.health, " \nSalves remaining: ", h.snumber)
                        break
                    if h.health > 450:
                        print("Overdose, lol")
                        h.health = 0
                    elif h.snumber == 0:
                        print("you drink all salves")

                if enemy.name == "Chop" and enemy.health < 30:
                    print(enemy.name," charges you, deals 40 damage and dies")
                    h.health -= enemy.idk
                    enemy.health = 0
                    print(enemy.name," health: ",enemy.health)
                    print(h.name," health: ", h.health)
                else:
                    h.take_damage(enemy.damage)
                    print(enemy.name," Attacks you!\n",h.name," health:", h.health)

                if h.health <= 0:
                    print("Game Over")
                    break
                if enemy.health <= 0:
                    print("You got dragon potion from " + enemy.nickname)
                    break
        
class BossFight(Human, Ogre, Troll, Dragon, Salve):
    def bfight():
     print("Final battle,", h.name, "!\n", dragon)
     while(h.health >= 0) or (dragon.health >= 0):
        hw = input(h.name +", 1.Attack, 2.Heal or 3.Use your Potion?:" )

        if hw == "1":
            if h.sword_status != 50:
                dragon.take_damage(h.damage - dragon.idk)
                print(dragon.name," health:", dragon.health)
            else:
                dragon.take_damage(h.damage + h.sword_status)
                print(dragon.name," health:", dragon.health)

        if hw == "2":
            while h.snumber > 0:
                h.take_healing(h.healing_points)
                h.snumber -= 1
                print(h.name, " health: ", h.health, " \nSalves remaining: ", h.snumber)
                break
            if h.health > 450:
                print("Overdose, lol")
                h.health = 0
            elif h.snumber == 0:
                print("you drink all salves")

        if hw == "3":
            h.potion(50)
            print("Using potion...\nYou put poison on your sword!\n Sword damage:", h.damage + h.sword_status)

        h.take_damage(dragon.damage)
        print(dragon.name," Attacks you!\n",h.name," health:", h.health) 

        if h.health <= 0:
                print("Game Over")
                break
        if dragon.health <= 0:
                print("YOU DEFEAT ", dragon.name, "!\n THE CHEESE IS YOUR!!")
                break
# ------------------------------------------------------------------------

#PLAYER:

h = Human("Pudge", "Butcher", 250, 25)
h.health_salve("Healing Salve", 125, 5)
h.potion(0)
# ------------------------------------------------------------------------

#Enemies:
#Troll
troll = Troll("Bababoy", "Troll", 100, 20)


#Ogre
ogre = Ogre("Chop","Ogre", 125, 24 )
ogre.spell("Charge", "Orc goes crazy when his health is low and charges into his enemy before death", 40)
# ------------------------------------------------------------------------

#BOSS:
#Dragon
dragon = Dragon("Three-Headed Dragon", "Boss", 400, 40)
dragon.spell("Thick skin", "Skin reduce damage by 20", 20)
# ------------------------------------------------------------------------

#LOCATION:

# ------------------------------------------------------------------------

#GAME:
print("Welcome,", h, "\nYour mission is to steal CHEESE from Dragon!\n\nWhose your way(enter number):\n 1.Forest\n 2.Cave")
number = input()
if int(number) < 1 or int(number) > 2 :
    print("Wrong Number...\n Whose your way(enter number):\n 1.Forest\n 2.Cave")
    number = input()
e = Fight
e.EnemyFight(number)

boss = BossFight
if h.is_alive() == True:
    boss.bfight()
# ------------------------------------------------------------------------