# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100].
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
import random

print('WORK_1')


def bsort(array):
    key = 0
    n = len(array)
    change = 0
    while (True):
        c = 0
        for i in range(n - key - 1):
            j = n - i - 1
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                c += 1
                change += 1
                print(array)
        if c == 0:
            break
    return change


array = [random.randrange(-100, 100) for _ in range(0, 10)]
print(array)
print(bsort(array))
print(array)

# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50]. Выведите на экран исходный и отсортированный массивы.
print('WORK_2')


def sl_sort(alist, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        sl_sort(alist, start, mid)
        sl_sort(alist, mid, end)
        sl_list(alist, start, mid, end)


def sl_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1
    print(alist, start, mid, end)


array = [random.randrange(-100, 100) for _ in range(0, 11)]
print(array)
sl_sort(array, 0, len(array))
print(array)

# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
print('WORK_3')


def max_min(arr):
    x_min, x_max = arr[0], arr[0]
    for _ in arr[1:]:
        if _ > x_max:
            x_max = _
        if _ < x_min:
            x_min = _

    return x_min, x_max


def med_sort(array):
    while len(array) != 1:
        d_min, d_max = max_min(array)
        array.remove(d_min)
        array.remove(d_max)


m = 5
array = [random.randrange(-100, 100) for _ in range(0, (2 * m + 1))]
print(array)
med_sort(array)
print('Медиана', array)
