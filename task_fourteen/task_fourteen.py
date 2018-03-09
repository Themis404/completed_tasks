'''
Создать класс Fraction, который должен иметь два поля:
числитель a и знаменатель b. Оба поля должны быть типа int.
Реализовать методы: сокращение дробей, сравнение, сложение и умножение.
'''

class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def comparison(self):
        if self.numerator > self.denominator:
            return self.numerator
        else:
            return self.denominator

    def plus(self):
        self.sum = self.numerator + self.denominator
        return self.sum

    def multiplication(self):
        self.multiply = self.numerator * self.denominator
        return self.multiply

def main():

    num = int(input("Введите первое значение "))
    den = int(input("Введите второе значение "))

    test = Fraction(num, den)

    print("Из двух чисел больше: ", test.comparison())
    print("Сложение: ", test.plus())
    print("Умножение: ", test.multiplication())

if __name__ == '__main__':
    main()