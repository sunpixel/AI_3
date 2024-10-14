'''Function performs math operations'''

def tab_func(a = 2, b = 4, c = 0.5, func = lambda x: x ** 2 + 3 * x + 2):
    # a - начальная
    # b - конечная
    # c - шаг
    # func - функция при желании
    '''Function will do math'''

    x = a
    while x <= b:
        result = func(x)
        print(f"f({x}) = {result:.2f}")
        x += c
