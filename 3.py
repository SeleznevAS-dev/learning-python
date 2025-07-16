# 3.1.


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


# 3.2.
class Animal:
    def __init__(self, age, weight, speed, color):
        self.age = age
        self.weight = weight
        self.speed = speed
        self.color = color

    def run(self, new_speed):
        self.speed = new_speed

    def stop(self):
        self.speed = 0


class Dog(Animal):
    def __init__(self, age, weight, speed, color):
        super().__init__(age, weight, speed, color)
        self.bite_damage = 15

    def bark(self):
        print("Гав-гав!")

    def bite(self, target):
        print(f"Собака укусила {target} и нанесла {self.bite_damage} урона.")


class Cat(Animal):
    def __init__(self, age, weight, speed, color):
        super().__init__(age, weight, speed, color)
        self.claw_damage = 5

    def meow(self):
        print("Мяу-мяу!")

    def scratch(self, target):
        print(f"Кошка поцарапала {target} и нанесла {self.claw_damage} урона.")


dog = Dog(3, 15, 0, "коричневый")
cat = Cat(2, 4, 0, "серый")

print(f"Собака: возраст {dog.age}, вес {dog.weight} кг, цвет {dog.color}.")
print(f"Кошка: возраст {cat.age}, вес {cat.weight} кг, цвет {cat.color}.")

dog.bark()
dog.run(15)
dog.bite("вор")
dog.stop()

cat.meow()
cat.run(20)
cat.scratch("обои")
cat.stop()

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} включён.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.brand} {self.model} выключен.")


class MobilePhone(Device):
    def __init__(self, brand, model, phone_number):
        super().__init__(brand, model)
        self.phone_number = phone_number

    def call(self, number):
        if self.is_on:
            print(f"Звоним на номер {number}.")
        else:
            print("Телефон выключен.")

    def sms(self, number, message):
        if self.is_on:
            print(f"Отправляем SMS на номер {number}: {message}.")
        else:
            print("Телефон выключен.")


class Laptop(Device):
    def __init__(self, brand, model, operating_system):
        super().__init__(brand, model)
        self.operating_system = operating_system

    def run_program(self, program_name):
        if self.is_on:
            print(f"Запущена программа: {program_name}.")
        else:
            print("Ноутбук выключен.")

    def play_game(self, game_name):
        if self.is_on:
            print(f"Запущена игра: {game_name}.")
        else:
            print("Ноутбук выключен.")


phone = MobilePhone("Samsung", "Galaxy S23", "+78005553535")
laptop = Laptop("Apple", "MacBook Pro", "macOS")

print(f"Телефон: {phone.brand} {phone.model}, номер: {phone.phone_number}")
print(f"Ноутбук: {laptop.brand} {laptop.model}, ОС: {laptop.operating_system}")

phone.turn_on()
phone.call("88001234567")
phone.sms("88001234567", "Привет!")
phone.turn_off()

laptop.run_program("VS Code")
laptop.turn_on()
laptop.run_program("VS Code")
laptop.play_game("Baba is you")
laptop.turn_off()
