class Student:
    def __init__(self, index, name, surname):
        self.__index = index
        self.__name = name
        self.__surname = surname
        self.__grades = []

    @property
    def index(self):
        return self.__index

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def grades(self):
        return self.__grades

    def add_grade(self, weight, grade):
        if grade not in range(1, 7):
            raise ValueError("Grade mus be integer between 1 and 6")
        elif weight < 0 or weight > 5:
            raise ValueError("Grade must be positive lower or equal 5")
        else:
            self.__grades.append([round(weight, 2), grade])

    def compute_mean(self):
        if self.__grades.__len__() == 0:
            return 0

        grades_sum = 0
        weight_sum = 0
        for grade in self.__grades:
            grades_sum = grades_sum + grade[0] * grade[1]
            weight_sum = weight_sum + grade[0]

        return grades_sum / weight_sum
