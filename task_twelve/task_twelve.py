'''
2. В одном файле в каждой строке записаны координаты пар точек.
Каждая координата отделена от другой пробелом.
Например, строка вида 3 6 -2 4 означает, что координаты первой точки (3;6), второй - (-2;4).
Во второй файл требуется построчно записать наибольшее и наименьшее расстояние между точками
'''

import math

def rangeCoords(coords: list):

    coords = [int(num) for num in coords]

    length = math.sqrt((coords[0]-coords[2])**2 + (coords[1]-coords[3])**2)

    return length


def main():

    maxLength = 0
    file = open('coordinates.txt', 'rt')


    for line in file:

        coords = line.split()
        length = rangeCoords(coords)
        print('Координаты двух точек: ', coords)

        if length > maxLength:
            maxLength = length

    print(maxLength)
    file.close()


if __name__ == '__main__':
    main()
