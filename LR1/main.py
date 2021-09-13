import sys
import math

def getcf(index, string):
    """
    Ввод коэффициентов из командной строки или с клавиатуры
    :param index: номер параметра в ком. строке
    :param string: приглашение для ввода коэффициента
    :return: коэффициент уравнения
    """
    try:
        str_cf = sys.argv[index]
        cf = float(str_cf)
    except:
        while True:
            print(string)
            str_cf = input()
            try:
                cf = float(str_cf)
            except ValueError:
                print('Input error')
            else:
                break
    return cf

def roots(a, b, c):
    """
    Вычисление корней уравнения
    :param a: коэффициент А
    :param b: коэффициент В
    :param c: коэффициент С
    :return: множество корней
    """
    d = b*b - 4*a*c
    res = set()
    if d == 0:
        t = (-b / (2*a))
        if t >= 0:
            res.add(math.sqrt(d))
            res.add(-math.sqrt(d))
    elif d > 0:
        t1 = (-b + math.sqrt(d))/(2*a)
        if t1 >= 0:
            res.add(math.sqrt(t1))
            res.add(-math.sqrt(t1))
        t2 = (-b - math.sqrt(d))/(2*a)
        if t2 >= 0:
            res.add(math.sqrt(t2))
            res.add(-math.sqrt(t2))
    return res

def main():
# Ввод коэффициентов
    a = getcf(1, 'Enter A: ')
    while a == 0:
        print('Input Error')
        a = getcf(1, 'Enter A: ')
    b = getcf(2, 'Enter B: ')
    c = getcf(3, 'Enter C: ')

#Вычисление корней
    rts = roots(a, b, c)
    if len(rts) == 0:
        print('No roots')
    elif len(rts) == 1:
        print('x =', rts.pop())
    else:
        for i,x in enumerate(rts):
            print('x{}'.format(i+1), '=', x)

if __name__ == "__main__":
    main()

