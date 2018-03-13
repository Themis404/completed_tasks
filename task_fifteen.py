'''
6. Создайте структуру с именем student, содержащую поля:
фамилия и инициалы, номер группы, успеваемость (массив из пяти элементов).
Создать массив из десяти элементов такого типа, упорядочить записи по возрастанию среднего балла.
Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 4 или 5.
'''


class Student:

    def __init__(self, surname, initials, numGroup, mark):
        self.surname = surname
        self.initials = initials
        self.numGroup = numGroup
        self.mark = mark


class Journal:

    def __init__(self, student: Student, journal):
        self.student = student
        self.journal = journal

    def fillJournal(self):
        self.journal = {self.student.surname, self.student.initials, self.student.numGroup, self.student.mark}
        return self.journal

def main():

    surname = input("Введите фамилию")
    initials = input("Введите инициалы")
    numGroup = int(input("Введите номер группы"))
    mark = int(input("Введите успеваемость"))

    journal = Student(surname, initials, numGroup, mark)
    fillLine = Journal(journal)

    print (fillLine.fillJournal())

if __name__ == '__main__':
    main()
