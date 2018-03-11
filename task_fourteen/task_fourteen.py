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

    def sum_num_and_addend(self, addend):
        self.fraction_to_operate.numerator += addend
        return self.fraction_to_operate.numerator

    def common_divisor(self):
        num_common_divisor = self.fraction_to_operate.numerator
        den_common_divisor = self.fraction_to_operate.denominator

        while num_common_divisor != 0 and den_common_divisor != 0:
            if num_common_divisor > den_common_divisor:
                num_common_divisor = num_common_divisor % den_common_divisor
            else:
                den_common_divisor = den_common_divisor % num_common_divisor

        return den_common_divisor + num_common_divisor



def main():

    num = int(input("Введите числитель "))
    den = int(input("Введите знаменатель "))
    addend = int(input("Число для суммы с числителеем "))

    test = Fraction(num, den)
    operTest = Operations(test)

    print("Дробь: ", num, '/', den)
    print("Сокращение дробей: ", int(num/operTest.common_divisor()), '/', int(den/operTest.common_divisor()))
    print("Из двух чисел больше: ", operTest.get_max())
    print("Сложение числителя и знаменателя: ", operTest.plus())
    print("Умножение: ", operTest.multiplication())
    print("Сложение числителя с новым значением: ", operTest.sum_num_and_addend(addend))
    print("Сложение числителя и знаменателя: ", operTest.plus())

if __name__ == '__main__':
    main()