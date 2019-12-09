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
    maxxp = 10
    gold = 0
    hpot = 5
    mpot = 5


# Enemy Classes
class slime(object):
    name = "Slime"
    hp = 20
    mp = 0
    attack = 2
    mattack = 0
    xpval = 5
    gpval = 5
    drop = random.randint(0, 2)


class spider(object):
    name = "Spider"
    hp = 18
    mp = 0
    attack = 2
    mattack = 0
    xpval = 5
    gpval = 7
    drop = random.randint(0, 2)


class skeleton(object):
    name = "Skeleton"
    hp = 30
    mp = 0
    attack = 4
    mattack = 0
    xpval = 10
    gpval = 9
    drop = random.randint(0, 2)


# functions

def gamestart():
    print("A text adventure rpg by Joseph Fitzpatrick")
    player.name = input("What is your name? ")
    print('Your name is ' + player.name)
    print('Select a class')
    selection = input('1. Warrior \n2. Mage \n3. Paladin\n')
    if selection == "1":
        player.hp = 200
        player.maxhp = 200
        player.mp = 5
        player.maxmp = 50
        player.attack = 10
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
        player.mattack = 10
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
                    elif enemy.name == "Skeleton":
                        enemy.hp = 30

                    print(player.name, 'has defeated the', enemy.name)
                    pause = input('')
                    player.xp = player.xp + enemy.xpval
                    player.gold = player.gold + enemy.gpval
                    print(player.name, 'has gained', enemy.xpval, 'xp', 'and got', enemy.gpval, 'gold')
                    pause = input('')
                    if player.xp >= player.maxxp:
                        player.maxhp = player.maxhp + 20
                        player.maxmp = player.maxmp + 20
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
                    elif enemy.name == "Skeleton":
                        enemy.hp = 30

                    print(player.name, 'has defeated the', enemy.name)
                    pause = input('')
                    player.xp = player.xp + enemy.xpval
                    player.gold = player.gold + enemy.gpval
                    print(player.name, 'has gained', enemy.xpval, 'xp', 'and got', enemy.gpval, 'gold')
                    pause = input('')
                    if player.xp >= player.maxxp:
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


def gameover():
    print(player.name, "has died.")
    pause = input('')
    print("Game Over")
    exit()


combatsystem(skeleton)
combatsystem(skeleton)
