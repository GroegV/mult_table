#n = 2
import os
from random import randint
print(f"Таблица умножения на 2:")
for i in range(1, 10):
    print(f"2 x {i} = {2*i}")

input("Нажмите Enter для продолжения...")
    
os.system("cls")

print("Выполните задания:")
for i in range(1, 10):
    answer = input(f"2 x {i} = ")
    if int(answer) == 2*i:
        print("Правильно!")
    else:
        print("Неверно!")