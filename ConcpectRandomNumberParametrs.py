# def test_func(*params):
#     print('Type', type(params))
#     print('Argumet',params)
#
# #test_func()
# test_func(1, 2, 3, 4)
#
#
# def summator(txt, *values, type='sum'):
#     s = 0
#     for i in values:
#         s += i
#     return f'{txt} {s} {type}'

def info(value, *types, name_author='Denis', **values):
    print('Type', type(values))
    print('Argumet', values)
    for key, value in values.items():
        print(key, value)
    print(types)

def my_sum(n, *args, txt='Сумма чисел'):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print(txt + ':', s)

# print(summator("Sum of numbers:", 2, 3, 4, type="summator"))
# Важно сохранять порядок
info('Пример использования папраметров всех типов', 2, 3, 4, name_author='Denis', name='Denis', course='Python')
my_sum(1, 1, 2, 3, 4, 5, 6, 7)
my_sum(2, 1, 2, 3, 4, 5, 6, 7, txt = 'Сумма квадратов')
