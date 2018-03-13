'''
6. �������� ��������� � ������ student, ���������� ����:
������� � ��������, ����� ������, ������������ (������ �� ���� ���������).
������� ������ �� ������ ��������� ������ ����, ����������� ������ �� ����������� �������� �����.
�������� ����������� ������ ������� � ������� ����� ���������, ������� ������, ������ ������ 4 ��� 5.
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

    surname = input("������� �������")
    initials = input("������� ��������")
    numGroup = int(input("������� ����� ������"))
    mark = int(input("������� ������������"))

    journal = Student(surname, initials, numGroup, mark)
    fillLine = Journal(journal)

    print (fillLine.fillJournal())

if __name__ == '__main__':
    main()
