# JASA - Just Another Space Adventure


# imports
import sys
import random
import json
import pickle


# dict of possible weapons; put in database and add prefixes/suffixes?
with open('data/weapons.json', 'r') as json_file:
    weapons = json.load(json_file)
weapons = {int(key):value for key, value in weapons.items()}

# dict of enemies
# use range of numbers to set, which enemies can be fought at the moment, then remove/add numbers to change this?
with open('data/enemies.json', 'r') as json_file:
    enemies = json.load(json_file)
enemies = {int(key):value for key, value in enemies.items()}

#rumour_list = ['\tDid you know that the Space Ninja Academy\n\thas its headquarters on Vome Seven?\n', '\tTy Corp is harvesting radioactive material\n\tnear Solecerca.\n', '\tDo you believe in personal luck?\nIt is said to influence everthing!\n']
with open('data/rumours.json', 'r') as json_file:
    rumour_list = json.load(json_file)
rumour_list = {int(key):value for key, value in rumour_list.items()}

# level up messages
with open('data/level_up.json', 'r') as json_file:
    level_up_list = json.load(json_file)
level_up_list = {int(key):value for key, value in level_up_list.items()}

# planets; could probably be put into a dict/json as well --> should make changing the planet easier
with open('data/planets.json', 'r') as json_file:
    planets = json.load(json_file)
planets = {int(key):value for key, value in planets.items()}

# enigmator hints
with open('data/enigma_hints.json', 'r') as json_file:
    hints = json.load(json_file)
hints = {int(key):value for key, value in hints.items()}

# possible difficulties:
difficulties = {0: 'Mundane', 1: 'Easy', 2: 'Vanilla', 3: 'Challenging', 4: 'Hard', 5: 'Deranged', 6: 'Impossible'}
current_difficulty = 2 # has to be set externally at first, to allow choosing it before the char is actually created

# player character class
class Char():
    def __init__(self, name):
        self.name = name
        self.maxhp = 50
        self.hp = self.maxhp
        self.credits = 100
        self.boosters = 1
        self.weaponlvl = 0
        self.weapon = weapons[self.weaponlvl]
        self.exp = 0
        self.lvl = 1
        self.luck = 1
        self.enigma = 0
        self.speed = 1 # not used yet
        self.planet_n = 0
        self.planet = planets[self.planet_n][0]
        self.difficulty = 2
        self.maxsp = 1
        self.sp = self.maxsp

    @property
    def dmg(self):
        global weapons
        damage = self.weapon[1]
        return(damage)


# enemy class
class Enemy():
    def __init__(self, name, maxhp, dmg, credits):
        self.name = name
        self.maxhp = maxhp
        self.hp = self.maxhp
        self.dmg = dmg
        self.credits = credits
    @classmethod
    def generate(self):
        return Enemy()


# clear the screen
def clr():
    print('\n'*50)


# continue
def cont():
    print('\tPress enter to continue.\n')


# exit the game
def quitter():
    clr()
    print('\tWe shall meet again.\n')
    sys.exit()


# introduction/background info
def main():
    clr()
    print(
        '''
             _   _    ____    _    
            | | / \  / ___|  / \   
         _  | |/ _ \ \___ \ / _ \  
        | |_| / ___ \ ___) / ___ \ 
         \___/_/   \_\____/_/   \_\ 
         
         Just Another Space Adventure
        ''')
    print('''
        In the distant future, in a solar system
        not very far from our own, a lone hero
        can fight for survival, fame, and money
        (not necessarily in that order).

        Will you be that hero?

        1: Engage
        2: Load game
        3: Change difficulty (current: %s)
        9: Quit
        ''' % difficulties[current_difficulty])
    choice = input('')
    if choice in ['', '1', 'Engage', 'engage']:
        intro()
    elif choice in ['2', 'Load', 'load', 'Load game']:
        gameload()
    elif choice in ['3', 'Difficulty', 'difficulty', 'Change difficulty']:
        change_difficulty()
    elif choice in ['9', 'Quit', 'quit']:
        quitter()
    else:
        clr()
        main()


# allow setting the difficulty
def change_difficulty():
    clr()
    print('''
        Choose your desired difficulty:

        1: Mundane
        2: Easy
        3: Vanilla (default)
        4: Challenging
        5: Hard
        6: Deranged
        7: Impossible
        ''')
    choice = input('')
    global current_difficulty
    if choice in ['1', 'Mundane', 'mundane']:
        current_difficulty = 0
        clr()
        print('\tMundane. Note: danger of boredom.\n')
        cont()
        choice = input('')
        main()
    elif choice in ['2', 'Easy', 'easy']:
        current_difficulty = 1
        clr()
        print('\tEasy. Easy peasy lemon squeezy.\n')
        cont()
        choice = input('')
        main()
    elif choice in ['3', 'Vanilla', 'vanilla']:
        current_difficulty = 2
        clr()
        print('\tVanilla. The classic.\n')
        cont()
        choice = input('')
        main()
    elif choice in ['4', 'Challenging', 'challenging']:
        current_difficulty = 3
        clr()
        print('\tChallenging. Challenge accepted!\n')
        cont()
        choice = input('')
        main()
    elif choice in ['5', 'Hard', 'hard']:
        current_difficulty = 4
        clr()
        print('\tHard. Nuff said.\n')
        cont()
        choice = input('')
        main()
    elif choice in ['6', 'Deranged', 'deranged']:
        current_difficulty = 5
        clr()
        print('\tDeranged. Who in their right mind would choose this?\n')
        cont()
        choice = input('')
        main()
    elif choice in ['7', 'Impossible', 'impossible']:
        current_difficulty = 6
        clr()
        print('\tImpossible. Now that\'s a mission.\n')
        cont()
        choice = input('')
        main()
    elif choice in ['8', 'Back', 'back']:
        main()
    else:
        change_difficulty


# load
def gameload():
    clr()
    print('''
    Please type the exact name of your savegame file.
    Press enter to accept the default ('jasa.save').
    ''')
    choice = input('')
    if choice == '':
        choice = 'jasa.save'
    clr()
    print('\tLoading game from ', choice)
    with open(choice, 'rb') as pickle_file:
        global player
        player = pickle.load(pickle_file)
    print('''
    Game loaded.
    Welcome back, %s.
    ''' % player.name) # note: while loading is not implemented, this breaks the game because player does not exist yet
    cont()
    choice = input('')
    start()


# introduction part two
def intro():
    clr()
    print('\tWhat is your name, nameless hero?\n')
    choice = input('')
    global player
    player = Char(choice)
    player.difficulty = current_difficulty
    start()


# main screen
def start():
    clr()
    # level check
    if player.exp >= player.lvl*player.lvl*5:
        level_up()
    print('''
        Name: %s
        HP: %i/%i
        SP: %i/%i
        Credits: %i
        Boosters: %i
        Weapon: %s
        Level: %i
        Experience: %i/%i

        Planet: %s

        Choose wisely:

        1: Look for a fight
        2: Search for quests
        3: Visit the weapon shop
        4: Visit the booster dispenser
        5: Listen to rumours
        6: Visit the Enigmator
        7: Visit the ITF (Interplanetary Teleportation Facility)
        8: Save the game
        9: Quit
        ''' % (player.name, player.hp, player.maxhp, player.sp, player.maxsp, player.credits, player.boosters, player.weapon[0], player.lvl, player.exp, player.lvl*player.lvl*5, player.planet))
    choice = input('')
    if choice in ['1', 'Fight', 'fight', 'Look for a fight']:
        battleprep()
    elif choice in ['2', 'Quests', 'quests', 'Search for quests']:
        quests()
    elif choice in ['3', 'weapon', 'Weapon', 'weapons', 'Weapons', 'Visit the weapon shop']:
        weapon_shop()
    elif choice in ['4', 'booster', 'Booster', 'boosters', 'Boosters', 'Visit the booster dispenser']:
        booster_shop()
    elif choice in ['5', 'Rumours', 'rumours', 'Listen', 'listen', 'Listen to rumours']:
        rumours()
    elif choice in ['6', 'Enigmator', 'enigmator', 'Visit the Enigmator']:
        enigmator()
    elif choice in ['7', 'ITF', 'itf']:
        itf()
    elif choice in ['8', 'Save', 'save', 'Save the game']:
        gamesave()
    elif choice in ['9', 'Quit', 'quit']:
        quitter()
    elif choice in ['creds']:
        player.credits += 9999 # cheat
        start()
    else:
        clr()
        start()


# level up
def level_up():
    clr()
    player.exp -= player.lvl*player.lvl*5 # change required exp?
    player.lvl += 1
    if player.lvl % 3 == 0: # increase max SP every third level; might change to every fifth level, depending on the power of the skills
        player.maxsp += 1
    player.maxhp = player.maxhp * 1.2
    player.hp = player.maxhp
    player.luck += 1 # randomize [0, 1]?
    level_up_n = random.randint(1, len(level_up_list))
    level_up_message = level_up_list[level_up_n - 1]
    print('''
        Level up!

        %s

        Level increased to %i.
        Max HP increased to %i.
        SP replenished to %i.
        ''' % (level_up_message, player.lvl, player.maxhp, player.maxsp))
    cont()
    choice = input('')
    start()


# save
def gamesave():
    clr()
    print('\tSaving.')
    with open('jasa.save', 'wb') as pickle_file:
        pickle.dump(player, pickle_file, pickle.HIGHEST_PROTOCOL)
    print('\tGame saved at jasa.save.')
    cont()
    choice = input('')
    start()


# teleportation facility
def itf():
    clr()
    print('''
        Welcome to the Interplanetary Teleporation Facility.
        Thanks to Ty Corp, you are travelling for free using
        our novel emission-free teleportation algorithm.

        Please choose your travel destination.

        1: %s
        2: %s
        3: %s
        4: %s
        5: %s
        6: %s
        7: %s
        8: Exit ITF
        ''' % (planets[0][0], planets[1][0], planets[2][0], planets[3][0], planets[4][0], planets[5][0], planets[6][0]))
    choice = input('')
    if choice in ['1', 'Linga', 'linga']:
        player.planet_n = 0
        player.planet = planets[0][0]
        teleport()
    elif choice in ['2', 'Vome Seven', 'vome seven']:
        player.planet_n = 1
        player.planet = planets[player.planet_n][0]
        teleport()
    elif choice in ['3', 'Krek Beta', 'krek beta']:
        player.planet_n = 2
        player.planet = planets[player.planet_n][0]
        teleport()
    elif choice in ['4', 'Pylox', 'pylox']:
        player.planet_n = 3
        player.planet = planets[player.planet_n][0]
        teleport()
    elif choice in ['5', 'Cherenkovia Gamma', 'cherenkovia gamma']:
        player.planet_n = 4
        player.planet = planets[player.planet_n][0]
        teleport()
    elif choice in ['6', 'Pastor Major', 'pastor major']:
        player.planet_n = 5
        player.planet = planets[player.planet_n][0]
        teleport()
    elif choice in ['7', 'Solecerca', 'solecerca']:
        player.planet_n = 6
        player.planet = planets[player.planet_n][0]
        teleport()
    else:
        start()


# teleportation
def teleport():
    clr()
    print('''
        You enter the teleportation chamber.
        Within what feels like seconds, you have arrived
        at your destination.

        Welcome to %s.
        ''' % player.planet)
    cont()
    choice = input('')
    start()


# riddle machine
def enigmator():
    clr()
    print('''
        You use your holo projector to access the Enigmator.
        The introduction pops up:

        ENIGMATOR - join the mystery!

        Please choose how to proceed:

        1: Play
        2: Show current level
        3: Show the rules
        4: Hint
        5: Enigma Ultima
        6: Log off
        ''')
    choice = input('')
    if choice in ['', '1', 'Play', 'play']:
        enigma_play()
    elif choice in ['2', 'level', 'Level', 'Show current level']:
        clr()
        print('\tYou are currently at Enigma Level %i.' % player.enigma)
        cont()
        choice = input('')
        enigmator()
    elif choice in ['3', 'rules', 'Rules', 'Show the rules']:
        enigmator_rules()
    elif choice in ['4', 'Hint', 'hint']:
        enigmator_hint()
    elif choice in ['5', 'Ultima', 'ultima', 'Enigma Ultima']:
        enigma_ultima()
    else:
        start()


# buy a hint
def enigmator_hint():
    clr()
    print('''
    You may buy a hint for your current enigma.
    Please note that your access to this hint will not be saved.

    1: Buy hint (1 Credit)
    2: Back
    ''')
    choice = input('')
    if choice in ['1', 'Buy', 'buy', 'Buy hint']:
        clr()
        print(hints[player.enigma])
        player.credits -= 1
        cont()
        choice = input('')
        enigmator()
    elif choice in ['2', 'Back', 'back']:
        enigmator()
    else:
        enigmator_hint()


# which enigma to start; might get messy in the near future
def enigma_play():
    if player.enigma == 0:
        enigma_00()
    elif player.enigma == 1:
        enigma_01()
    else:
        enigmator()


# show the rules of enigmator
def enigmator_rules():
    clr()
    print('''
        The rules are simple: you play, you win, you win!
        Solving one level immediately unlocks the next.
        
        Please note that Ty Corp thanks you for playing
        Enigmator. However, Ty Corp can not be held accountable
        for loss of Credits, loss of time, loss of memory, loss
        of orientation, damage to you (physical or psychological),
        damage to your surroundings, damage to others.
        By playing Enigmator you agree to forfeiting your
        right to litigate.
        ''')
    cont()
    choice = input('')
    enigmator()


def enigma_ultima():
    clr()
    print('''
        You are about to attempt solving the ultimate Enigma.
        Please note that once you begin, you will be locked in
        a cycle of trying to enter the correct answer. 
        Until you do so, you can not leave.

        Please type 'Ultima' to proceed.
        ''')
    choice = input('')
    if choice == 'Ultima':
        clr()
        print('\tMissing.')
        choice = ''
        while choice != 'final answer':
            choice = input('')
        print('\tWin.')
        enigmator()
    else:
        enigmator()


# first enigma; hint: 'Sum... sum... something.'
def enigma_00():
    clr()
    print('''
        987 --> 6
        1337 --> 5
        8080 --> ?
        ''')
    choice = input('')
    if choice in ['7', 'Seven', 'seven']:
        enigma_win()
    else:
        enigma_fail()


# second enigma; hint: 'Politics. In Spaaace.'
def enigma_01():
    clr()
    print('''
        In another time, in another galaxy, 
        how does liberty die?
        ''')
    choice = input('')
    if choice in 'With thunderous applause':
        enigma_win()
    else:
        enigma_fail()


# third enigma; hint: 'Letters and numbers.'
def enigma_02():
    clr()
    print('''
        Ten --> 39
        Eleven --> 63
        Twelve --> ?
        ''')
    choice = input('')
    if choice in ['87', 'eightyseven', 'eighty-seven', 'eighty seven']:
        enigma_win()
    else:
        enigma_fail()


# fourth enigma; hint: 'Lateral thinking: the Ides of March.'
def enigma_03():
    clr()
    print('\tYLXP ZQ ESTD RLXP?')
    choice = input('')
    if choice in ['JASA', 'YPHP', 'ULDL']:
        enigma_win()
    else:
        enigma_fail()


# fifth enigma; hint: 'Who?'
def enigma_04():
    clr()
    print('\tDemons run...')
    choice = input('')
    if choice in ['when a good man goes to war', 'good man', 'to war', 'Good Man', 'to War']:
        enigma_win()
    else:
        enigma_fail()


# correct enigma answer
def enigma_win():
    clr()
    print('\tCorrect answer.')
    print('\tYou win 5 Credits.') # needs improvement
    player.credits += 5
    player.enigma += 1
    cont()
    choice = input('')
    enigmator()


# wrong enigma answer
def enigma_fail():
    clr()
    print('\tWrong answer.')
    cont()
    choice = input('')
    enigmator()


# random rumours
def rumours():
    clr()
    rumour_n = random.randint(1, len(rumour_list))
    print(rumour_list[rumour_n - 1])
    cont()
    choice = input('')
    start()


# booster shop
def booster_shop():
    clr()
    print('''
        You find the local booster vending machine.
        The display has several dead pixels but you
        can see that there are several options
        available:

        You currently have %i booster(s).

        1: Buy 1 booster (15 Credits)
        2: Buy 3 boosters (40 Credits)
        3: Buy 10 boosters (120 Credits)
        4: Go back
        ''' % player.boosters)
    choice = input('')
    if choice == '1':
        clr()
        print('''
        This will cost you 15 Credits, please confirm
        your purchase.

        1: Buy
        2: Go back
        ''')
        choice = input('')
        if choice in ['', '1', 'Buy', 'buy']:
            if player.credits >= 15:
                clr()
                player.credits -= 15
                player.boosters += 1
                print('\tPurchase successful.')
                cont()
                choice = input('')
                booster_shop()
            else:
                clr()
                print('\tInsufficient Credits.')
                cont()
                choice = input('')
                booster_shop()
        else:
            booster_shop()
    elif choice == '2':
        clr()
        print('''
        This will cost you 40 Credits, please confirm
        your purchase.

        1: Buy
        2: Go back
        ''')
        choice = input('')
        if choice in ['', '1', 'Buy', 'buy']:
            if player.credits >= 40:
                clr()
                player.credits -= 40
                player.boosters += 3
                print('\tPurchase successful.')
                cont()
                choice = input('')
                booster_shop()
            else:
                clr()
                print('\tInsufficient Credits.')
                cont()
                choice = input('')
                booster_shop()
        else:
            booster_shop()
    elif choice == '3':
        clr()
        print('''
        This will cost you 120 Credits, please confirm
        your purchase.

        1: Buy
        2: Go back
        ''')
        choice = input('')
        if choice in ['', '1', 'Buy', 'buy']:
            if player.credits >= 120:
                clr()
                player.credits -= 120
                player.boosters += 10
                print('\tPurchase successful.')
                cont()
                choice = input('')
                booster_shop()
            else:
                clr()
                print('\tInsufficient Credits.')
                cont()
                choice = input('')
                booster_shop()
        else:
            booster_shop()
    else:
        start()


# quests; nothing to be seen yet
def quests():
    clr()
    print('\tAt the moment, no quests are available.\n')
    cont()
    choice = input('')
    start()


# weapon shop
def weapon_shop():
    clr()
    price = weapons[player.weaponlvl + 1][2]
    print('''
        Welcome to the weapon shop.
        My name is Blasty McBlast.
        If you are looking for a mighty new blaster
        to burn some more holes into your enemies
        you have certainly come to the right place.

        What can I do for you?

        1: Buy the next best weapon (%i Credits)
        2: Buy some armour
        3: Go back
        ''' % price)
    choice = input('')
    if choice in ['', '1', 'Buy', 'buy', 'Buy the next weapon']:
        clr()
        print('''
        This will cost you %i Credits, please confirm
        your purchase.

        1: Buy
        2: Go back
        ''' % price)
        choice = input('')
        if choice in ['', '1', 'Buy', 'buy']:
            if player.credits >= price:
                clr()
                player.credits -= price
                player.weaponlvl += 1
                player.weapon = weapons[player.weaponlvl]
                print('\tPurchase successful.')
                cont()
                choice = input('')
                weapon_shop()
            else:
                clr()
                print('\tInsufficient Credits.')
                cont()
                choice = input('')
                weapon_shop()
        else:
            weapon_shop()
    elif choice in ['2', 'Armour', 'armour']:
        clr()
        print('''
        Armour? What kind of armour? This is a weapon
        shop. Anyway, people everywhere are shooting
        at each other with blasters, what do you think
        some armour might do for you?
            ''')
        cont()
        choice = input('')
        weapon_shop()
    elif choice in ['3', 'Back', 'back', 'Go back']:
        start()
    else:
        clr()
        weapon_shop()


# prepare enemy entity
def battleprep():
    global enemy
    el = enemies[random.randint(1, len(enemies))-1]
    enemy = Enemy(el[0], el[1], el[2], el[3])
    battle()


# fight the created enemy
def battle():
    clr()
    print('''
        %s:
        HP: %i/%i
        SP: %i/%i
        Boosters: %i

        %s:
        HP: %i/%i

        Choose wisely:

        1: Fight
        2: Use booster
        3: Skills
        4: Flee
        ''' % (player.name, player.hp, player.maxhp, player.sp, player.maxsp, player.boosters, enemy.name, enemy.hp, enemy.maxhp))
    choice = input('')
    if choice in ['', '1', 'Fight', 'fight',]:
        fight()
    elif choice in ['2', 'Booster', 'booster', 'Use booster', 'use booster', 'Use Booster']:
        booster()
    elif choice in ['3', 'Skills', 'skills']:
        skills()
    elif choice in ['4', 'Flee', 'flee']:
        flee()
    else:
        clr()
        battle()


# skill overview; unlocked by leveling up
def skills():
    clr()
    print('''
        Skills:

        1: Double Shot (Level 3)
        2: Stun Shot (Level 5)
        3: skill 3 (Level 8)
        4: skill 4 (Level 10)
        5: skill 5 (Level 14)
        6: skill 6 (Level 20)
        etc
        9: Back
        ''')
    choice = input('')
    if choice in ['1', 'Double Shot', 'double shot']:
        skill_01()
    elif choice in ['2', 'Stun Shot', 'stun shot']:
        skill_02()
    elif choice in ['3']:
        skill_03()
    elif choice in ['4']:
        skill_04()
    elif choice in ['5']:
        skill_05()
    elif choice in ['6']:
        skill_06()
    elif choice in ['9', 'Back', 'back']:
        battle()
    else:
        skills()


# first skill; double shot
def skill_01():
    clr()
    if player.lvl >= 3:
        player.sp -= 1
        print('\tYou use Double Shot, dealing 150 % damage.')
        pdmg = (player.dmg + random.randint(1,3) - 2) * 1.5
        enemy.hp -= pdmg
        print('\tThe enemy loses %i HP.' % pdmg)
        cont()
        choice = input('')
        if enemy.hp <= 0:
            victory()
        edmg = enemy.dmg + random.randint(1,3) - 2
        player.hp -= edmg
        print('\tThe enemy attacks. You lose %i HP.' % edmg)
        cont()
        choice = input('')
        if player.hp <= 0:
            defeat()
        else:
            battle()
    else:
        print('\tYou can not yet use this skill.')
        cont()
        choice = input('')
        battle()


# second skill; stun shot
def skill_02():
    clr()
    if player.lvl >= 5:
        player.sp -= 1
        print('\tYou use Stun Shot, preventing the enemy from attacking.')
        pdmg = player.dmg + random.randint(1,3) - 2
        enemy.hp -= pdmg
        print('\tThe enemy loses %i HP.' % pdmg)
        cont()
        choice = input('')
        if enemy.sp <= 0:
            victory()
        print('\tThe enemy is stunned and can not attack.')
        cont()
        choice = input('')
        battle()
    else:
        print('\tYou can not yet use this skill.')
        cont()
        choice = input('')
        battle()
    battle()


# third skill; missing
def skill_03():
    clr()
    battle()


# fourth skill; missing
def skill_04():
    clr()
    battle()


# fifth skill; missing
def skill_05():
    clr()
    battle()


# sixth skill; missing
def skill_06():
    clr()
    battle()


# the fight proper; player always attacks first, seems unfair
def fight():
    clr()
    pdmg = player.dmg + random.randint(1,3) - 2
    enemy.hp -= pdmg
    print('\tYou attack. The enemy loses %i HP.' % pdmg)
    cont()
    choice = input('')
    if enemy.hp <= 0:
        victory()
    edmg = enemy.dmg + random.randint(1,3) - 2
    player.hp -= edmg
    print('\tThe enemy attacks. You lose %i HP.' % edmg)
    cont()
    choice = input('')
    if player.hp <= 0:
        defeat()
    else:
        battle()


# failed, restart
def defeat():
    clr()
    print('\tYou have been defeated.')
    print('\tYour tale must end here.\n')
    cont()
    choice = input('')
    clr()
    main()


# enemy defeated, back to start
def victory():
    clr()
    print('\tYou are victorious!')
    cred = enemy.credits + random.randint(1,5)
    print('\tYou have found %i Credits.' % cred)
    player.credits += cred
    experience = random.randint(1,5) + random.randint(1,3) + player.luck
    print('\tYou have earned %i XP.' % experience)
    player.exp += experience
    if random.randint(1,2) == 1:
        player.sp += 1
        if player.sp >= player.maxsp:
            player.sp = player.maxsp
        print('\tYou have regained 1 SP.')
    cont()
    choice = input('')
    start()


# boost hp (if possible)
def booster():
    clr()
    if player.boosters >= 1:
        player.boosters -= 1
        if player.hp >= player.maxhp:
            print('\tYou use a booster despite feeling fine.')
            print('\tWhat a waste.')
        else:
            player.hp += 50
            if player.hp > player.maxhp:
                player.hp = player.maxhp
            print('\tYou use a booster.')
            print('\tYou feel refreshed.')
        cont()
    else:
        print('\tYou do not own any boosters.')
        cont()
    choice = input('')
    battle()


# try to run away
def flee():
    clr()
    flee_n = random.randint(1,2)
    if flee_n == 1:
        print('\tYou got away.')
        cont()
        choice = input('')
        start()
    else:
        print('\tYou could not make it to safety.')
        # let enemy attack? needs some stronger penalty
        print('\tYour HP have been reduced by 1.\n')
        player.hp -= 1
        cont()
        choice = input('')
        if player.hp <= 0:
            defeat()
        battle()


# go
if __name__ == '__main__':
    main()

