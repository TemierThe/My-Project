import random

random_number1 = random.randrange(50, 100, 2)
random_number2 = random.randrange(0, 50, 2)

random_dict = random.choice(['+', '-', '*'])
result = 0

for i in range(1, 6):
    random_number1 = random.randrange(0, 100, 2)
    random_number2 = random.randrange(0, 50, 2)
    random_dict = random.choice(['+', '-', '*'])
    
    user_question = int(input(f"Вопрос {i}) {random_number1} {random_dict} {random_number2} = ... "))
    if random_dict == '+':
        sum_number = random_number1 + random_number2
        if user_question == sum_number:
            print ("Ответ верен")
            result += 1
            continue
        else:
            print ("Ответ неверен")
            continue

    elif random_dict == '-':
        sum_number = random_number1 - random_number2
        if user_question == sum_number:
            print ("Ответ верен")
            result += 1
            continue
        else:
            print ("Ответ неверен")
            continue

    elif random_dict == '*':
        sum_number = random_number1*random_number2
        if user_question == sum_number:
            print ("Ответ верен")
            result += 1
            continue
        else:
            print ("Ответ неверен")
            continue
print (f"Количество верных ответов: {result}")
if result == 5:
    print ("Отлично справился")
elif result == 4:
    print ("Хорошо справился")
elif result == 3:
    print ("3 из 5, хорошо")
elif result == 2:
    print ("2 из 5, могло быть и лучше")
elif result == 1:
    print ("1 из 5, могло быть и лучше")
else:
    print ("ты главное не отчаивайся")
