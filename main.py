from classes.game import Person, BColors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic
fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("Thunder", 20, 120, "Black")
blizzard = Spell("Blizzard", 30, 140, "Black")
meteor = Spell("Meteor", 40, 170, "Black")
quake = Spell("Quake", 50, 200, "Black")

# Create White Magic
cure = Spell('Cure', 10, 100, 'White')
cura = Spell('Cura', 20, 200, 'White')


# Create some item
potion = Item('Potion', 'potion', 'Heals 50 HP', 50)
hipotion = Item('Hi-Potion', 'potion', 'Heals 100 HP', 100)
superpotion = Item('Super Potion', 'potion', 'Heals 500 HP', 500)
elixer = Item('Elixer', 'elixer', 'Fully restored MP/HP of one party member', 9999)
hielixer = Item('Hi-Elixer', 'elixer', 'Fully restored MP/HP of all party members', 9999)
grenade = Item('Grenade', 'attack', 'Deals 500 damage', 500)

player_magic = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{'item': potion, 'quantity': 15}, {'item': hipotion, 'quantity': 5},
                {'item': superpotion, 'quantity': 5}, {'item': elixer, 'quantity': 5},
                {'item': hielixer, 'quantity': 5}, {'item': grenade, 'quantity': 5}]

# Create Players
player1 = Person('Valos:', 1000, 100, 60, 34, player_magic, player_items)
player2 = Person('Nick :', 1000, 100, 60, 34, player_magic, player_items)
player3 = Person('Robot:', 1000, 100, 60, 34, player_magic, player_items)
enemy = Person('Devil:', 5000, 100, 100, 50, [], [])
players = [player1, player2, player3]


# Enemy Attack
def enemy_attack():
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(BColors.WARNING + BColors.BOLD + "ENEMY ATTACKED", enemy_dmg, "POINTS." + BColors.END_C)
    # print(BColors.OK_GREEN, "Your HP:", player.get_hp(), BColors.END_C)


# Main section
run = 1
running = True
print(BColors.FAIL + BColors.BOLD + "\t\t\t\t\t\t\t\t<<<<.....WELCOME TO RPG.....>>>>" + BColors.END_C)
while run < len(players) and running:
    print("\t\t\t\t\t\t================================================")
    for player in players:
        enemy.get_enemy_stats()
        for person in players:
            person.get_stats()
        print(BColors.UNDERLINE + BColors.BOLD + player.name + BColors.END_C)
        player.choose_action()
        choice = input("Choose Action: ")
        index = int(choice) - 1
        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print(BColors.OK_GREEN + BColors.BOLD + "YOU ATTACKED", dmg, "POINTS." + BColors.END_C)
            enemy_attack()
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose Magic: ")) - 1
            if magic_choice == -1:
                continue
            cost = player.magic[magic_choice].cost
            cost = player.get_mp() - cost
            if cost < 0:
                print(BColors.FAIL + BColors.BOLD + "<<<NOT ENOUGH MP>>>" + BColors.END_C)
            else:
                dmg = player.magic[magic_choice].generate_damage()
                spell = player.magic[magic_choice]
                if spell.types == 'Black':
                    enemy.take_damage(dmg)
                    print(BColors.OK_GREEN + BColors.BOLD + "YOU ATTACKED", dmg, "POINTS." + BColors.END_C)
                    player.reduce_mp(player.magic[magic_choice].cost)
                    enemy_attack()
                elif spell.types == "White":
                    player.heal(dmg)
                    player.reduce_mp(player.magic[magic_choice].cost)
        elif index == 2:
            player.choose_items()
            item_choice = int(input('Choose item: ')) - 1
            if item_choice >= len(player_items):
                print(BColors.FAIL + BColors.BOLD + "<<<WRONG CHOICE>>>" + BColors.END_C)
                continue
            item = player.items[item_choice]
            player.reduce_quantity(item_choice)
            if item['quantity'] < 0:
                item['quantity'] = 0
                print(BColors.FAIL + BColors.BOLD + "<<<NOT ENOUGH ITEMS>>>" + BColors.END_C)
                continue
            if item_choice == -1:
                continue
            if item['item'].types == 'potion':
                player.heal(item['item'].prop)
                print(BColors.OK_GREEN + '\n' + item['item'].name + ' heals for ' + str(item['item'].prop) + ' HP' +
                      BColors.END_C)
            elif item['item'].types == 'elixer':
                for member in players:
                    member.hp = member.max_hp
                    member.mp = member.max_mp
                print(BColors.OK_GREEN + '\n' + item['item'].name + ' fully restored HP/MP. ' + BColors.END_C)
            elif item['item'].types == 'attack':
                enemy.take_damage(item['item'].prop)
                print(BColors.OK_GREEN + BColors.BOLD + "YOU ATTACKED", item['item'].prop, "POINTS." + BColors.END_C)
        else:
            print(BColors.FAIL + "Wrong choice!" + BColors.END_C)
            running = False
        if player.get_hp() == 0:
            print(BColors.FAIL + player.name + "DIED!!!" + BColors.END_C)
            run += 1
        if run > 3:
            print(BColors.FAIL + "ALL PLAYERS ARE DEAD" + BColors.END_C)
            # running = False
        if enemy.get_hp() == 0:
            print(BColors.OK_GREEN + BColors.BOLD + "WOOO..!!! ENEMY IS DEAD" + BColors.END_C)
            running = False
