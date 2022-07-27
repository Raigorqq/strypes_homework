# from Entity import Info, Check, Spell, Salve, Sword
from Player import Human
from Enemies import Ogre, Troll, Dragon

# ------------------------------------------------------------------------

#Player

h = Human("Pudge", "Butcher", 250, 25)
h.health_salve("Healing Salve", 125)
h.potion(0)
# ------------------------------------------------------------------------

#Enemies
#Troll
troll = Troll("Bababoy", None, 100, 20)


#Ogre
ogre = Ogre("Chop","Ludaka", 125, 24 )
ogre.spell("Charge", "Orc goes crazy when his health is low and charges into his enemy before death", 40)
# ------------------------------------------------------------------------

#BOSS
#Dragon
dragon = Dragon("Three-Headed Dragon", "Boss", 400, 40)
dragon.spell("Thick skin", "Skin reduce damage by 20", 20)

# ------------------------------------------------------------------------

#GAME
salves = 5
print("Welcome,", h, "\nYour mission is to steal CHEESE from Dragon!\n\nWhose your way(enter number):\n 1.Forest\n 2.Cave")
number = input()


#LOCATION 1.FOREST(OGRE)
if int(number) == 1:
    print("An ",ogre.name," lives in this Forest, fight!\n")
    while(h.health >= 0) or (ogre.health >= 0):
        hw = input(h.name +", 1.Attack or 2.Heal?:" )

        if hw == "1":
            ogre.take_damage(h.damage)
            print(ogre.name," health:", ogre.health)

        if hw == "2":
            while salves > 0:
                h.take_healing(h.healing_points)
                salves -= 1
                print(h.name, " health: ", h.health, " \nSalves remaining: ", salves)
                break
            if h.health > 450:
                print("Overdose, lol")
                h.health = 0
            elif salves == 0:
                print("you drink all salves")

        if ogre.health < 30:
            print(ogre.name," charges you, deals 40 damage and dies")
            h.health -= ogre.idk
            ogre.health = 0
            print(ogre.name," health: ",ogre.health)
            print(h.name," health: ", h.health)
        else:
            h.take_damage(ogre.damage)
            print(ogre.name," Attacks you!\n",h.name," health:", h.health)

        if h.health <= 0:
            print("Game Over")
            break
        if ogre.health <= 0:
            print("You got dragon potion from troll")
            break

#LOCATION 2.CAVE(TROLL)
if int(number) ==2:
    print("An ", troll.name," lives in this Cave, fight!\n")
    while(h.health >= 0) or (troll.health >= 0):
        hw = input(h.name + ", 1.Attack or 2.Heal?:" )

        if hw == "1":
            troll.take_damage(h.damage)
            print(troll.name," health:", troll.health)

        if hw == "2":
            while salves > 0:
                h.take_healing(h.healing_points)
                salves -= 1
                print(h.name, " health: ", h.health, " \nSalves remaining: ", salves)
                break
            if h.health > 450:
                print("Overdose, lol")
                h.health = 0
            elif salves == 0:
                print("you drink all salves")

        h.take_damage(troll.damage)
        print(troll.name," Attacks you!\n",h.name," health:", h.health)  

        if h.health <= 0:
            print("Game Over")
            break
        if troll.health <= 0:
            print("You got dragon potion from troll")
            break


#BOSS FIGHT
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
        while salves > 0:
            h.take_healing(h.healing_points)
            salves -= 1
            print(h.name, " health: ", h.health, " \nSalves remaining: ", salves)
            break
        if h.health > 450:
            print("Overdose, lol")
            h.health = 0
        elif salves == 0:
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
