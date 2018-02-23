#task 2
'''
Написать функцию is_year_leap,
принимающую 1 аргумент — год,
и возвращающую True, если год високосный,
и False иначе.
'''


def in_year_leap(year):
    if (year%4) == 0:
        return True
    else:
        return False



#task 3
'''
Написать функцию square, принимающую 1 аргумент — сторону квадрата,
и возвращающую 3 значения (с помощью кортежа): периметр квадрата,
площадь квадрата и диагональ квадрата.
'''

def perimetr(side):
    perimetr_ = int(side*4)
    return perimetr_

def area(side):
    area_ = int(side**2)
    return area_

def diagonal(side):
    diagonal_ = float(side/(2**(1/2)))
    return diagonal_

def main():
    year = int(input("Enter year: "))
    print(in_year_leap(year))
    print('______________________________________________________________________')
    side = int(input("Enter the side of the square"))
    cortege = ('Perimetr: ', perimetr(side), 'Area: ', area(side), 'Diagonal: ', diagonal(side))
    print(cortege)

if __name__ == '__main__':
    main()