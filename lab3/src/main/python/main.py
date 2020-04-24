#!/usr/bin/python3
from random import uniform, randint
from argparse import ArgumentParser

from zadanie1 import CountNumberOfExecutions, PrintDecoratedFunctionName, FibonacciGenerator
from zadanie2 import MinMaxStack
from zadanie3 import SchoolDiary
from zadanie4 import ImageModifier


@CountNumberOfExecutions
def print_fibonacci_sequence(number_of_fibonacci_elements):
    i = 1
    for element in FibonacciGenerator(number_of_fibonacci_elements):
        if i < number_of_fibonacci_elements:
            end_of_line = ', '
        else:
            end_of_line = '\n'
        print(element, end=end_of_line)
        i = i + 1


@PrintDecoratedFunctionName
def zadanie_1(number_of_calls):
    for i in range(1, number_of_calls + 1):
        print_fibonacci_sequence(i)


@PrintDecoratedFunctionName
def zadanie_2(elements_to_insert):
    stack = MinMaxStack()
    for element in elements_to_insert:
        stack.push(element)
    print('Min element on stack is {0}'.format(stack.min_element()))
    print('Max element on stack is {0}'.format(stack.max_element()))


@PrintDecoratedFunctionName
def zadanie_3():
    dziennik = SchoolDiary()
    dziennik.add_student("Jan", "Kowalski")
    dziennik.add_student("Paweł", "Kozakiewicz")
    dziennik.add_student("Jolanta", "Mucha")
    dziennik.add_student("Anna", "Romaniak")
    dziennik.add_student("Piotr", "Zboralski")

    for student in dziennik.students:
        for i in range(0, 5):
            student.add_grade(uniform(0.1, 5.0), randint(1, 6))

    dziennik.add_grade_by_index(1, 2.6, 5)
    dziennik.add_grade_by_index(4, 3.8, 2)

    print(dziennik.get_grades_by_index(1))
    print(dziennik.get_grades_by_index(4))
    print()

    dziennik_2 = SchoolDiary.copy_existing_schoolar_diary(dziennik)
    dziennik_2.print_all_students()


@PrintDecoratedFunctionName
def zadanie_4(input_image_path, output_image_path):
    image_modifier = ImageModifier(input_image_path, output_image_path)
    image_modifier.execute()


def prepare_parser():
    parser = ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input-path', type=str, help='Path to input image', required=True)
    parser.add_argument('-o', '--output-path', type=str, help='Path to output image', required=True)
    return parser.parse_args()


def main():
    args = prepare_parser()
    zadanie_1(15)
    zadanie_2([1, 45, 54, 123, 6423, 43, 5])
    zadanie_3()
    zadanie_4(args.input_path, args.output_path)


if __name__ == "__main__":
    main()
