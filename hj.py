import time

class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        if self.player_class == "Paladin":
            self.max_hp = 200
            self.attack = 25
            self.defense = 15
            self.energy = 150
            self.speed = 15
        elif self.player_class == "Warrior":
            self.max_hp = 150
            self.attack = 20
            self.defense = 12
            self.energy = 100
            self.speed = 10
        elif self.player_class == "Mage":
            self.max_hp = 100
            self.attack = 25
            self.defense = 8
            self.energy = 120
            self.speed = 7
        elif self.player_class == "Rogue":
            self.max_hp = 120
            self.attack = 15
            self.defense = 10
            self.energy = 150
            self.speed = 12

        self.hp = self.max_hp

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage

    def attack_enemy(self, enemy):
        return self.attack

    def defend(self):
        self.defense += 5
        print(f"{self.name} defends, increasing defense.")

    def recharge_energy(self):
        recovered_energy = min(50, int(0.5 * self.energy))
        self.energy += recovered_energy
        print(f"{self.name} recovers {recovered_energy} energy.")

    def recharge_health(self):
        recovered_health = min(10, int(0.1 * self.max_hp))
        self.hp = min(self.max_hp, self.hp + recovered_health)
        print(f"{self.name} recovers {recovered_health} health.")

class Enemy:
    def __init__(self, name, hp, attack, defense, speed, special_attack=None):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.special_attack = special_attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage

    def attack_player(self, player):
        return self.attack

def fight(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while player.is_alive() and enemy.is_alive():
        print(f"{player.name} ({player.player_class}) (HP: {player.hp}, Energy: {player.energy}) vs {enemy.name} (HP: {enemy.hp})")
        print("What will you do?")
        print("1. Attack")
        print("2. Defend")
        print("3. Recharge Energy")
        print("4. Recharge Health")
        choice = input("Enter your choice: ")

        if choice == "1":
            if player.energy >= 10:
                player.energy -= 10
                damage = player.attack_enemy(enemy)
                enemy.take_damage(damage)
                print(f"{player.name} attacks {enemy.name} for {damage} damage.")
            else:
                print("Not enough energy to attack!")
        elif choice == "2":
            player.defend()
        elif choice == "3":
            player.recharge_energy()
        elif choice == "4":
            player.recharge_health()
        else:
            print("Invalid choice.")

        if enemy.is_alive():
            if player.speed >= enemy.speed:
                damage = enemy.attack_player(player)
                player.take_damage(damage)
                print(f"{enemy.name} attacks {player.name} for {damage} damage.")
            else:
                damage = enemy.attack_player(player)
                player.take_damage(damage)
                print(f"{enemy.name} attacks {player.name} for {damage} damage.")
                if player.is_alive():
                    if player.energy >= 10:
                        player.energy -= 10
                        damage = player.attack_enemy(enemy)
                        enemy.take_damage(damage)
                        print(f"{player.name} attacks {enemy.name} for {damage} damage.")
                    else:
                        print("Not enough energy to attack!")
                else:
                    break
    if player.is_alive():
        print(f"You defeated the {enemy.name}!")
        player.energy = min(100, player.energy + 50)  # Recover 50% of energy after battle
        return True
    else:
        print(f"{player.name} has been defeated! Game Over!")
        return False

def main():
    print("Welcome to the Adventure!")
    player_name = input("Enter your name: ")
    if player_name.lower() == "liam":
        player_class = "Paladin"
    else:
        print("Choose your class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Rogue")
        player_class_choice = input("Enter the number corresponding to your class: ")
        if player_class_choice == "1":
            player_class = "Warrior"
        elif player_class_choice == "2":
            player_class = "Mage"
        elif player_class_choice == "3":
            player_class = "Rogue"
        else:
            print("Invalid choice, defaulting to Warrior.")
            player_class = "Warrior"

    player = Player(player_name, player_class)

    dragon = Enemy("Dragon", 200, 30, 20, 10, special_attack=70)  # Dragon's special attack does 70 damage
    goblin = Enemy("Goblin", 30, 8, 2, 5)
    orc = Enemy("Orc", 50, 12, 5, 7)
    demon_lord = Enemy("Demon Lord", 100, 20, 10, 12)

    enemies = [goblin, orc, demon_lord, dragon]

    for enemy in enemies:
        if fight(player, enemy):
            print(f"You continue your journey after defeating the {enemy.name}.")
        else:
            break

    print("Game Over")

if __name__ == "__main__":
    main()
