# Результаты анализа сохранить в виде комментариев в файле с кодом.
# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.
import random


# 3/3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
def var_1(n):
    array1 = [random.randint(-50, 500) for _ in range(0, n)]

    elem_max, pos_max = 0, 0
    elem_min, pos_min = array1[0], 0

    for pos, elem in enumerate(array1):
        elem_max, pos_max = (elem, pos) if elem_max < elem else (elem_max, pos_max)
        elem_min, pos_min = (elem, pos) if elem_min > elem else (elem_min, pos_min)

    array1[pos_min] = elem_max
    array1[pos_max] = elem_min

    return array1


def var_2(n):
    arr = [random.randint(-50, 500) for _ in range(0, n)]

    arr_min = arr[0]
    arr_max = arr[0]
    ind_min = 0
    ind_max = 0

    for ind, el in enumerate(arr):
        if el < arr_min:
            arr_min = el
            ind_min = ind

        if el > arr_max:
            arr_max = el
            ind_max = ind

    arr[ind_min], arr[ind_max] = arr[ind_max], arr[ind_min]

    return arr


def var_3(n):
    array1 = [random.randint(-50, 500) for _ in range(0, n)]
    elem_max, pos_max = 0, 0
    elem_min, pos_min = array1[0], 0
    lenght = len(array1)
    while lenght:
        pos = lenght - 1
        if elem_max < array1[pos]:
            elem_max, pos_max = (array1[pos], pos)
            continue
        if elem_min > array1[lenght - 1]:
            elem_min, pos_min = (array1[pos], pos)
        lenght = pos

    array1[pos_min] = elem_max
    array1[pos_max] = elem_min

    return array1


# -n 1000 -s"import lesson4" "lesson4.var_1(100)"
# 1000 loops, best of 5: 429 usec per loop
# -n 1000 -s"import lesson4" "lesson4.var_2(100)"
# 1000 loops, best of 5: 394 usec per loop
# -n 1000 -s"import lesson4" "lesson4.var_3(100)"
# 1000 loops, best of 5: 398 usec per loop

# -n 1000 -s"import lesson4" "lesson4.var_1(500)"
# 1000 loops, best of 5: 2.21 msec per loop
# -n 1000 -s"import lesson4" "lesson4.var_2(500)"
# 1000 loops, best of 5: 2.02 msec per loop
# -n 1000 -s"import lesson4" "lesson4.var_3(500)"
# 1000 loops, best of 5: 2.06 msec per loop

# -n 1000 -s"import lesson4" "lesson4.var_1(1000)"
# 1000 loops, best of 5: 3.72 msec per loop
# -n 1000 -s"import lesson4" "lesson4.var_2(1000)"
# 1000 loops, best of 5: 4.11 msec per loop
# -n 1000 -s"import lesson4" "lesson4.var_3(1000)"
# 1000 loops, best of 5: 4.1 msec per loop

# Вывод: Никакой из методов не даёт преймуществ. Все варианты работают одинаково.


# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2

def sieve(n):
    def isPrime(n):
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        return d * d > n

    i = 2
    num = 1
    while True:
        if isPrime(i):
            if n == num:
                break;
            num += 1

        i += 1

    return i


def prime(n):
    i = 2
    num = 1
    from math import sqrt
    lst = [i]
    i+=1
    while True:
        # for i in range(3, n + 1, 2):
        if n == num:
            break
        if (i > 10) and (i % 10 == 5):
            i += 2
            continue
        for j in lst:
            if j > int((sqrt(i)) + 1):
                lst.append(i)
                num += 1
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
            num += 1
        i += 2

    return lst[n-1]

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# -n 100 -s"import lesson4" "lesson4.sieve(10)"
# 100 loops, best of 5: 22.4 usec per loop
# -n 100 -s"import lesson4" "lesson4.sieve(100)"
# 100 loops, best of 5: 650 usec per loop
# -n 100 -s"import lesson4" "lesson4.sieve(1000)"
# 100 loops, best of 5: 18.1 msec per loop

# -n 100 -s"import lesson4" "lesson4.prime(10)"
# 100 loops, best of 5: 41.6 usec per loop
# -n 100 -s"import lesson4" "lesson4.prime(100)"
# 100 loops, best of 5: 1.15 msec per loop
# -n 100 -s"import lesson4" "lesson4.prime(1000)"
# 100 loops, best of 5: 26.7 msec per loop

