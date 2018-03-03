'''Даны два списка произвольной длины каждый.
Списки могут содержать как числа, так и строки.
Необходимо вывести только те элементы,
которые входят как первый список, так и во второй'''

def main():

    list1 = ['привет', '123', '321', 'как', 'дела', 'дела', '111']
    list2 = ['132', 'привет', 'как', 'твои', 'дела', 'милый', 'друг', '777', 'друг']
    print('Первый список без изменений: ', list1)
    print('Второй список без изменений: ', list2)

    for words in list1:
        while list1.count(words) > 1:
            list1.remove(words)
    print('Первый список с исключением повтора слов: ', list1)

    for words2 in list2:
        while list2.count(words2) > 1:
            list2.remove(words2)
    print('Второй список с исключением повтора слов: ', list2)

    list1.extend(list2)
    print('Два списка в одном: ', list1)

    list2.clear()

    for words in list1:
        while list1.count(words) > 1:
            list2.append(words)
            list1.remove(words)
    print('Искомые повторения из двух списков: ', list2)

if __name__ == '__main__':
    main()