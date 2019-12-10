# Joseph Fitzpatrick
# Programming for IT
# Text Adventure Game

import random


####
# player class
class player(object):
    name = 'player'
    maxhp = 0
    maxmp = 0
    minmp = 0
    hp = 0
    mp = 0
    attack = 10
    mattack = 5
    xp = 0
    maxxp = 25
    gold = 0
    hpot = 3
    mpot = 3
    key = 0


# Enemy Classes
class slime(object):
    name = "Slime"
    hp = 30
    mp = 0
    attack = 4
    mattack = 0
    xpval = 5
    gpval = 5


class spider(object):
    name = "Spider"
    hp = 25
    mp = 0
    attack = 6
    mattack = 0
    xpval = 5
    gpval = 7


class bat(object):
    name = "Bat"
    hp = 15
    mp = 0
    attack = 2
    mattack = 0
    xpval = 2
    gpval = 2


class skeleton(object):
    name = "Skeleton"
    hp = 60
    mp = 0
    attack = 15
    mattack = 0
    xpval = 10
    gpval = 9


class undead(object):
    name = "Undead"
    hp = 35
    mp = 0
    attack = 7
    mattack = 0
    xpval = 10
    gpval = 9


class ghoul(object):
    name = "Ghoul"
    hp = 30
    mp = 0
    attack = 4
    mattack = 0
    xpval = 10
    gpval = 9


class skeletonking(object):
    name = "Skeleton King"
    hp = 100
    mp = 0
    attack = 25
    mattack = 0
    xpval = 10
    gpval = 9


# functions

def gamestart():
    print("A text adventure rpg by Joseph Fitzpatrick")
    player.name = input("What is your name? ")
    print('Your name is ' + player.name)
    print('Select a class')
    selection = input('1. Warrior \n2. Mage \n3. Paladin\n')
    if selection == "1":
        player.hp = 150
        player.maxhp = 150
        player.mp = 40
        player.maxmp = 40
        player.attack = 100
        player.mattack = 5
        print("You selected the Warrior class, here are the stats")
        print('Health: ', player.hp)
        print('Mana: ', player.mp)
        print('Attack: ', player.attack)
        print('Magic Attack: ', player.mattack)
        pause = input('')
        return player

    elif selection == "2":
        player.hp = 100
        player.maxhp = 100
        player.mp = 100
        player.maxmp = 100
        player.attack = 5
        player.mattack = 20
        print("You selected the Mage class, here are the stats")
        print('Health: ', player.hp)
        print('Mana: ', player.mp)
        print('Attack: ', player.attack)
        print('Magic Attack: ', player.mattack)
        pause = input('')
        return player

    elif selection == "3":
        player.hp = 125
        player.maxhp = 125
        player.mp = 75
        player.maxmp = 75
        player.attack = 7
        player.mattack = 7
        print("You selected the Paladin class, here are the stats")
        print('Health: ', player.hp)
        print('Mana: ', player.mp)
        print('Attack: ', player.attack)
        print('Magic Attack: ', player.mattack)
        pause = input('')
        return player

    else:
        print('Please select either 1, 2, or 3. Restarting character creation')
        pause = input('')
        gamestart()


def combatsystem(enemyname):
    enemy = enemyname
    print('You encountered a', enemy.name)
    print('What would you like to do?')
    print(player.name, "HP =", player.hp, enemy.name, "HP =", enemy.hp)
    while enemy.hp > 0:
        choice = input(' 1. Attack\n 2. Magic\n 3. Use Item\n')

        if choice == "1":
            print(player.name, 'attacks the', enemy.name)
            pause = input('')
            hitchance = random.randint(0, 10)
            if hitchance > 2:
                enemy.hp = enemy.hp - player.attack
                print('The', enemy.name, 'lost', player.attack, 'health, their hp is now', enemy.hp)
                pause = input('')

                if enemy.hp > 0:
                    player.hp = player.hp - enemy.attack
                    print(enemy.name, 'hits you for', enemy.attack, ', your hp is now', player.hp)
                    pause = input('')
                    print(player.name, "HP =", player.hp, enemy.name, "HP =", enemy.hp)
                    if player.hp <= 0:
                        gameover()

                else:
                    if enemy.name == "Slime":
                        enemy.hp = 10
                    elif enemy.name == "Spider":
                        enemy.hp = 8
                    elif enemy.name == "Bat":
                        enemy.hp = 15
                    elif enemy.name == "Skeleton":
                        enemy.hp = 40
                    elif enemy.name == "Undead":
                        enemy.hp = 35
                    elif enemy.name == "Ghoul":
                        enemy.hp = 30

                    print(player.name, 'has defeated the', enemy.name)
                    pause = input('')
                    player.xp = player.xp + enemy.xpval
                    player.gold = player.gold + enemy.gpval
                    print(player.name, 'has gained', enemy.xpval, 'xp', 'and got', enemy.gpval, 'gold')
                    pause = input('')
                    if player.xp >= player.maxxp:
                        player.maxxp = player.maxxp + 15
                        player.xp = 0
                        player.maxhp = player.maxhp + 10
                        player.maxmp = player.maxmp + 10
                        player.attack = player.attack + 5
                        player.mattack = player.mattack + 5
                        print(player.name, "leveled up!")
                        pause = input('')
                    else:
                        pass
                    break
            else:
                print(player.name, 'missed the', enemy.name)
                pause = input('')
                player.hp = player.hp - enemy.attack
                print(enemy.name, 'hits you for', enemy.attack, ', your hp is now', player.hp)
                pause = input('')
                if player.hp <= 0:
                    gameover()
                print(player.name, "HP =", player.hp, enemy.name, "HP =", enemy.hp)

        if choice == "2":
            print(player.name, "MP =", player.mp)
            print("Which spell would you like to use?")
            print('1. Fireball\n2. Heal')
            schoice = input()
            if schoice == "1":
                if player.mp == 0:
                    print("You do not have enough mana")
                    pause = input('')
                else:
                    enemy.hp = enemy.hp - player.mattack
                    player.mp = player.mp - 5
                    if player.mp <= player.minmp:
                        player.mp = player.minmp
                    print("You casted a fireball at the", enemy.name, "dealing", player.mattack, "their hp is now",
                          enemy.hp)
                    pause = input('')

                if enemy.hp > 0:
                    player.hp = player.hp - enemy.attack
                    print(enemy.name, 'hits you for', enemy.attack, ', your hp is now', player.hp)
                    pause = input('')
                    print(player.name, "HP =", player.hp, enemy.name, "HP =", enemy.hp)
                    if player.hp <= 0:
                        gameover()
                else:
                    if enemy.name == "Slime":
                        enemy.hp = 10
                    elif enemy.name == "Spider":
                        enemy.hp = 8
                    elif enemy.name == "Bat":
                        enemy.hp = 15
                    elif enemy.name == "Skeleton":
                        enemy.hp = 40
                    elif enemy.name == "Undead":
                        enemy.hp = 35
                    elif enemy.name == "Ghoul":
                        enemy.hp = 30

                    print(player.name, 'has defeated the', enemy.name)
                    pause = input('')
                    player.xp = player.xp + enemy.xpval
                    player.gold = player.gold + enemy.gpval
                    print(player.name, 'has gained', enemy.xpval, 'xp', 'and got', enemy.gpval, 'gold')
                    pause = input('')
                    if player.xp >= player.maxxp:
                        player.maxxp = player.maxxp + 15
                        player.xp = 0
                        player.maxhp = player.maxhp + 20
                        player.maxmp = player.maxmp + 20
                        player.attack = player.attack + 5
                        player.mattack = player.mattack + 5
                        print(player.name, "leveled up!")
                        pause = input('')
                    else:
                        pass
                    break

            if schoice == "2":
                if player.hp == player.maxhp:
                    print("You already have full health")
                else:
                    player.hp = player.hp + 50
                    if player.hp > player.maxhp:
                        player.hp = player.maxhp
                    print("Your health is now", player.hp)
                    pause = input('')

                if enemy.hp > 0:
                    player.hp = player.hp - enemy.attack
                    print(enemy.name, 'hits you for', enemy.attack, ', your hp is now', player.hp)

        if choice == "3":
            print("Which item would you like to use")
            print("1. HP Potion\n2. MP Potion")
            potchoice = input()
            if potchoice == "1":
                if player.hpot == 0:
                    print("You do not have any HP Potions")
                    pause = input('')
                else:
                    player.hp = player.hp + 50
                    player.hpot = player.hpot - 1
                    if player.hp > player.maxhp:
                        player.hp = player.maxhp
                    print("Your health is now", player.hp)
                    pause = input('')

            if potchoice == "2":
                if player.mpot == 0:
                    print("You do not have any mana potions")
                    pause = input('')
                else:
                    player.mp = player.mp + 50
                    player.mpot = player.mpot - 1
                    if player.mp > player.maxmp:
                        player.mp = player.maxmp
                print("Your mana is now", player.mp)
                pause = input('')

            if enemy.hp > 0:
                player.hp = player.hp - enemy.attack
                print(enemy.name, 'hits you for', enemy.attack, ', your hp is now', player.hp)
                pause = input('')
                if player.hp <= 0:
                    gameover()
                print(player.name, "HP =", player.hp, enemy.name, "HP =", enemy.hp)


def randomenemy():
    global rename
    elist = [slime, spider, bat]
    rename = random.choice(elist)
    return rename


def shop():
    print("Welcome to the shop")
    print("What would you like to buy?")
    print(player.name, "Gold:", player.gold)
    print("1. Health Potion  2 Gold\n2. Mana Potion  2 Gold\n3. Health Upgrade  20 Gold\n4. Mana Upgrade  20 Gold\n"
          "5. Exit Shop")
    shopchoice = input()
    if shopchoice == "1":
        if player.gold < 2:
            print("You do not have enough gold")
            pause = input('')
            shop()
        else:
            player.hpot = player.hpot + 1
            player.gold = player.gold - 2
            print("You purchased a health potion")
            pause = input('')
            shop()
    if shopchoice == "2":
        if player.gold < 2:
            print("You do not have enough gold")
            pause = input('')
            shop()
        else:
            player.mpot = player.mpot + 1
            player.gold = player.gold - 2
            print("You purchased a mana potion")
            pause = input('')
            shop()
    if shopchoice == "3":
        if player.gold < 20:
            print("You do not have enough gold")
            pause = input('')
            shop()
        else:
            player.maxhp = player.maxhp + 20
            player.gold = player.gold - 20
            print("Your max health is now", player.maxhp)
            pause = input('')
            shop()
    if shopchoice == "4":
        if player.gold < 20:
            print("You do not have enough gold")
            pause = input('')
            shop()
        else:
            player.maxmp = player.maxmp + 20
            player.gold = player.gold - 20
            print("Your max mana is now", player.maxmp)
            pause = input('')
            shop()
    if shopchoice == "5":
        town()


def inn():
    print("Welcome to the Inn, would you like to rest?")
    print("Cost: 5 Gold")
    print("1. Yes\n2. No")
    innchoice = input()
    if innchoice == "1":
        if player.gold < 5:
            print("You do not have enough gold")
            pause = input('')
            inn()
        else:
            player.gold = player.gold - 5
            player.hp = player.maxhp
            player.mp = player.maxmp
            print("You rested at the inn, full restoring health and mana.")
            pause = input('')
            town()
    if innchoice == "2":
        town()


room1clear = 0
room2clear = 0
room3clear = 0
room4clear = 0
room5clear = 0
room6clear = 0
room7clear = 0
room8clear = 0
room9clear = 0


def room1():
    global room1clear
    if room1clear == 1:
        print("Room 1")
        print("This room has been cleared")
        print("Where would you like to go?")
        print("1. Up\n2. Right")
        nav = input()
        if nav == "1":
            room4()
        if nav == "2":
            room2()
        else:
            room1()
    else:
        print("Room 1")
        combatsystem(skeleton)
        room1clear = 1
        room1()


def room2():
    global room2clear
    if room2clear == 1:
        print("Room 2")
        print("This room has been cleared")
        print("Where would you like to go?")
        print("1. Left\n2. Up\n3. Right")
        nav = input()
        if nav == "1":
            room4()
        if nav == "2":
            room5()
        if nav == "3":
            room3()
        else:
            room2()
    else:
        print("Room 2")
        combatsystem(undead)
        room2clear = 1
        room2()


def room3():
    global room3clear
    if room3clear == 1:
        print("Room 3")
        print("This room has been cleared")
        print("Where would you like to go?")
        print("1. Up\n2. Left")
        nav = input()
        if nav == "1":
            room6()
        if nav == "2":
            room2()
        else:
            room3()
    else:
        print("Room 3")
        combatsystem(undead)
        room3clear = 1
        room3()


def room4():
    global room4clear
    if room4clear == 1:
        print("Room 4")
        print("This room has been cleared")
        print("Where would you like to go?")
        print("1. Up\n2. Down\n3. Right")
        nav = input()
        if nav == "1":
            room7()
        if nav == "2":
            room1()
        if nav == "3":
            room5()
        else:
            room4()
    else:
        print("Room 4")
        combatsystem(skeleton)
        room4clear = 1
        room4()


def room5():
    global room5clear
    if room5clear == 1:
        print("Room 5")
        print("This room has been cleared")
        print("Where would you like to go?")
        print("1. Up\n2. Down\n3. Left\n4. Right")
        nav = input()
        if nav == "1":
            room4()
        if nav == "2":
            room2()
        if nav == "3":
            room4()
        if nav == "4":
            room6()
        else:
            room5()
    else:
        print("Room 5")
        combatsystem(ghoul)
        room5clear = 1
        room5()


def room6():
    global room6clear
    if room6clear == 1:
        print("Room 6")
        print("This room has been cleared")
        print("Where would you like to go?")
        print("1. Up\n2. Down\n3. Left")
        nav = input()
        if nav == "1":
            room9()
        if nav == "2":
            room3()
        if nav == "3":
            room5()
        else:
            room6()
    else:
        print("Room 6")
        combatsystem(skeleton)
        room6clear = 1
        room6()


def room7():
    global room7clear
    if room7clear == 1:
        print("Room 7")
        print("This room has been cleared")
        print("Where would you like to go?")
        print("1. Down\n2. Right")
        nav = input()
        if nav == "1":
            room4()
        if nav == "2":
            room8()
        else:
            room7()
    else:
        print("Room 7")
        combatsystem(undead)
        player.key = 1
        print("You got a key!")
        pause = input('')
        room7clear = 1
        room7()


def room8():
    global room8clear
    if room8clear == 1:
        print("Room 8")
        print("This room has been cleared")
        print("Where would you like to go?")
        print("1. Left\n2. Right\n3. Down")
        nav = input()
        if nav == "1":
            room7()
        if nav == "2":
            room9()
        if nav == "3":
            room5()
    else:
        print("Room 8")
        combatsystem(skeleton)
        room8clear = 1
        room8()


def room9():
    global room9clear
    if room9clear == 1:
        print("Room 9")
        print("This room has been cleared")
        print("There is a door, behind this door is a boss battle. A key is required to enter. Do you want to enter?")
        print("1. Yes\n2. No")
        keychoice = input()
        if keychoice == "1":
            if player.key == 0:
                print("You do not have the key")
                pass
            else:
                combatsystem(skeletonking)
                print("Congratulations! You beat the game!")
                exit()
        if keychoice == "2":
            pass
        print("Where would you like to go?")
        print("1. Down\n2. Left")
        nav = input()
        if nav == "1":
            room6()
        if nav == "2":
            room8()
        else:
            room9()

    else:
        print("Room 9")
        combatsystem(skeleton)
        room9clear = 1
        room9()


def dungeon():
    print(player.name, "entered the dungeon")
    pause = input('')
    room1()


def town():
    print("Welcome to the town! What would you like to do?")
    print("1. Fight\n2. Shop\n3. Inn\n4. Go to Dungeon\n5. Exit game")
    tchoice = input()
    if tchoice == "1":
        randomenemy()
        combatsystem(rename)
        town()
    if tchoice == "2":
        shop()
    if tchoice == "3":
        inn()
    if tchoice == "4":
        dungeon()
    if tchoice == "5":
        exit()
    else:
        town()


def gameover():
    print(player.name, "has died.")
    pause = input('')
    print("Game Over")
    exit()


gamestart()
room9()
town()
