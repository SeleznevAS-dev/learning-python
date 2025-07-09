# 1.1. 
# Программа 1: Мессенджер
# Классы:
# 1) Пользователь: имя, фамилия, номер телефона, фото профиля, айди
# 2) Чат: название, список участников, дата создания, тип (личный, групповой, канал), создатель чата
# 3) Сообщение: текст, отправитель, ссылка на чат получателя, время отправки, статус прочтения, вложения, тип (текст, голосовое)

# Программа 2: Приложение для доставки пиццы
# Классы:
# 1) Пользователь: имя, фамилия, номер телефона, айди, список адресов, привязанные карты для оплаты, бонусы, настройки
# 2) Продукт (пицца): состав, цена, доступные размеры для заказа, время приготовления
# 3) Заказ: продукты, адрес доставки, способ оплаты, статус заказа, время создания, итоговая стоимость

# Программа 3: Браузер
# Классы:
# 1) Страница: имя, ссылка, содержимое, иконка, кэш 
# 2) Профиль: имя пользователя, настройки, закладки, история посещений, сохраненные пароли, загрузки
# 3) Поисковая строка: текст запроса, история поиска, автодополнение, поисковая система по умолчанию

# 1.2.
class FireMode:
    type: str
    rate_of_fire: int
    is_automatic: bool


class Weapon:
    name: str
    damage: int
    ammo: int
    max_ammo: int
    range: int
    fire_mode: FireMode | None


class Player:
    nickname: str
    health: int
    level: int
    experience: int
    weapon: Weapon | None
    kills: int


single_mode = FireMode()
single_mode.type = "Single"
single_mode.rate_of_fire = 1
single_mode.is_automatic = False

sniper_rifle = Weapon()
sniper_rifle.name = "Sniper rifle"
sniper_rifle.damage = 60
sniper_rifle.ammo = 10
sniper_rifle.max_ammo = 10
sniper_rifle.range = 500
sniper_rifle.fire_mode = single_mode

player1 = Player()
player1.nickname = "Player"
player1.level = 3
player1.experience = 800
player1.weapon = sniper_rifle

print(f"Игрок: {player1.nickname}, Уровень: {player1.level}")
print(
    f"Оружие: {player1.weapon.name}, Урон: {player1.weapon.damage}, Режим стрельбы: {player1.weapon.fire_mode.type}"
)

ak47_mode = FireMode()
ak47_mode.type = "Automatic"
ak47_mode.rate_of_fire = 10
ak47_mode.is_automatic = True

ak47 = Weapon()
ak47.name = "AK-47"
ak47.damage = 35
ak47.ammo = 30
ak47.max_ammo = 30
ak47.range = 250
ak47.fire_mode = ak47_mode

player2 = Player()
player2.nickname = "NewPlayer"
player2.level = 1
player2.experience = 0
player2.weapon = ak47
print(f"Игрок: {player2.nickname}, Уровень: {player2.level}")
print(
    f"Оружие: {player2.weapon.name}, Урон: {player2.weapon.damage}, Режим стрельбы: {player2.weapon.fire_mode.type}"
)

# 1.3.
player2.weapon = player1.weapon

print(f"Количество патронов игрока 1: {player1.weapon.ammo}")
print(f"Количество патронов игрока 2: {player1.weapon.ammo}")
player1.weapon.ammo -= 5

print(f"Количество патронов игрока 1: {player1.weapon.ammo}")
print(f"Количество патронов игрока 2: {player2.weapon.ammo}")