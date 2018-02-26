'''
4.Найти все уникальные элементы в списке.
Список произвольной длины и может состоять как из чисел,
так и строк.
'''

def main():

    #line = list(input("Введите текст"))
    line = ['привет', 'привет', 'глеб', 'привет', 'как', 'твои', 'дела', 'глеб']
    #line = ['привет', 'привет', 'привет', 'глеб', 'привет', 'как', 'твои', 'дела', 'глеб']
    print(line)
    for letter in line:
        if line.count(letter) > 1:
            for i in range(line.count(letter)-1):
                line.remove(letter)
    print(line)

if __name__ == '__main__':
    main()