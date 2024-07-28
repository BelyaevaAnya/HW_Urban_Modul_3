# int() --> int(input())
# float()
# bool()
# str()
# list()
# tuple() - кортеж
# dict()
# set() - множество


print(bool(' '))
print(bool(35))
print(bool(0))
print(bool('asda'))
print(bool(None))
# Примеры неявных преобразований
type = None
if type:
    print('Ok')
print(1)
type = 0
if type:
    print('Ok')
print(2)
# Работает неявное преобразование
type = 1
if type:
    print('Ok')
print(3)

print(list('stroka'))
print(tuple('stroka'))

salary = [2300, 1800, 500, 1234.5324238, 7500.12243]
print(sum(salary), len(salary))
print(round(sum(salary) / len(salary), 2), '- средняя зарплата в компании')
print(round(max(salary), 2), '- макс. зарплата')
print(round(min(salary), 2), '- мин. зарплата')
names = ['Denis', 'Katya', 'Zhenya', 'Max', 'Olya']
zipped = dict(zip(names, salary))
print(zipped['Denis'], '- Denis salary')

# any - проверяет объект и если хотябы 1 объект будет True, функция вернет True
a = [True, False, False]
print(any(a))  # => True
# если
a = [False, False, False]
print(any(a))  # => False
a = [1, 2, 3]
print(any(a))  # => True
a = [0, 0, 0]
print(any(a))  # => False
a = '0'
print(any(a))  # => True
a = ''
print(any(a))  # => False
# all - если все элементы True =>True, если хотя бы 1 элемент False => False
a = [0, 1, 1]
print(all(a))  # => False
a = [1, 1, 1]
print(all(a))  # => True
b = ''
# Интроспекция в Python
#  интроспекция — это способность объекта во время выполнения получить
#  тип, доступные атрибуты и методы, а также другую информацию,
#  необходимую для выполнения дополнительных операций с объектом.

print(isinstance(a, str))  # => False
print(isinstance(b, str))  # => True
b1 = ''
# print(type(b1) == str)  # TypeError: 'int' object is not callable
d = [1, 1, 1]
c1 = d
c1[0] = 2   # => изменения внесены и в список с1 и в d
print(id(a))
print(c1)
print(d)
# =>
# [2, 1, 1]
# [2, 1, 1]
print(id(d))
print(id(c1))
print(a is d)  # => False
print(id(3))    # => 140703907576312
print(id(3))    # => 140703907576312
print(c1 is d)  # => True
# помощь с функциями
# print(help(print()))

def helper():
    """
    Эта функция-помощник
    """
    pass

print(help(helper()))
print(help.__doc__(helper))