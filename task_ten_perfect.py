'''
6. Реализовать функцию-валидатор почтовых адресов.
Принимает строку, которая содержит адрес электронной почты.
Возвращает True, если адрес валидный, иначе возвращает False.
Валидным адресом называется такой, который удовлетворяет следующим условиям:

1. Имеет формат username@websitename.extension
2. username может содержать только латинские буквы, целые числа, нижние подчеркивания и тире
3. websitename содержит только латинские буквы и целые числа
'''
from string import ascii_letters, digits

def check_if_email(email: str):
    if '@' in email and '.' in email:
        first_part = email.split('@')[0]
        second_part = email.split('@')[1]
        for symbol in first_part:
            if symbol in ascii_letters or symbol in digits or symbol == '_' or symbol == '-':
                continue
            else:
                return False

        extension = second_part.split('.')[1]
        second_part = second_part.split('.')[0]

        if len(extension) < 4:
            for symbol in second_part:
                if symbol in ascii_letters or symbol in digits:
                    continue
                else:
                    return False
        else:
            return False
    else:
        return False
    return True

def main():
    email = "bigman212@yandex.ru"
    print(email.split('@'))
    print(email.split('@')[1].split('.'))

    print(check_if_email(email))
if __name__ == '__main__':
    main()
