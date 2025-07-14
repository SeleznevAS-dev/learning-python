class Weapon:
    def __init__(self, name, damage, max_ammo):
        self.name = name
        self.damage = damage
        self.max_ammo = max_ammo
        self.ammo = self.max_ammo
        self.durability = 100
        self.max_durability = 100

    def Fire(self):
        if self.ammo <= 0:
            print("Нет патронов для выстрела.")
            return 0
        if self.durability <= 0:
            print("Оружие сломано.")
            return 0

        self.ammo -= 1
        self.durability -= 2
        return self.damage

    def Reload(self):
        print(f"Патроны до перезарядки: {self.ammo}.")
        self.ammo = self.max_ammo
        print(f"Патроны после перезарядки: {self.ammo}.")
        return self.ammo

    def Repair(self):
        print(f"Прочность до ремонта: {self.durability}.")
        self.durability = self.max_durability
        print(f"Прочность после ремонта: {self.durability}.")


class Player:
    def __init__(self, nickname, weapon):
        self.health = 100
        self.nickname = nickname
        self.weapon = weapon
        self.additional_ammo_magazine = 5
        self.weapon_repair_kit = 1

    def Shoot(self, target):
        damage = self.weapon.Fire()
        target.health -= damage
        if damage > 0:
            print(
                f"Игрок {self.nickname} выстрелил в {target.nickname} и нанёс {damage} единиц урона."
            )
            if target.health <= 0:
                print(f"Игрок {target.nickname} был убит.")
                target.health = 0

    def Reload_weapon(self):
        if self.additional_ammo_magazine > 0:
            self.weapon.Reload()
            self.additional_ammo_magazine -= 1
        else:
            print("Нет дополнительных магазинов для перезарядки.")

    def Repair_weapon(self):
        if self.weapon_repair_kit > 0:
            self.weapon.Repair()
            self.weapon_repair_kit -= 1
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
