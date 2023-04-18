#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число N "))
p = 2

if n > p:
    for i in range (n):
        print(p)
        p *= 2
        if p == n:
            print(p)
            break
        elif p > n:
            break