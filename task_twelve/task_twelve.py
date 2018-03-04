'''
2. В одном файле в каждой строке записаны координаты пар точек.
Каждая координата отделена от другой пробелом.
Например, строка вида 3 6 -2 4 означает, что координаты первой точки (3;6), второй - (-2;4).
Во второй файл требуется построчно записать наибольшее и наименьшее расстояние между точками
'''

import math

def rangeCoords(line):

    maxLength = 0

    for i, coordinates in enumerate(line):

        coordinates = line.split()
        coordinates = [int(num) for num in coordinates]

        length = math.sqrt((coordinates[0]+coordinates[2])**2 + (coordinates[1]+coordinates[3])**2)

        if length > maxLength:
            maxLength = length

    return maxLength

def main():

    file = open('coordinates.txt', 'rt')
    line = file.read()
    print(line)

    coords = line.split(' ')
    print('Весь файл: ', coords)

    print(rangeCoords(line))
    file.close()


if __name__ == '__main__':
    main()
