from .student import Student


class SchoolDiary:
    def __init__(self):
        self.__students = []
        self.__max_index = 0

    @classmethod
    def copy_existing_schoolar_diary(cls, schoolar_diary):
        new_object = cls()
        i = 1
        for student in schoolar_diary.students:
            new_object.add_student(student.name, student.surname)
            for grade in student.grades:
                new_object.add_grade_by_index(i, grade[0], grade[1])
            i = i + 1
        return new_object

    @property
    def students(self):
        return self.__students

    def add_student(self, name, surname):
        self.__max_index = self.__max_index + 1
        self.__students.append(Student(self.__max_index, name, surname))

    def print_all_students(self):
        for student in self.__students:
            print('Index number:', student.index)
            print(student.name, student.surname)
            print(student.grades)
            print("Mean: ", student.compute_mean())
            print()



    def add_grade_by_index(self, index, weight, grade):
        student = list(filter(lambda x: x.index == index, self.__students))
        if student is not None:
            student[0].add_grade(weight, grade)
        else:
            raise ValueError('There is no student with this index number')

    def get_grades_by_index(self, index):
        student = list(filter(lambda x: x.index == index, self.__students))
        if student is not None:
            return student[0].grades
        else:
            raise ValueError('There is no student with this index number')

