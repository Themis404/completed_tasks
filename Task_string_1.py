'''
1.Дана строка, состоящая из слов,
разделенных пробелами. Определите,
сколько в ней слов.
'''

def main():
    words = 1
    string_ = input("Введите текст: ")
    length_ = len(string_)
    print("Количество символов: ", length_)

    while length_ > 0:
        for i in string_[length_-1]:

            if (string_[length_-1] == ' ') and (string_[length_-2] != ' '):
                length_ -= 1
                words += 1
            else:
                length_ -= 1

    print("Вывод строки: ", string_)
    print("Колличество слов: ", words)

if __name__ == '__main__':
    main()