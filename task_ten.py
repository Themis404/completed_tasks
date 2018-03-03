'''
6. Реализовать функцию-валидатор почтовых адресов.
Принимает строку, которая содержит адрес электронной почты.
Возвращает True, если адрес валидный, иначе возвращает False.
Валидным адресом называется такой, который удовлетворяет следующим условиям:

1. Имеет формат username@websitename.extension
2. username может содержать только латинские буквы, целые числа, нижние подчеркивания и тире
3. websitename содержит только латинские буквы и целые числа
4. Максимальная длина extension 3 символа.
'''

def firstIdentification(email, countDog, countPoint):

    for letter in email:

        if letter == '@':
            countDog += 1

        if letter == '.':
             countPoint += 1

    if (countPoint and countDog) != 1:
        return False

def identificationStart(email):

    for i, letter in enumerate(email):

        if letter != '@':

            if (letter.isalnum()) or (letter == '_') or (letter == '-'):
                print('start')
            else:
                return False
        else:
            return True

def identificationMiddle(email):

    afterDog = len(email)

    for i, letter in enumerate(email):

        if letter == '@':
            afterDog = i

        if i > afterDog:

            if letter != '.':

                if letter.isalnum():
                    print('mid')
                else:
                    return False
            else:
                return True

def identificationEnd(email, countEnd):

    afterPoint = len(email)

    for i, letter in enumerate(email):

        if letter == '.':
            afterPoint = i

        if i > afterPoint and letter.isalnum():
            countEnd += 1

    if countEnd == 3:
        return True
    else:
        return False

def main():

    countEnd = 0
    countDog = 0
    countPoint = 0

    #email = input("Введите адрес электронной почты: ")
    email = 'legen_waitforit_dary@mail.rus'

    if (identificationStart(email) == False) or (identificationEnd(email, countEnd) == False) or (identificationMiddle(email) == False) or (firstIdentification(email, countDog, countPoint) == False):
        print("Неверный адрес")
    else:
        print("Корректный адреес")

if __name__ == '__main__':
    main()
#legen_waitforit_dary@mail.rus