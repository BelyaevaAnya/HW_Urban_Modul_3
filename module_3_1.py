# Задача "Счётчик вызовов":
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция.
# К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
# Давайте реализуем данную фишку самостоятельно!
def count_calls():
    global calls
    calls += 1


def string_info(str_):
    count_calls()
    len_val = len(str_)
    str_l = str_.lower()
    str_u = str_.upper()
    str_tuple = (len_val, str_u, str_l)
    return str_tuple


def is_contains(str_, list_substr):
    count_calls()
    str_ = str_.lower()
    list_substr = map(lambda x: x.lower(), list_substr)
    find_flag = False
    for sub_str in list_substr:
        try:
            str_.index(sub_str)
        except ValueError:
            find_flag |= False
        else:
            find_flag |= True
    return find_flag


calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
# =>
# (8, 'CAPYBARA', 'capybara')
# (10, 'ARMAGEDDON', 'armageddon')
# True
# False
# 4
