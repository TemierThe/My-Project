# Игровые классы
CHAR_CLASS_ELF   = "эльф"
CHAR_CLASS_GNOME = "гном"
CHAR_CLASS_OGRE  = "огр"
CHAR_CLASS_HUMAN = "человек"

# Характеристики персонажа (1-3 - низкий, 4-6 - средний, 7-9 - высокий)
char_parameter_strength     = {}  # Сила             = 0
char_parameter_dexterity    = {}  # Ловкость         = 0
char_parameter_constitution = {}  # Телосложение     = 0
char_parameter_intelligence = {}  # Интеллект        = 0
char_parameter_size         = {}  # Размер персонажа = 0

# Уровень персонажа
char_level = 0

# Список оружия, урон (1-3 - низкий, 4-6 - средний, 7-9 - высокий)
char_weapon_sword  = {"Damage": 7}  # Меч, урон    = 7
char_weapon_stuff  = {"Damage": 7}  # Посох, урон  = 7
char_weapon_bow    = {"Damage": 6}  # Лук, урон    = 6
char_weapon_dagger = {"Damage": 4}  # Кинжал, урон = 4
char_weapon_hammer = {"Damage": 8}  # Молот, урон  = 8
char_weapon_axe    = {"Damage": 8}  # Топор, урон  = 8



# Выбор расы Эльфов
def select_race_elf():
    global char_level
    char_level += 1     # Устанавливаем 1 уровень
    char_parameter_strength["Range"], char_parameter_strength["Mode"]         = 4, "Средний"  # Сила - 4              |  {"Range": 4, "Mode": "Средний"}
    char_parameter_dexterity["Range"], char_parameter_dexterity["Mode"]       = 7, "Высокий"  # Ловкость = 7          |  {"Range": 7, "Mode": "Высокий"}
    char_parameter_constitution["Range"], char_parameter_constitution["Mode"] = 4, "Средний"  # Телосложение = 4      |  {"Range": 4, "Mode": "Средний"}
    char_parameter_intelligence["Range"], char_parameter_intelligence["Mode"] = 8, "Высокий"  # Интеллект = 8         |  {"Range": 8, "Mode": "Высокий"}
    char_parameter_size["Range"], char_parameter_size["Mode"]                 = 7, "Высокий"  # Размер персонажа = 7  |  {"Range": 7, "Mode": "Высокий"}

# Выбор расы Гномов
def select_race_gnome():
    global char_level
    char_level += 1     # Устанавливаем 1 уровень
    char_parameter_strength["Range"], char_parameter_strength["Mode"]         = 7, "Высокий"  # Сила - 7              |  {"Range": 7, "Mode": "Высокий"}
    char_parameter_dexterity["Range"], char_parameter_dexterity["Mode"]       = 5, "Средний"  # Ловкость = 5          |  {"Range": 5, "Mode": "Средний"}
    char_parameter_constitution["Range"], char_parameter_constitution["Mode"] = 6, "Средний"  # Телосложение = 6      |  {"Range": 6, "Mode": "Средний"}
    char_parameter_intelligence["Range"], char_parameter_intelligence["Mode"] = 6, "Средний"  # Интеллект = 6         |  {"Range": 6, "Mode": "Средний"}
    char_parameter_size["Range"], char_parameter_size["Mode"]                 = 3, "Низкий"   # Размер персонажа = 3  |  {"Range": 3, "Mode": "Низкий"}

# Выбор расы Огров
def select_race_ogre():
    global char_level
    char_level += 1     # Устанавливаем 1 уровень
    char_parameter_strength["Range"], char_parameter_strength["Mode"]         = 8, "Высокий"  # Сила - 8              |  {"Range": 8, "Mode": "Высокий"}
    char_parameter_dexterity["Range"], char_parameter_dexterity["Mode"]       = 3, "Низкий"   # Ловкость = 3          |  {"Range": 3, "Mode": "Низкий"}
    char_parameter_constitution["Range"], char_parameter_constitution["Mode"] = 8, "Высокий"  # Телосложение = 8      |  {"Range": 8, "Mode": "Высокий"}
    char_parameter_intelligence["Range"], char_parameter_intelligence["Mode"] = 3, "Низкий"   # Интеллект = 3         |  {"Range": 3, "Mode": "Низкий"}
    char_parameter_size["Range"], char_parameter_size["Mode"]                 = 8, "Высокий"  # Размер персонажа = 8  |  {"Range": 8, "Mode": "Высокий"}

# Выбор расы Людей
def select_race_human():
    global char_level
    char_level += 1     # Устанавливаем 1 уровень
    char_parameter_strength["Range"], char_parameter_strength["Mode"]         = 5, "Средний"  # Сила - 5              |  {"Range": 5, "Mode": "Средний"}
    char_parameter_dexterity["Range"], char_parameter_dexterity["Mode"]       = 5, "Средний"  # Ловкость = 5          |  {"Range": 5, "Mode": "Средний"}
    char_parameter_constitution["Range"], char_parameter_constitution["Mode"] = 5, "Средний"  # Телосложение = 5      |  {"Range": 5, "Mode": "Средний"}
    char_parameter_intelligence["Range"], char_parameter_intelligence["Mode"] = 5, "Средний"  # Интеллект = 5         |  {"Range": 5, "Mode": "Средний"}
    char_parameter_size["Range"], char_parameter_size["Mode"]                 = 5, "Средний"  # Размер персонажа = 5  |  {"Range": 5, "Mode": "Средний"}




description_race_elf = """\n Считается, что эльфы тесно связаны с людьми. Они не так распространены или многочисленны, как люди, 
но считаются одной из основных рас. Остроумие и обаяние долгоживущих, ловких эльфов хорошо известны, 
так же как и их непрерывная война с гоблиноидами. Считается, что самым большим недостатком эльфийской расы 
является их низкий интерес к физической работе; эльфы в основном ученые и художники."""

description_race_gnome = """\n Гномы - это раса маленьких гуманоидов, родственных гномам. Гномы отличаются от гномов 
главным образом своей средой обитания и привычками. Они живут в основном в лесах и иногда строят свои дома в подземных шахтах. 
Гномы не так сильно полагаются на физическую работу, как их двоюродные братья гномы, поскольку они чувствуют себя комфортно
с магическими явлениями и рядом с ними. Некоторые гномы являются лучшими магами-искателями приключений и иллюзионистами."""

description_race_ogre = """\n Огры — раса крупных и сильных гуманоидов. Они способны противостоять стихийным бедствиям и ранам.
Хотя они не очень яркие. Ближе всего огры к гению, когда они готовят гения другой расы. Однако это случается очень редко, 
потому что глупость огров позволяет успешному гению обманом выбраться из их котелка. Однако не все огры такие злые. 
И большинство самых предприимчивых огров, как правило, заботятся о своих меньших друзьях. 
Есть много успешных искателей приключений, которые наняли дружелюбного и полезного людоеда в качестве своего тарана."""

description_race_human = """\n Люди — самая распространенная из многочисленных разумных рас, населяющих этот мир. 
Они настолько распространены и многочисленны, что их считают шкалой для других рас. Могут быть некоторые уникальные примеры
экстраординарной внешности, но в основном люди непредсказуемы в том, что их интересует."""


