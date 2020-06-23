import random

# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

natur_digit = [i for i in range(2, 100)]
diap = [i for i in range(2, 10)]
array = {}
for test_digital in diap:
    for _ in natur_digit:
        if _ % test_digital == 0:
            if test_digital in array:
                array[test_digital].append(_)
            else:
                array[test_digital] = []
                array[test_digital].append(_)

for key, list_data in array.items():
    print(f"{key} кратно {len(list_data)} раз.")

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
# (помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
array1 = [random.randrange(100) for _ in range(0, 11)]
array2 = [pos for pos, elem in enumerate(array1) if elem % 2 == 0]

print(array1, array2)

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
array1 = [random.randrange(100) for _ in range(0, 10)]
elem_max, pos_max = 0, 0
elem_min, pos_min = array1[0], 0

for pos, elem in enumerate(array1):
    elem_max, pos_max = (elem, pos) if elem_max < elem else (elem_max, pos_max)
    elem_min, pos_min = (elem, pos) if elem_min > elem else (elem_min, pos_min)

print(array1)
array1[pos_min] = elem_max
array1[pos_max] = elem_min
print(array1)

# 4. Определить, какое число в массиве встречается чаще всего.
array1 = [random.randrange(11) for _ in range(0, 50)]
data = {}
for _ in array1:
    if _ in data:
        data[_] += 1
    else:
        data[_] = 1
print(array1)
max_num, count_max = sorted(data.items(), key=lambda x: x[1]).pop()
print(f"число {max_num} встречается {count_max} раз, максимально.")

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

array1 = [random.randrange(-110, 110) for _ in range(0, 50)]
check_elem = 0

for pos, _ in enumerate(array1):
    if not check_elem and _ < 0:
        elem_max = _
        check_elem = 1

    if check_elem and _ < 0 and _ > elem_max:
        elem_max = _
        pos_max = pos
print(array1)
print(f"максимально отрицательный {elem_max}, его позиция {pos_max}")
