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

    def set_case(self, bool: bool) -> None:
        self.case = bool


"""НПС"""


@dataclass
class NPCmain:
    name: str = "None"
    surname: str = "None"
    gender: str = "None"
    age: int = 0
    victim: bool = False
    guilty: bool = False
    witness: bool = False
    param: dict = field(default_factory=lambda: {"race": "None"})

    def random_name(self) -> None:
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

    def random_surname(self) -> None:
        self.surname = random.choice(['Бисмарк', 'Мольткер', 'Шлиффен',
                                      'Гинденбург', 'Людендорф',
                                      'Розенберг', 'фон Раух',
                                      'Гнейзенау', 'Борхардт',
                                      'Штайн', 'Веймар', 'Лихтенштейн',
                                      'Блюментал', 'Геннингсен', 'Вайнер',
                                      'Тресков', 'Лютцов', 'Вернер',
                                      'Велленродт'])

    def random_gender(self) -> None:
        self.gender = random.choice(["Мужской", "Женский"])

    def custom_gender(self, input_gender: str) -> None:
        if input_gender == "Мужской":
            self.gender = input_gender
        elif input_gender == "Женский":
            self.gender = input_gender
        else:
            print("Есть только два гендера")
            self.gender = "Мужской"

    def random_age(self) -> None:
        self.age = random.randint(18, 76)

    def custom_age(self, input_age: int) -> None:
        self.gender = input_age

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
class Griffon(NPCmain):
    clan: str = "None"
    param: str = field(default_factory=lambda: {"race": "Гриффон"})
    living_place: Location = field(default_factory=lambda: Location())

    def create_age_num(self) -> None:
        self.age = random.randint(18, 100)

    def random_clan(self) -> None:
        self.clan = random.choice(["Вороны",
                                   "Голуби",
                                   "Безродные"])

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

    def creation_body(self) -> None:
        self.gender = random.choice(["Мужской", "Женский"])
        self.create_clan(random.choice(["Вороны", "Голуби", "Безродные"]))
        self.random_name()
        self.random_surname()
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


"""Улики"""


@dataclass
class Clue:
    name: str = "None"
    type: str = "None"
    descrip: str = "None"
    tool_need: list = field(default_factory=lambda: [])
    owner: NPCmain = field(default_factory=lambda: NPCmain())

    def clue_descrip(self, place_district: str,
                     place_street: str,
                     place_house_num: str) -> str:
        return (" найдена по адрессу: " +
                place_district + " р-н" + " ул." +
                place_street + " д. " +
                place_house_num)

    def set_owner(self, npc: NPCmain):
        self.owner = npc

    def use_tool(self, tool: str):
        pass

    def __eq__(self, npc: NPCmain) -> bool:
        for attr in dir(self.owner):
            if (not callable(getattr(self.owner, attr))
                    and not attr.startswith("__")):
                if getattr(self.owner, attr) != getattr(npc, attr):
                    return False
        return True

    def summary(self, npc) -> str:
        npc_name = self.owner.owner_name()
        npc_surname = {self.owner.surname}
        if self.__eq__(npc) is True:
            return f'Пренадлежит: {npc_name} {npc_surname}'
        else:
            return 'Улика не имеет отношения к проверяемому'


@dataclass
class Print(Clue):
    name: str = "Отпечатки"
    type: str = "prints"
    tool_need: list = field(default_factory=lambda: ["порошок",
                                                     "кисть"])

    def use_tool(self, tool: list):
        nessesary_tools: list = self.tool_need
        for i in self.tool_need:
            if i in tool:
                nessesary_tools.remove(i)
        if len(nessesary_tools) == 0:
            return "Отпечатки собраны"
        else:
            return nessesary_tools

    def create_finger(self):
        self.name += " лап"

    def create_footprints(self):
        self.name += " задних лап"


@dataclass
class Blood(Clue):
    name: str = "Следы крови"
    type: str = "blood"
    tool_need: list = field(default_factory=lambda: ["ватная палочка",
                                                     "пробирка",
                                                     "жидкость"])

    def use_tool(self, tool: list):
        nessesary_tools: list = self.tool_need
        for i in self.tool_need:
            if i in tool:
                nessesary_tools.remove(i)
        if len(nessesary_tools) == 0:
            return "Образцы крови собраны"
        else:
            return nessesary_tools

    def create_wall(self):
        self.name + "на стене"

    def create_floor(self):
        self.name + "с пола"

    def create_weapon(self):
        self.name + "на орудии убийства"


@dataclass
class Note(Clue):
    name: str = "Записка"
    type: str = "note"
    descrip: str = "None"

    def create_note(self, note_text) -> None:
        self.descrip = note_text

    def read_note(self) -> str:
        return self.descrip


@dataclass
class WeaponClue(Clue):
    name: str = "Орудие убийства"
    type: str = "weapon"
    additional_clue: list = field(default_factory=lambda: [])

    def random_name(self) -> None:
        name = random.choice(["кинжал",
                              "дубина",
                              "пистолет"])
        self.name += (": " + name)

    def create_name(self, name: str) -> None:
        self.name += (": " + name)

    def add_clues(self, clue: Clue) -> None:
        self.additional_clue.append(clue)


"""Предметы"""


@dataclass
class Item:
    name: str = "None"
    type: str = "None"
    clues: dict = field(default_factory=lambda: {})

    def create_name(self, name: str) -> None:
        self.name = name

    def create_params(self, params: dict) -> None:
        self.params = params

    def create_clue(self, clue: Clue) -> None:
        self.params[clue.name] = clue


@dataclass
class Weapon(Item):
    type: str = "weapon"
    damage: int = 0
    ammo_type: str = "None"
    ammo_loaded: int = 0


"""Дело"""


@dataclass
class Case:
    name: str = "None"
    motivation: str = "None"
    hour: int = 0
    minutes: int = 0
    clues: list = field(default_factory=lambda: [])
    victim: NPCmain = field(default_factory=lambda: NPCmain())
    guilty: NPCmain = field(default_factory=lambda: NPCmain())
    crime_place: Location = field(default_factory=lambda: Location())
    witnesses: list = field(default_factory=lambda: [])

    def create_NPC(self) -> Griffon:
        npc = Griffon()
        npc.random_gender()
        npc.random_name()
        npc.random_surname()
        npc.random_age()
        npc.random_clan()
        npc.create_body()
        return npc

    def create_victim(self) -> None:
        self.victim = self.create_NPC()
        self.victim.victim = True

    def create_guilty(self) -> None:
        self.guilty = self.create_NPC()
        self.guilty.guilty = True

    def create_custom_name(self, name: str) -> None:
        self.name = name

    def prepare_clues(self, clue: Clue) -> None:
        self.clues.append(clue)


@dataclass
class Murder(Case):
    motivation: str = "Убийство"

    def murder_type(self) -> str:
        return random.choice([" на почве личной неприязни",
                              " на семейно-бытовой почве",
                              " с целью грабежа"])

    def motiv_create(self) -> None:
        self.motivation += self.murder_type()

    def prepare_guilty(self) -> None:
        self.create_victim()
        if self.motivation == "Убийство на семейно-бытовой почве":
            self.create_guilty()
            """Убрать дубликат в отдельный метод,
            на будущее исключить генерирование
            семейной связи в деле перенести её к НПС"""
            if self.victim.gender == "Мужской":
                self.guilty.gender = "Женский"
                self.guilty.random_name()
                self.guilty.surname = self.victim.surname
                self.guilty.age = self.victim.age + random.randint(-2, 2)
            else:
                self.guilty.gender = "Мужской"
                self.guilty.random_name()
                self.guilty.surname = self.victim.surname
                self.guilty.age = self.victim.age + random.randint(-2, 2)
        elif self.motivation != "Убийство на семейно-бытовой почве":
            self.create_guilty()
        else:
            raise ValueError(f'Мотив убиства "{self.motivation}"'
                             + 'неверен или указан с ошибкой')

    def prepare_fingerprints(self) -> Print:
        prints: Print = Print()
        prints.create_finger()
        return prints

    def prepare_footprints(self) -> Print:
        prints: Print = Print()
        prints.create_footprints()
        return prints

    def prepare_weapon(self) -> WeaponClue:
        weapon: WeaponClue = WeaponClue()
        fingerprints: Print = self.prepare_fingerprints()
        fingerprints.owner = self.guilty
        blood: Blood = Blood()
        blood.create_weapon()
        weapon.additional_clue.append(fingerprints)
        weapon.additional_clue.append(blood)
        weapon.random_name()
        weapon.owner = self.guilty
        return weapon

    def random_clue_owner(self, clue: Clue):
        dice = random.randint(0, 1)
        if dice == 0:
            clue.set_owner(self.victim)
        else:
            clue.set_owner(self.guilty)

    def test_create_murder(self):
        self.motiv_create()
        self.prepare_guilty()
        weapon: WeaponClue = self.prepare_weapon()
        self.prepare_clues(weapon)
        if self.clues[0].name == "Орудие убийства: кинжал":
            self.victim.param["torso"] += "\n На теле видна колотая рана"
        elif self.clues[0].name == "Орудие убийства: дубина":
            self.victim.param["head"] += ("\n На голове видны следы"
                                          + "от удара тупым предметом")
        elif self.clues[0].name == "Орудие убийства: пистолет":
            self.victim.param["torso"] += ("\n На теле видны пулевые ранения")
        for i in range(1):
            fingerprints: Clue = self.prepare_fingerprints()
            self.prepare_clues(fingerprints)
        for i in range(1):
            footprints: Clue = self.prepare_footprints()
            self.prepare_clues(footprints)
        for i in self.clues:
            self.random_clue_owner(i)
