def print_params(a, b, c):  # *args, **kwargs
    print(a, b, c)


# * - распаковка позиционных параметров, которые содержат отдельные переменные
# списки, кортежи, множества
# ** - распаковка, запоковка именнованных параметров
# словари

# если хотим передать неопределенное число параметров
# *args-можно менять, например: *params
def print_params(*params):
    print(params)


def print_params_unpack(*params):
    print(*params)

# всегда смотрим сколько параметров ожидает функция
def pr_a_b_c(a, b, c):
    print(a, b, c)


def pr_a_b_c_1(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)

list_1 = [n for n in range(1, 6)]
# упаковка в кортеж
print_params(list_1)
print_params(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# распаковка параметров
print_params_unpack(list_1)
print_params_unpack(1, 2, 3, 4)

# Распаковка параметров
list_2 = [n for n in range(0, 3)]
pr_a_b_c(*list_2)
# если без изменения функции отправить список с меньшим числом
# параметров, то будет ошибка
list_2 = [1, 2]
pr_a_b_c(1, *list_2)
# => 1 1 2
pr_a_b_c(*list_2, 4)
# => 1 2 4

dictinary = {'a': 1, 'b': 2, 'c': 3}
pr_a_b_c(**dictinary)
# Имена ключей должны соответствовать именам параметров
dictinary = {'a': 1, 'b': 2, 'd': 3}
# pr_a_b_c(**dictinary)
# TypeError: pr_a_b_c() got an unexpected keyword argument 'd'
# чтобы это работало меняем параметры на **kwargs
pr_a_b_c_1(**dictinary)

# всегда смотрим сколько параметров ожидает функция
list_2 = [1, 2]
dictinary = {'с': 1}
pr_a_b_c(*list_2, *dictinary)