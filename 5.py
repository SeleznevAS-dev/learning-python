# 5.1.

class Weapon:
    def __init__(self, name, damage, max_ammo):
        self.__name = name
        self.__damage = damage
        self.__max_ammo = max_ammo
        self.__ammo = self.__max_ammo
        self.__durability = 100
        self.__max_durability = 100

    def Fire(self):
        if self.__ammo <= 0:
            print("Нет патронов для выстрела.")
            return 0
        if self.__durability <= 0:
            print("Оружие сломано.")
            return 0

        self.__ammo -= 1
        self.__durability -= 2
        return self.__damage

    def Reload(self):
        print(f"Патроны до перезарядки: {self.__ammo}.")
        self.__ammo = self.__max_ammo
        print(f"Патроны после перезарядки: {self.__ammo}.")
        return self.__ammo

    def Repair(self):
        print(f"Прочность до ремонта: {self.__durability}.")
        self.__durability = self.__max_durability
        print(f"Прочность после ремонта: {self.__durability}.")


class Player:
    def __init__(self, nickname, weapon):
        self.__health = 100
        self.__nickname = nickname
        self.__weapon = weapon
        self.__additional_ammo_magazine = 5
        self.__weapon_repair_kit = 1

    def Shoot(self, target):
        damage = self.__weapon.Fire()
        target.__health -= damage
        if damage > 0:
            print(
                f"Игрок {self.__nickname} выстрелил в {target.__nickname} и нанёс {damage} единиц урона."
            )
            if target.__health <= 0:
                print(f"Игрок {target.__nickname} был убит.")
                target.__health = 0

    def Reload_weapon(self):
        if self.__additional_ammo_magazine > 0:
            self.__weapon.Reload()
            self.__additional_ammo_magazine -= 1
        else:
            print("Нет дополнительных магазинов для перезарядки.")

    def Repair_weapon(self):
        if self.__weapon_repair_kit > 0:
            self.__weapon.Repair()
            self.__weapon_repair_kit -= 1
        else:
            print("Нет комплектов для ремонта оружия.")


sniper_rifle = Weapon("Sniper rifle", 60, 10)

player1 = Player("Player", sniper_rifle)

player2 = Player("NewPlayer", Weapon("AK-47", 35, 30))

player1.Shoot(target=player2)
player2.Shoot(target=player1)
player1.Shoot(target=player2)
player1.Reload_weapon()
player1.Repair_weapon()