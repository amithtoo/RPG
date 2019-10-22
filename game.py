import random
from classes.magic import Spell

class BColors:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_C = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk_l = atk - 10
        self.atk_h = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.name = name
        self.actions = ['Attack', 'Magic', 'Items']

    def generate_damage(self):
        return random.randrange(self.atk_l, self.atk_h)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def reduce_quantity(self, index):
        self.items[index]['quantity'] -= 1

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(BColors.FAIL + BColors.OK_BLUE + "Actions" + BColors.END_C)
        for item in self.actions:
            print("   ", str(i), ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + BColors.FAIL + BColors.OK_BLUE + "Magic Spells" + BColors.END_C)
        for magic in self.magic:
            print("   ", str(i), ".", magic.name, "(Cost :", magic.cost, ")")
            i += 1

    def choose_items(self):
        i = 1
        print("\n" + BColors.FAIL + BColors.OK_BLUE + "Items" + BColors.END_C)
        for item in self.items:
            print("   ", str(i), ".", item['item'].name, '(' + item['item'].description + ')' + '(x' +
                  str(item['quantity']) + ')')
            i += 1

    def get_enemy_stats(self):
        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""
        if len(hp_string) < 9:
            dec = 9 - len(hp_string)
            while dec > 0:
                current_hp += " "
                dec -= 1
        current_hp += hp_string
        hp_bar = ''
        hp_bar_ticks = (self.hp / self.max_hp) * 100 / 2
        while hp_bar_ticks > 0:
            hp_bar += '█'
            hp_bar_ticks -= 1
        for hp_len in range(len(hp_bar), 50):
            hp_bar += ' '
        print("                               " + " __________________________________________________" +
              "                        ")
        print(BColors.BOLD + BColors.FAIL + self.name + ":          " + current_hp + " HP: |" +
              BColors.FAIL + hp_bar + BColors.END_C + "|")

    def get_stats(self):
        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""
        if len(hp_string) < 9:
            dec = 9 - len(hp_string)
            while dec > 0:
                current_hp += " "
                dec -= 1
        current_hp += hp_string
        mp_string = str(self.mp) + "/" + str(self.max_mp)
        current_mp = ""
        if len(mp_string) < 7:
            dec = 7 - len(mp_string)
            while dec > 0:
                current_mp += " "
                dec -= 1
        current_mp += mp_string
        hp_bar = ''
        hp_bar_ticks = (self.hp / self.max_hp) * 100 / 4
        while hp_bar_ticks > 0:
            hp_bar += '█'
            hp_bar_ticks -= 1
        for hp_len in range(len(hp_bar), 25):
            hp_bar += ' '
        mp_bar = ''
        mp_bar_ticks = (self.mp / self.max_mp) * 100 / 4
        while mp_bar_ticks > 0:
            mp_bar += '█'
            mp_bar_ticks -= 1
        for mp_len in range(len(mp_bar), 25):
            mp_bar += ' '
        print("                                " + "_________________________" + "                        " +
              "_________________________")
        print(BColors.BOLD + self.name + BColors.END_C + ":          " + current_hp + " HP: |" +
              BColors.OK_GREEN + hp_bar + BColors.END_C + "|          " + current_mp + BColors.BOLD + " MP: |" +
              BColors.OK_BLUE + mp_bar + BColors.END_C + "|")
