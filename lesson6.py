# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
import random
import sys


# 3/3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
def touch_mem(x, dict_mem_adress = {}, _int_mem = 0):
    if id(x) not in dict_mem_adress:
        print(f'type={x.__class__},  + {sys.getsizeof(x)}byte, mem_adress: {id(x)}')
        dict_mem_adress[id(x)] = sys.getsizeof(x)
        return _int_mem+sys.getsizeof(x), dict_mem_adress
    else:
        return _int_mem, dict_mem_adress


def var_1(n):
    array1 = [random.randint(-50, 500) for _ in range(0, n)]
    mem, dict_adress = touch_mem(array1)

    elem_max, pos_max = 0, 0
    elem_min, pos_min = array1[0], 0

    mem, dict_adress = touch_mem(elem_max, dict_adress, mem)
    mem, dict_adress = touch_mem(pos_max, dict_adress, mem)
    mem, dict_adress = touch_mem(elem_min, dict_adress, mem)
    mem, dict_adress = touch_mem(pos_min, dict_adress, mem)

    for pos, elem in enumerate(array1):
        mem, dict_adress = touch_mem(pos, dict_adress, mem)
        elem_max, pos_max = (elem, pos) if elem_max < elem else (elem_max, pos_max)
        elem_min, pos_min = (elem, pos) if elem_min > elem else (elem_min, pos_min)

    array1[pos_min] = elem_max
    array1[pos_max] = elem_min

    print(f"total_mem  = {mem}byte")

    return array1


def var_2(n):
    arr = [random.randint(-50, 500) for _ in range(0, n)]
    mem, dict_adress = touch_mem(arr, {}, 0)

    dict_max_min = {0: arr[0], 1: arr[0], 2: 0, 3: 0}  # arr_min,arr_max,ind_min,ind_max
    mem, dict_adress = touch_mem(dict_max_min, dict_adress, mem)

    for ind, el in enumerate(arr):
        mem, dict_adress = touch_mem(ind, dict_adress, mem)
        if el < dict_max_min[0]:
            dict_max_min[0] = el
            dict_max_min[2] = ind

        if el > dict_max_min[1]:
            dict_max_min[1] = el
            dict_max_min[3] = ind

    arr[dict_max_min[2]], arr[dict_max_min[3]] = arr[dict_max_min[3]], arr[dict_max_min[2]]

    print(f"total_mem  = {mem}byte")
    return arr


def var_3(n):

    array1 = [random.randint(-50, 500) for _ in range(0, n)]
    mem, dict_adress = touch_mem(array1, {}, 0)

    elem_max, pos_max = 0, 0
    elem_min, pos_min = array1[0], 0

    mem, dict_adress = touch_mem(elem_max, dict_adress, mem)
    mem, dict_adress = touch_mem(pos_max, dict_adress, mem)
    mem, dict_adress = touch_mem(elem_min, dict_adress, mem)
    mem, dict_adress = touch_mem(pos_min, dict_adress, mem)

    lenght = len(array1)
    mem, dict_adress = touch_mem(lenght, dict_adress, mem)

    while lenght:
        pos = lenght - 1
        mem, dict_adress = touch_mem(pos, dict_adress, mem)

        if elem_max < array1[pos]:
            elem_max, pos_max = (array1[pos], pos)
            continue
        if elem_min > array1[lenght - 1]:
            elem_min, pos_min = (array1[pos], pos)
        lenght = pos

    array1[pos_min] = elem_max
    array1[pos_max] = elem_min

    print(f"total_mem  = {mem}byte")

    return array1


print(sys.version, sys.platform)
print(f"def var_1")
var_1(10)

print(f"def var_2")
var_2(10)

print(f"def var_3")
var_3(10)

# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;

# 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] win32
# def var_1
# type=<class 'list'>,  + 192byte, mem_adress: 2550869302536
# type=<class 'int'>,  + 24byte, mem_adress: 140724461138160
# type=<class 'int'>,  + 28byte, mem_adress: 140724461143472
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138192
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138224
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138256
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138288
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138320
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138352
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138384
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138416
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138448
# total_mem  = 496byte
# def var_2
# type=<class 'list'>,  + 192byte, mem_adress: 2550872517960
# type=<class 'dict'>,  + 240byte, mem_adress: 2550872512616
# type=<class 'int'>,  + 24byte, mem_adress: 140724461138160
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138192
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138224
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138256
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138288
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138320
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138352
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138384
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138416
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138448
# total_mem  = 708byte
# def var_3
# type=<class 'list'>,  + 192byte, mem_adress: 2550872577288
# type=<class 'int'>,  + 24byte, mem_adress: 140724461138160
# type=<class 'int'>,  + 28byte, mem_adress: 2550872260464
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138480
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138448
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138416
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138384
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138352
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138320
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138288
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138256
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138224
# type=<class 'int'>,  + 28byte, mem_adress: 140724461138192
# total_mem  = 524byte


# d. написать общий вывод: какой из трёх вариантов лучше и почему.

# На мой взгляд использование обычных переменных лучше чем использование словаря переменных, т.к. занимает меньше памяти.
# Что и демонстрирует вывод приведённый выше.
