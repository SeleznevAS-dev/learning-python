# 5.1.


class Weapon:
    def __init__(self, name, damage, max_ammo):
        self.__name = name
        self.__damage = damage
        self.__max_ammo = max_ammo
        self.__ammo = self.__max_ammo
        self.__durability = 100
        self.__max_durability = 100

    def __fire(self):
        if self.__ammo <= 0:
            print("Нет патронов для выстрела.")
            return 0
        if self.__durability <= 0:
            print("Оружие сломано.")
            return 0

        self.__ammo -= 1
        self.__durability -= 2
        return self.__damage

    def fire(self):
        return self.__fire()

    def __reload(self):
        print(f"Патроны до перезарядки: {self.__ammo}.")
        self.__ammo = self.__max_ammo
        print(f"Патроны после перезарядки: {self.__ammo}.")
        return self.__ammo

    def reload(self):
        return self.__reload()

    def __repair(self):
        print(f"Прочность до ремонта: {self.__durability}.")
        self.__durability = self.__max_durability
        print(f"Прочность после ремонта: {self.__durability}.")
        
    def repair(self):
        return self.__repair()


class Player:
    def __init__(self, nickname, weapon):
        self.__health = 100
        self.__nickname = nickname
        self.__weapon = weapon
        self.__additional_ammo_magazine = 5
        self.__weapon_repair_kit = 1

    def __shoot(self, target):
        damage = self.__weapon.fire()
        target.__health -= damage
        if damage > 0:
            print(
                f"Игрок {self.__nickname} выстрелил в {target.__nickname} и нанёс {damage} единиц урона."
            )
            if target.__health <= 0:
                print(f"Игрок {target.__nickname} был убит.")
                target.__health = 0

    def shoot(self, target):
        self.__shoot(target)

    def __reload_weapon(self):
        if self.__additional_ammo_magazine > 0:
            self.__weapon.reload()
            self.__additional_ammo_magazine -= 1
        else:
            print("Нет дополнительных магазинов для перезарядки.")

    def reload_weapon(self):
        self.__reload_weapon()

    def __repair_weapon(self):
        if self.__weapon_repair_kit > 0:
            self.__weapon.repair()
            self.__weapon_repair_kit -= 1
        else:
            print("Нет комплектов для ремонта оружия.")

    def repair_weapon(self):
        self.__repair_weapon()


sniper_rifle = Weapon("Sniper rifle", 60, 10)

player1 = Player("Player", sniper_rifle)

player2 = Player("NewPlayer", Weapon("AK-47", 35, 30))

player1.shoot(target=player2)
player2.shoot(target=player1)
player1.shoot(target=player2)
player1.reload_weapon()
player1.repair_weapon()
