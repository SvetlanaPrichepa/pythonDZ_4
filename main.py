# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi

d = int(input("Введите число для заданной точности числа Пи:\n"))
print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')


# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

number = int(input("Введите число: "))
i = 2
list = []
old = number
while i <= number:
    if number % i == 0:
        list.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} : {list}")

# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.


lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")


