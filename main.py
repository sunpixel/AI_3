'''Main code file'''

import equation
import traingle_calc

def get_number():
    '''A function that is made to get number from user'''
    a = float(input("Введите значение: "))
    return a

def excercise_1():
    '''First excercise'''
    x = equation.solve_quadratic(get_number(), get_number(), get_number())
    print(x)

def excercise_2():
    '''Second excercise'''
    traingle_calc.triangle(get_number(), get_number(), get_number())

if __name__ == '__main__':
    print('Going main')
    excercise_1()
    print('-' * 20)
    excercise_2()
