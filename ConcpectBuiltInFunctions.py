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
print(round(sum(salary)/len(salary), 2),'- средняя зарплата в компании')
print(round(max(salary), 2),'- макс. зарплата')
print(round(min(salary), 2),'- мин. зарплата')
names = ['Denis', 'Katya', 'Zhenya', 'Max', 'Olya']
zipped = zip(names, salary)
print(list(zipped))
zipped = dict(zipped)
print(zipped)