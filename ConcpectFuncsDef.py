def print_params(a, b, c):
    print(a, b, c)


def print_params_1(*, a, b, c):
    print(a, b, c)


def print_params_2(a, b, *, c):
    print(a, b, c)


print_params(1, 2, 3)
print_params('True', True, 1.1)
print_params(b=1, a=2.2, c="string")

print_params_1(a=1, b=1, c=2)
print_params_2(1, 2, c = 3)
