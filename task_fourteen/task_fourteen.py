'''
Создать класс Fraction, который должен иметь два поля:
числитель a и знаменатель b. Оба поля должны быть типа int.
Реализовать методы: сокращение дробей, сравнение, сложение и умножение.
'''

class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


class Operations:

    def __init__(self, fraction: Fraction):
        self.fraction_to_operate = fraction

    def get_max(self):
        if self.fraction_to_operate.numerator > self.fraction_to_operate.denominator:
            return self.fraction_to_operate.numerator
        else:
            return self.fraction_to_operate.denominator

    def plus(self):
        return self.fraction_to_operate.numerator + self.fraction_to_operate.denominator

    def multiplication(self):
        return self.fraction_to_operate.numerator * self.fraction_to_operate.denominator

def main():

    num = int(input("Введите первое значение "))
    den = int(input("Введите второе значение "))

    test = Fraction(num, den)
    operTest = Operations(test)
    print("Из двух чисел больше: ", operTest.get_max())
    print("Сложение: ", operTest.plus())
    print("Умножение: ", operTest.multiplication())

if __name__ == '__main__':
    main()