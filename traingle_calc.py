'''Code file made to get smth out of triangle'''

def straight_angle(a, b, c):
    """Проверяет, является ли угол прямым."""
    if a ** 2 == b ** 2 + c ** 2:
        return True
    else:
        return False

def sharp_angle(a, b, c):
    """Проверяет, является ли угол острым."""
    if a ** 2 < b ** 2 + c ** 2:
        return True
    else:
        return False

def wide_angle(a, b, c):
    """Проверяет, является ли угол тупым."""
    if a ** 2 > b ** 2 + c ** 2:
        return True
    else:
        return False

def main_checks(a, b, c):
    """Выполняет стандартные проверки."""
    arguments = sorted((a, b, c), reverse=True)
    print(arguments)

    if a == b == c:
        return 0
    elif (a == b or b == c or a == c):
        if straight_angle(*arguments):
            return 10
        elif wide_angle(*arguments):
            return 11
        else:
            return 1
    else:
        if sharp_angle(*arguments):
            return 2
        elif wide_angle(*arguments):
            return 3
        elif straight_angle(*arguments):
            return 4

def triangle_possible(a, b, c):
    """Проверяет возможность существования треугольника."""
    # Если большая сторона треугольника меньше суммы двух других сторон,
    # значит треугольник существует.
    arg = tuple(sorted((a, b, c), reverse=True))
    print(arg)
    if arg[0] <= arg[1] + arg[2]:
        return True
    else: return False

def triangle(a, b, c):
    """Основная функция."""
    # 0 - все стороны равны
    # 1 - 2 стороны равны
    # 2 - острый угол
    # 3 - тупой угол
    # 4 - прямой угол
    # 10 - прямоугольный равнобедренный
    # 11 - равнобедренный с тупым углом
    #
    if triangle_possible(a, b, c):
        string = ' треугольник'
        triangle_type = main_checks(a, b, c)
        match triangle_type:
            case 0:
                print("Равносторонний" + string)
            case 1:
                print("Равнобедренный" + string)
            case 2:
                print('Остроугольный'+ string)
            case 3:
                print('Тупоугольный' + string)
            case 4:
                print('Прямоугольный' + string)
            case 10:
                print('Равнобедерненный' + string + 'с прямым углом')
            case 11:
                print('Равнобедренный' + string + 'с тупым углом')
    else:
        print("Такой треугольник невозможен.")
