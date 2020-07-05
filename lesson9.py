# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.


# 2. Закодируйте любую строку по алгоритму Хаффмана.

from collections import namedtuple

str = 'а роза упала на лапу азора'


def sort_by_value(d):
    elem_dict = namedtuple('elem', 'node weight leaf')
    out_list = []
    for simb, counter in d.items():
        if len(out_list) == 0:
            out_list = [elem_dict(simb, counter, 1)]
            continue

        for id, into_out_list in enumerate(out_list):
            if into_out_list.weight >= counter:  # Ставим новое значение справо
                out_list.insert(id, elem_dict(simb, counter, 1))
                break

    return out_list


def count_simb(str):
    out_data = {}
    for simb in str:
        if simb not in out_data:
            out_data[simb] = 1
        else:
            out_data[simb] += 1
    print(out_data)
    return sort_by_value(out_data)



def get_code(root, table_code, code_bit=''):
    if not root.leaf:
        get_code(root.node.left, table_code, code_bit)
        get_code(root.node.right, table_code, code_bit)
    else:
        table_code[root.node.left] = root.node.left_cost
        table_code[root.node.right] = root.node.right_cost
    return table_code


def code_haffman(d):
    table_code = {}
    node = namedtuple('node', 'node_int left left_cost l_leaf right right_cost r_leaf')
    elem_dict = namedtuple('elem', 'node weight leaf')

    while len(d) > 1:
        left_branch, count_left, l_leaf = d.pop(0)
        right_branch, count_right, r_leaf = d.pop(0)
        elem_node = node(count_left + count_right, left_branch, 0, l_leaf, right_branch, 1, r_leaf)

        for id, find_elem in enumerate(d):
            if find_elem.weight >= elem_node.node_int:
                d.insert(id, elem_dict(elem_node, elem_node.node_int, 0))
                break

    d.insert(0, elem_dict(elem_node, elem_node.node_int, 0))

    # Проходим по дереву, собираем таблицу хаффмана
    get_code(d[0], table_code)

    print(d)


arr_simb = count_simb(str)
print(arr_simb)
print(code_haffman(arr_simb))
