'''
3. Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк.
Выведите три найденных числа в формате, приведенном в примере.

Пример входного файла:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Пример выходного файла:
Input file contains:
108 letters
20 words
4 lines
'''

from string import ascii_letters

def checkLetters(line):

    amountLetters = 0
    for words in line:
        for letters in words:
            if letters in ascii_letters:
                amountLetters += 1

    return amountLetters

def checkWords(line):

    amountWords = 0
    for words in line:
        amountWords += 1

    return amountWords

def main():

    sumLine = 0
    sumLetters = 0
    sumWords = 0
    text = open('file.txt')

    for numLine, allDate in enumerate(text):

        line = allDate.split()
        sumLetters += checkLetters(line)
        sumWords += checkWords(line)

        if checkWords(line) > 0:
            sumLine += 1

    print('Количество строк в тексте: ', sumLine)
    print('Количество слов в тексте: ', sumWords)
    print('Количество латинских букв в тексте: ', sumLetters)

    text.close()
if __name__ == '__main__':
    main()