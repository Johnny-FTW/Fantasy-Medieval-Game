from abc import ABC, abstractmethod
from time import sleep
import random


class Being(ABC):

    def __init__(self, name, dmg, armor, life):
        self.name = name
        self.dmg = dmg
        self.armor = armor
        self.life = life

    @abstractmethod
    def special_skill(self):
        pass


class Warrior(Being):
    specialization = "Warrior"

    def __init__(self, name, dmg=20, armor=10, life=70):
        super().__init__(name, dmg, armor, life)

    def special_skill(self):
        bonus_armor = random.randint(5,10)
        self.armor = self.armor + bonus_armor
        return f"{self.specialization} {self.name} picked up shield: +{bonus_armor} bonus armor!"


class Mage(Being):
    specialization = "Mage"

    def __init__(self, name, dmg=25, armor=5, life=70):
        super().__init__(name, dmg, armor, life)

    def special_skill(self):
        heal = random.randint(50,100)
        self.life = self.life + heal
        return f"{self.specialization} {self.name} used heal: +{heal} bonus health!"


class Ranger(Being):
    specialization = "Ranger"

    def __init__(self, name, dmg=30, armor=5, life=65):
        super().__init__(name, dmg, armor, life)

    def special_skill(self):
        fire_arrows = random.randint(5,10)
        self.dmg = self.dmg + fire_arrows
        return f"{self.specialization} {self.name} used fire arrows: +{fire_arrows} bonus dmg!"


class Dragon(Being):
    specialization = "Dragon"

    def __init__(self, name, dmg, armor, life):
        super().__init__(name, dmg, armor, life)

    def special_skill(self):
        fly_atack = random.randint(10, 30)
        self.dmg = self.dmg + fly_atack
        return f"{self.specialization} {self.name} is flying: +{fly_atack} bonus dmg!"


class Arena:

    def __init__(self, H1, H2):
        self.H1 = H1
        self.H2 = H2

    def fight(self):
        print(self.H1.special_skill())
        sleep(2)
        print(self.H2.special_skill())
        while self.H1.life > 0 and self.H2.life > 0:
            sleep(2)
            self.H1.life = self.H1.life + self.H1.armor - self.H2.dmg
            print(f'{self.H2.specialization} {self.H2.name} is atacking! Damage atack: {self.H2.dmg}')
            sleep(2)
            print(f'{self.H1.specialization} {self.H1.name} has current life: {self.H1.life}')
            if self.H1.life <= 0:
                break
            sleep(2)
            self.H2.life = self.H2.life + self.H2.armor - self.H1.dmg
            print(f'{self.H1.specialization} {self.H1.name} is atacking! Damage atack: {self.H1.dmg}')
            sleep(2)
            print(f'{self.H2.specialization} {self.H2.name} has current life: {self.H2.life}')
            if self.H2.life <= 0:
                break
        if self.H1.life > self.H2.life:
            print(f"Winner is {self.H1.specialization} {self.H1.name}")
        else:
            print(f"Winner is {self.H2.specialization} {self.H2.name}")


class War:

    def __init__(self, team_1, team_2, team_1_name="Team 1", team_2_name="Team 2"):
        self.team_1 = team_1
        self.team_2 = team_2
        self.team_1_name = team_1_name
        self.team_2_name = team_2_name

    def big_fight(self):

        i = 0
        z = 0
        print(self.team_1[i].special_skill())
        sleep(2)
        print(self.team_2[z].special_skill())

        while self.team_1[i].life > 0 and self.team_2[z].life > 0:
            sleep(2)
            self.team_1[i].life = self.team_1[i].life + self.team_1[i].armor - self.team_2[z].dmg
            print(f'{self.team_2[z].specialization} {self.team_2[z].name} is atacking! '
                  f'Damage atack: {self.team_2[z].dmg}')
            sleep(2)
            print(f'{self.team_1[i].specialization} {self.team_1[i].name}, current life:{self.team_1[i].life}')
            if self.team_1[i].life <= 0:
                print(f'{self.team_1[i].specialization} {self.team_1[i].name} has DIED!')
                i += 1
                if i == len(self.team_1):
                    print(f"{self.team_2_name} WON!")
                    break
                else:
                    print(self.team_1[i].special_skill())
            sleep(2)
            self.team_2[z].life = self.team_2[z].life + self.team_2[z].armor - self.team_1[i].dmg
            print(
                f'{self.team_1[i].specialization} {self.team_1[i].name} is atacking! '
                f'Damage atack: {self.team_1[i].dmg}')
            sleep(2)
            print(f'{self.team_2[z].specialization} {self.team_2[z].name}, current  life:{self.team_2[z].life}')
            if self.team_2[z].life <= 0:
                print(f'{self.team_2[z].specialization} {self.team_2[z].name} has DIED!')
                z += 1
                if z == len(self.team_2):
                    print(f"{self.team_1_name} WON!")
                    break
                else:
                    print(self.team_2[z].special_skill())


def print_menu():
    print("--------------------------------------------")
    print("WELCOME!, press:")
    print("\t[0] for ARENA (player vs player)")
    print("\t[1] for WAR (team vs team)")
    print("\t[2] for DRAGON(team vs environment)")
    print("\t[3] for QUIT APP ")


def print_menu_characters():
    print("Please choose character:")
    print("\t[0] choose Warrior")
    print("\t[1] choose Mage")
    print("\t[2] choose Ranger")


def create_character(team, name):
    print_menu_characters()
    try:
        menu_choice_character = int(input(f"{name} choose character: "))
        if menu_choice_character == 0:
            H1 = Warrior(name)
            team.append(H1)
        elif menu_choice_character == 1:
            H1 = Mage(name)
            team.append(H1)
        elif menu_choice_character == 2:
            H1 = Ranger(name)
            team.append(H1)
        else:
            print("Wrong input")
            create_character(team, name)
    except Exception as e:
        print(e)
        print("Please choose valid menu choice")
        create_character(team, name)


while True:
    print_menu()
    try:
        menu_choice = int(input("Your choice: "))
        if menu_choice < 0 or menu_choice > 3:
            raise Exception("Wrong menu choice")
    except Exception as e:
        print(e)
        print("Please choose valid menu choice")
        continue

    if menu_choice == 0:
        arena = []
        for i in range(1, 3):
            name_of_character = input(f"Player{i} choose name:")
            create_character(arena, name_of_character)
        Arena(arena[0], arena[1]).fight()

    elif menu_choice == 1:
        both_teams = []
        number_of_characters_in_team = int(input("Choose how many characters will fight in single team: "))
        for i in range(1, 3):
            team = []
            for z in range(1, number_of_characters_in_team+1):
                name_of_character = input(f"Player{i} choose name of character num.{z}:")
                create_character(team, name_of_character)
            both_teams.append(team)
        War(both_teams[0], both_teams[1]).big_fight()

    elif menu_choice == 2:
        team = []
        number_of_characters_vs_dragon = int(input("Choose how many characters will fight vs dragon: "))
        for i in range(1, number_of_characters_vs_dragon + 1):
            name_of_character = input(f"Choose name of character num.{i}:")
            create_character(team, name_of_character)
        dragon = [Dragon("Skrill",len(team)*15,len(team)*3,len(team)*50)]
        War(team,dragon,"Suicide suqad", "Dragon Skrill").big_fight()

    elif menu_choice == 3:
        print("Good bye!")
        break





