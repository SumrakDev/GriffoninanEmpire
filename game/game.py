import random
from dataclasses import dataclass, field

"""Локации"""


@dataclass
class Location:
    owner: dict = field(default_factory=lambda: {"name": "None",
                                                 "surname": "None"})
    case: bool = False
    district: str = "None"
    street: str = "None"
    house_num: str = "None"
    apartment_num: str = "None"
    clue_in_place: list = field(default_factory=lambda: [])
    item_in_place: list = field(default_factory=lambda: [])

    def create_owner(self, name: str, surname: str) -> None:
        self.owner["name"] = name
        self.owner["surname"] = surname

    def create_district(self, disctrict: str) -> None:
        self.district = disctrict

    def create_street(self, street: str) -> None:
        self.district = street

    def create_house_num(self, num: int) -> None:
        self.house_num = str(num)

    def create_apartment_num(self, num: int) -> None:
        self.apartment_num = str(num)

    def place_clue(self, clue_list: list) -> None:
        self.clue_in_place = clue_list

    def place_items(self, item_list: list) -> None:
        self.item_in_place = item_list


"""НПС"""


@dataclass
class NPC:
    name: str = "None"
    surname: str = "None"
    gender: str = "None"
    age: int = 0
    victim: bool = False
    crimer: bool = False
    witness: bool = False
    param: dict = field(default_factory=lambda: {"race": "None"})

    def create_gender(self) -> str:
        if self.gender == "Мужской":
            return "ого"
        else:
            return "ой"

    def create_color(self) -> str:
        if self.param["race"] == "Гриффон":
            return "белыми "
        elif self.param["race"] == "Волк":
            return "белой "
        elif self.param["race"] == "Змей":
            return "белой "
        else:
            raise ValueError(f'Раса "{self.param["race"]}" неизвестна')

    def create_skin(self) -> str:
        if self.param["race"] == "Гриффон":
            return "перьями "
        elif self.param["race"] == "Волк":
            return "шерстью "
        elif self.param["race"] == "Змей":
            return "чешуёй "
        else:
            raise ValueError(f'Раса "{self.param["race"]}" неизвестна')

    def create_body_part_race(self) -> list:
        if self.param["race"] == "Гриффон":
            return ["гриффона", "гриффоннки"]
        elif self.param["race"] == "Волк":
            return ["волка", "волчицы"]
        elif self.param["race"] == "Змей":
            return ["змея", "змеи"]
        else:
            raise ValueError(f'Раса "{self.param["race"]}" неизвестна')

    def create_body_part_gender(self) -> str:
        list_of_race = self.create_body_part_race()
        if self.gender == "Мужской":
            return list_of_race[0]
        else:
            return list_of_race[1]

    def create_age(self) -> str:
        if self.age <= 35:
            return " молод" + self.create_gender() + " "
        elif self.age > 35 and self.age <= 48:
            return " зрел" + self.create_gender() + " "
        else:
            return " стар" + self.create_gender() + " "

    def create_body_part_owner(self) -> str:
        return self.create_age() + self.create_body_part_gender()

    def create_body(self) -> None:
        self.param["head"] = ("Покрытая " +
                              self.create_color() +
                              self.create_skin() +
                              "голова " +
                              self.create_body_part_owner())
        self.param["neck"] = ("Покрытая " +
                              self.create_color() +
                              self.create_skin() +
                              "шея" +
                              self.create_body_part_owner())
        self.param["torso"] = ("Покрытое " +
                               self.create_color() +
                               self.create_skin() +
                               "туловище" +
                               self.create_body_part_owner())
        self.param["hands"] = ("Покрытые " +
                               self.create_color() +
                               self.create_skin() +
                               "лапы" +
                               self.create_body_part_owner())
        self.param["legs"] = ("Покрытые " +
                              self.create_color() +
                              self.create_skin() +
                              "задние лапы" +
                              self.create_body_part_owner())
        self.param["tail"] = ("Покрытый " +
                              self.create_color() +
                              self.create_skin() +
                              "хвост" +
                              self.create_body_part_owner())

    def explore_body(self, bodypart: str) -> str:
        return self.param[bodypart]

    def owner_name(self) -> str:
        if self.gender == "Мужской":
            return self.name + "у"
        elif self.gender == "Женский":
            return self.name + "е"
        else:
            raise ValueError('Есть только два гендера')

    def test_creation_body(self) -> None:
        self.param["race"] = random.choice(["Гриффон", "Волк", "Змей"])
        self.name = random.choice(["Герхард", "Вульф", "Зигфрид"])
        self.surname = random.choice(["фон Абен", "Хоргольф", "Олафсон"])
        self.gender = random.choice(["Мужской", "Женский"])
        self.age = random.randrange(18, 70)
        self.create_body()
        summary = (f'Имя: {self.name}\n'
                   f'Фамилия: {self.surname}\n'
                   f'Возраст: {self.age}\n'
                   f'Пол: {self.gender}\n'
                   f'Расса: {self.param["race"]}\n'
                   f'-Физические параметры-\n'
                   f'Голова: {self.param["head"]}\n'
                   f'Шея: {self.param["neck"]}\n'
                   f'Туловище: {self.param["torso"]}\n'
                   f'Лапы: {self.param["hands"]}\n'
                   f'Задние лапы: {self.param["legs"]}\n'
                   f'Хвост: {self.param["tail"]}\n')
        print(summary)


@dataclass
class Griffon(NPC):
    clan: str = "None"
    param: str = field(default_factory=lambda: {"race": "Гриффон"})
    living_place: Location = field(default_factory=lambda: Location())

    def create_age_num(self) -> None:
        self.age = random.randint(18, 100)

    def create_clan(self, clan) -> None:
        self.clan = clan

    def create_color(self) -> str:
        if self.clan == "Вороны":
            return "чёрными "
        elif self.clan == "Голуби":
            return "голубыми "
        elif self.clan == "Безродные":
            return "серыми "
        else:
            raise ValueError(f'Клан "{self.clan}" неизвестен')

    def create_name(self) -> None:
        if self.gender == "Мужской":
            self.name = random.choice(["Дитер", "Карл", "Гюнтер",
                                       "Рихард", "Максимилиан", "Кристиан"
                                       ])
        elif self.gender == "Женский":
            self.name = random.choice(["Эрика", "Урсула", "Инге",
                                       "Герта", "Магда", "Регина",
                                       "Берта", "Эдит", "Биргит",
                                       "Констанца"])
        else:
            raise ValueError('Есть только два гендера')

    def create_surname(self) -> None:
        self.surname = random.choice(['Бисмарк', 'Мольткер', 'Шлиффен',
                                      'Гинденбург', 'Людендорф',
                                      'Розенберг', 'фон Раух',
                                      'Гнейзенау', 'Борхардт',
                                      'Штайн', 'Веймар', 'Лихтенштейн',
                                      'Блюментал', 'Геннингсен', 'Вайнер',
                                      'Тресков', 'Лютцов', 'Вернер',
                                      'Велленродт'])

    def test_creation_body(self) -> None:
        self.gender = random.choice(["Мужской", "Женский"])
        self.create_clan(random.choice(["Вороны", "Голуби", "Безродные"]))
        self.create_name()
        self.create_surname()
        self.create_age_num()
        self.create_body()
        summary = (f'Имя: {self.name}\n'
                   f'Фамилия: {self.surname}\n'
                   f'Возраст: {self.age}\n'
                   f'Пол: {self.gender}\n'
                   f'Расса: {self.param["race"]}\n'
                   f'-Физические параметры-\n'
                   f'Голова: {self.param["head"]}\n'
                   f'Шея: {self.param["neck"]}\n'
                   f'Туловище: {self.param["torso"]}\n'
                   f'Лапы: {self.param["hands"]}\n'
                   f'Задние лапы: {self.param["legs"]}\n'
                   f'Хвост: {self.param["tail"]}\n')
        print(summary)


test_griffon = Griffon()
test_griffon.test_creation_body()
print(test_griffon)


"""Улики"""

@dataclass
class Clue:
    name: str = "None"
    type: str = "None"
    descrip: str = "None"
    owner: NPC = field(default_factory=lambda: NPC())

    def clue_descrip(self, place_district: str,
                     place_street,
                     place_house_num: str) -> str:
        return (" найдена по адрессу: " +
                place_district + " р-н" + " ул." +
                place_street + " д. " +
                place_house_num)

    def set_owner(self, npc: NPC):
        self.__dict__["owner"] = npc

    def use_tool(self, tool: str):
        pass

    def __eq__(self, npc: NPC) -> str:

        for attr in dir(self):
            if not callable(getattr(self, attr)) and not attr.startswith("__"):
                if getattr(self, attr) != getattr(npc, attr):
                    return "совпадений не обнаруженно"
        return f'{self.name}: обнаруженно совпадение'

    def name_known(self):
        return f' по имени {self.owner.name}'

    def surname_known(self):
        return f' фамилии {self.owner.surname}'


@dataclass
class Prints(Clue):
    tools: list = field(default_factory=lambda: ["Специальный порошок",
                                                 "Щётка с мягкой щетиной",
                                                 "Плёнка-клей («липучка»)"])

    def clue_type(self, type: str):
        if type == "random":
            self.type = random.choice(["fingerprints",
                                       "legprints"])
        else:
            self.type = type

    def clue_possible_names(self) -> str:
        if self.type == "fingerprints":
            self.name = "отпечаток лап"
            return self.name
        elif self.type == "legprints":
            self.name == "отпечаток обуви"
            return self.name
        else:
            raise ValueError(f'Неверный вид улик: {self.type}')

    def on_item(self) -> None:
        self.type = "fingerprints"

    def on_floor(self) -> None:
        self.type = "legprints"

    def race_known(self):
        if self.owner.param["race"] == "Гриффон":
            return "прендлежит гриффону"

    def name_known(self):
        return f' по имени {self.owner.name}'

    def surname_known(self):
        return f' фамилии {self.owner.surname}'


@dataclass
class Blood(Clue):
    tools: list = field(default_factory=lambda: ["Ножницы",
                                                 "Скребок для сбора скоб",
                                                 "Раствор цитрата натрия",
                                                 "Ватные палочки"])
