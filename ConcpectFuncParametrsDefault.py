# Значение парметров поумолчнаию указываются только для конечных параметров
# Только последние параметры могут иметь значения поумолчанию
# Пример: def func_with_params(a, b = 2):

# В качестве параметров указываются неизменяемые объекты

def func_with_params(a=2, b=2):
    print(a + b)


def func_with_params_1(a, b=2):
    print(a + b)


def func_with_params_2(a, b=2, c=[]):
    c.append(a)
    print(a + b)
    print(c)


def func_with_params_3(a, b=2, c=None):
    if c is None:
        c = []
        c.append(a)
    print(c)


func_with_params(3, 3)
func_with_params()
func_with_params()
func_with_params()

func_with_params_1(5)

func_with_params_2(5)
func_with_params_2(5)
func_with_params_2(5)

func_with_params_3(5)
func_with_params_3(5)
func_with_params_3(5)
