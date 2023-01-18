import library

# user_name - Ник
# user_race - Раса


user_name = input ("Приветствую тебя путник! Подскажи, как тебя зовут ? ")
print (f"Добро пожаловать в наш Мир, {user_name}")

# Выбор расы
while True:
    user_race = input ("\n Выбери свою расу:\n Эльф | Дворф | Огр | Человек \n\n").lower()
    if user_race == library.CHAR_CLASS_ELF:
        library.select_race_elf()  # Выставление начальных характеристик расы
        print (library.description_race_elf)  # Описание расы
        print (f"\n Ты выбрал расу: {(library.CHAR_CLASS_ELF).upper()}")         
    elif user_race == library.CHAR_CLASS_GNOME:
        library.select_race_gnome()  # Выставление начальных характеристик расы
        print (library.description_race_gnome)  # Описание расы
        print (f"\n Ты выбрал расу: {(library.CHAR_CLASS_GNOME).upper()}") 
    elif user_race == library.CHAR_CLASS_OGRE:
        library.select_race_ogre()  # Выставление начальных характеристик расы
        print (library.description_race_ogre)  # Описание расы
        print (f"\n Ты выбрал расу: {(library.CHAR_CLASS_OGRE).upper()}") 
    elif user_race == library.CHAR_CLASS_HUMAN:
        library.select_race_human()  # Выставление начальных характеристик расы
        print (library.description_race_human)  # Описание расы
        print (f"\n Ты выбрал расу: {(library.CHAR_CLASS_HUMAN).upper()}") 
    else:
        print ("Ты не можешь быть никем, так не пойдет, попытайся вспомнить..")
        continue

    print (f"\n Характеристики расы: \n Уровень силы       | {library.char_parameter_strength['Mode']}  \n Уровень ловкости   | {library.char_parameter_dexterity['Mode']}  \n Твое телосложение  | {library.char_parameter_constitution['Mode']}  \n Уровень интеллекта | {library.char_parameter_intelligence['Mode']}  \n Размер персонажа   | {library.char_parameter_size['Mode']}")
    return_race = input (f"\n Ты будешь играть за расу {user_race}ов ? (да/нет) \n")
    if return_race == "да":

            while True:
                user_weapon = input (f"{(user_race).upper()} {user_name}, выбери себе оружие:\n Меч ({library.char_weapon_sword['Damage']} урона) | Посох ({library.char_weapon_stuff['Damage']} урона) | Лук ({library.char_weapon_bow['Damage']} урона) | Кинжал ({library.char_weapon_dagger['Damage']} урона) | Молот ({library.char_weapon_hammer['Damage']} урона) | Топор ({library.char_weapon_axe['Damage']} урона) \n\n").lower()
                if (user_weapon == "меч" or user_weapon == "посох" or user_weapon == "лук" or user_weapon == "кинжал" or user_weapon == "молот" or user_weapon == "топор"):
                    _ = input (f"Хорошо {user_name}, сейчас я вижу перед собой {user_race}a {library.char_level} уровня с {user_weapon}ом, ты готов отправляться в путь? (да/нет) \n")
                    if _ == "да":
                        print ("\\\\\\\\ WELCOME ///////")
                        break  # Начало игры
                    else:
                        continue
                else:
                    print ("Так не пойдет, без оружия твое приключение может закончиться очень быстро, попробуй выбрать что тебе подойдет.. \n")
                    continue

    elif return_race == "нет":
        continue

    else:
        print ("Ты не можешь быть никем, так не пойдет, попытайся вспомнить..")
        continue
    break 

# Начало игры
# Мы выбрали Ник, Расу, Оружие (урон) и получили уровень


