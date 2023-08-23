import random

class Player:
    def __init__(self):
        self.hp = 10

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0

class Enemy:
    def __init__(self, name, max_hp, max_damage):
        self.name = name
        self.hp = max_hp
        self.max_damage = max_damage

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0

    def attack(self):
        return random.randint(1, self.max_damage)

def main():
    print("Welcome to the Terminal Mini RPG Game!")
    print("You are standing at the entrance of a mysterious forest.")

    player = Player()

    while player.is_alive():
        print("\nWhat do you want to do?")
        print("1. Enter the forest")
        print("2. Turn back and leave")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            enter_forest(player)
        elif choice == "2":
            print("You decide to turn back and leave. Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def enter_forest(player):
    print("\nYou enter the forest and encounter a fork in the path.")
    print("Do you want to go left or right?")

    while True:
        print("1. Go left")
        print("2. Go right")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            go_left(player)
        elif choice == "2":
            go_right(player)
        else:
            print("Invalid choice. Please enter 1 or 2.")

def go_left(player):
    enemy = Enemy("Goblin", max_hp=5, max_damage=3)
    print("\nYou follow the left path and encounter a {}!".format(enemy.name))

    battle(player, enemy)

def go_right(player):
    print("\nYou take the right path and find a group of wild animals.")
    print("They chase you away. You barely escape.")
    print("You decide to head back to the entrance of the forest.")

def battle(player, enemy):
    while player.is_alive() and enemy.is_alive():
        print("\nWhat do you want to do?")
        print("1. Attack")
        print("2. Run away")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            player_attack = random.randint(1, 4)
            enemy_attack = enemy.attack()

            print("You deal {} damage to the {}.".format(player_attack, enemy.name))
            enemy.take_damage(player_attack)

            if enemy.is_alive():
                print("The {} retaliates and deals {} damage to you.".format(enemy.name, enemy_attack))
                player.take_damage(enemy_attack)
            else:
                print("You have defeated the {}!".format(enemy.name))
                break
        elif choice == "2":
            print("You manage to escape from the {} and return to the entrance.".format(enemy.name))
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    if not player.is_alive():
        print("You have been defeated. Game over.")
        return

    print("\nYou continue your journey deeper into the forest.")

    # Battle with boss
    boss = Enemy("Ancient Dragon", max_hp=15, max_damage=5)
    print("\nYou encounter the mighty {}!".format(boss.name))

    battle(player, boss)

    if player.is_alive():
        print("\nCongratulations! You have defeated the final boss and won the game!")

if __name__ == "__main__":
    main()

