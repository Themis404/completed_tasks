'''
7.Определим слова в хэштеге. Дана строка,
начинается с # и содержит набор слов соединенных в одну строку без пробелов.
Срока описана в стиле camelCase,
то есть первое слово начинается с прописной буквы,
а каждое следующее с заглавной. Например: #приветКакДела,
#меняЗовутЕгорМнеМногоЛет и тд.
Необходимо посчитать количество слов в
строке и вывести количество этих слов.
'''


def main():
    words = []
    first = 0
    sum_words = 1
    text = str(input("Введите хэштег "))

    for i, letter in enumerate(text):

        if letter.isupper():

             sum_words += 1
             last = i
             words.append(text[first:last])
             first = i

    last = i+1
    words.append(text[first:last])

    print(words)


    print(text, "  ", sum_words)

if __name__ == '__main__':
    main()