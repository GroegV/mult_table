import os
from random import randint
for n in range(2, 11):
    print(f"Таблица умножения на {n}:")
    for i in range(1, 10):
        print(f"{n} x {i} = {n*i}")

    input("Нажмите Enter для продолжения...")
    
    os.system("cls")

    print("Выполните задания:")
    for i in range(1, 10):
       answer = input(f"{n} x {i} = ")
       if int(answer) == n*i:
            print("Правильно!")
       else:
           print("Неверно!")
