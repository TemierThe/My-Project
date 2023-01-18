import random

number1 = random.randint(1, 100)
random_number = random.randint(1, number1)
correct = False

while correct == False:
    user_number = int(input(f"Угадай число от 1 до {number1}: "))
    if user_number == random_number:
        print ("Ты угадал, молодец")
        correct = True
        break
    if user_number > random_number:
        print ("Твое число больше моего")
        continue
    elif user_number < random_number:
        print ("Твое число меньше моего")
        continue
    else:
        print ("фигня какая-то, вбивай по новой")