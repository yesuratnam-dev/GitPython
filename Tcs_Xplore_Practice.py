class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def percentage(self):
        self.perce = int(sum(marks) / len(marks))
        return self.perce

    def find_grade(self):
        try:
            if self.perce > 80:
                return "A"
            elif 60 <= self.perce < 80:
                return "B"
            elif 40 <= self.perce < 60:
                return "C"
            else:
                return "Fail"
        except ValueError:
            print("something went wrong: try again")


if __name__ == '__main__':
    name = str(input("enter student name: "))
    roll = int(input("enter student roll number: "))
    no_subjects = int(input('how many subjects student registered for: '))
    marks = []
    for i in range(no_subjects):
        marks_in_sub = int(input("enter how many marks student obtained in subject {}: ".format(i + 1)))
        marks.append(marks_in_sub)

    s = Student(name, roll, marks)
    print(s.percentage())
    print(s.find_grade())