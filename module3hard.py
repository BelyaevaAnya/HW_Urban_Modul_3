data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


# 1 вариант решения
# функция полностью отражает критерии указанные в задании
def calculate_structure_sum_1(*data):
    """
    Функция обрабатывает поступающую в нее струтуру *data и считает
    ее сумму элементов(для str используется длинна str)
    :param data: *data- структура состоящая из списков, множеств, кортежей,
     словарей и переменных с типом данных str и int(boolean и float функцией не предусмотрены)
    :return: summ_of_elements(int)-сумма элементов структуры
    """
    summ_of_elements = 0
    for items in data:
        # Список
        if isinstance(items, list):
            for element in items:
                summ_of_elements += calculate_structure_sum_1(element)
        # Множество
        elif isinstance(items, set):
            for element in items:
                summ_of_elements += calculate_structure_sum_1(element)
        # Кортеж
        elif isinstance(items, tuple):
            for element in items:
                summ_of_elements += calculate_structure_sum_1(element)
        # Словарь
        elif isinstance(items, dict):
            for key, value in items.items():
                summ_of_elements += calculate_structure_sum_1(key, value)
        # Строка
        elif isinstance(items, str):
            summ_of_elements += len(items)
        # Целое число
        elif isinstance(items, int):
            summ_of_elements += items
    return summ_of_elements


# 2 вариант функции
#
# исключает множественное ветвление на if elif(структура match-case)
# использует для определения типа функции непосредственно типов

def calculate_structure_sum_2(*data):
    """
    Функция обрабатывает поступающую в нее струтуру *data и считает
      ее сумму элементов(для str используется длинна str)
    :param data: *data- структура состоящая из списков, множеств, кортежей,
       словарей и переменных с типом данных str и int(boolean и float функцией не предусмотрены)
    :return: summ_of_elements(int)-сумма элементов структуры
    """
    summ = 0
    for items in data:
        match (items):
            case list():
                for element in items:
                    summ += calculate_structure_sum_2(element)
            case tuple():
                for element in items:
                    summ += calculate_structure_sum_2(element)
            case set():
                for element in items:
                    summ += calculate_structure_sum_2(element)
            case dict():
                for key, value in items.items():
                    summ += calculate_structure_sum_2(key, value)
            case str():
                summ += len(items)
            case int():
                summ += items
        continue
    return summ


print(help(calculate_structure_sum_1))
print(help(calculate_structure_sum_2))
result = calculate_structure_sum_1(data_structure)
result2 = calculate_structure_sum_2(data_structure)
print(result)
print(result2)
