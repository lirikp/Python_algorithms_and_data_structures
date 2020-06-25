# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.
from collections import defaultdict, OrderedDict, deque

# ООО "Ромашка", 19901
# ОАО "Барсук", 20000
# МП "Муравей", 15000
# ООО "Мохнатка", 14000

collect = True
d_proj = defaultdict(list)
total_profit = 0
while collect:
    data_input = input(
        'Введите данные через запятую в виде: Название предприятия, прибыль за 4ре квартала или "0" выход: ')
    if data_input == '0':
        break;
    spam = data_input.split(', ')
    if len(spam) == 2:
        profit = int(spam[1])
        d_proj[spam[0]].append(profit)
        total_profit += profit
    else:
        print('Данные не распознаны, попробуйте ещё раз')

avg_profit = total_profit / len(d_proj)
ordered_profit = OrderedDict(sorted(d_proj.items(), key=lambda x: x[1]))

for name, profit in d_proj.items():
    if profit[0] < avg_profit:
        print(f'{name} --- {profit[0]} < {avg_profit}')
    else:
        print(f'{name} --- {profit[0]} > {avg_profit}')


# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

def break_hex(hex):
    isset_hex = deque('0123456789abcdef')
    l = 0
    for simb in hex:
        if simb in isset_hex:
            l += 1

    if l == len(hex):
        return True
    else:
        return False


while True:
    hex_trans = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, "b": 11,
                 "c": 12, "d": 13, "e": 14, "f": 15}
    hexS_user = deque(maxlen=2)
    for i in range(1, 3):
        while True:
            hex_user = deque(input(f'Введите {i}ое HEX число: ')[::-1])
            digit_integer = 0
            if break_hex(hex_user):
                for key, val in enumerate(hex_user):  # Переводим в десятичную систему исчисления
                    digit_integer += hex_trans[val] * (16 ** key)
                hexS_user.append(digit_integer)
                break
            else:
                print("Введённые данные не соответствует HEX числу, может только содержать набор: 0123456789abcdef ")

    while True:
        oper = input('Выберете операцию "+" "*" или X для выхода: ')
        if oper == 'X':
            exit(0)
        elif oper == '+':
            print("0x%0.2X" % (hexS_user[0] + hexS_user[1]))
            break
        elif oper == '*':
            print("0x%0.2X" % (hexS_user[0] * hexS_user[1]))
            break
    exit_state = input('X для выхода: ')

    if exit_state == 'X':
        break
