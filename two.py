#task 2
'''
Написать функцию is_year_leap,
принимающую 1 аргумент — год,
и возвращающую True, если год високосный,
и False иначе.
'''

year = int(input("Enter year: "))
def in_year_leap (year):
    if (year%4) == 0:
        return True
    else:
        return False
print (in_year_leap(year))


#task 3
'''
Написать функцию square, принимающую 1 аргумент — сторону квадрата,
и возвращающую 3 значения (с помощью кортежа): периметр квадрата,
площадь квадрата и диагональ квадрата.
'''
print('______________________________________________________________________')
side = int(input("Enter the side of the square"))
def square(side):
    perimetr = int(side*4)
    area = int(side**2)
    diagonal = float(side/(2**(1/2)))
    cortege = ('Perimetr: ', perimetr, 'Area: ', area, 'Diagonal: ', diagonal)
    print(cortege)
square(side)
