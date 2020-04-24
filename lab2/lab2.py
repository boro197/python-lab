#!/usr/bin/python3

from functools import wraps


def zadanie_5():
    print("\nZADANIE 5")
    input_list = list(range(11))
    print("Input list:", input_list)
    print("Sequence found with map and filter:", find_primary_numbers_with_map_and_filter(input_list))
    print("Sequence found with comprehension list:", find_primary_numbers_with_list_comprehension(input_list))


def zadanie_6():
    print("\nZADANIE 6")
    number_of_elements = 5
    for number in generate_fibonacci_sequence(number_of_elements):
        line_end = ', '
        if number == number_of_elements: line_end = '\n'
        print(number, end=line_end)


def zadanie_7():
    print("\nZADANIE 7")
    print("Zadanie 7 zostało wykonane poprzez dodanie dekoratora print_function_name "
          "do kilku funkcji wykorzystywanych w innych zadaniach.")


def zadanie_8():
    print("\nZADANIE 8")
    for i in range(1, 10):
        generate_fibonacci_sequence(i)


def zadanie_9():
    print("\nZADANIE 9")
    file_path = "input_file.txt"
    print("There are", len(read_file_and_count_words(file_path)), "words in file", file_path, "!")


def print_function_name(func):
    @wraps(func)
    def printing_func(*args):
        print("Called function: ", end='')
        print(func.__name__, end='')
        print(args)
        return func(*args)

    return printing_func


def count_function_calls(func):
    @wraps(func)
    def counter(*args):
        counter.calls += 1
        last_word = "times"
        if counter.calls == 1:
            last_word = "time"
        else:
            last_word = "times"
        print('Function called', counter.calls, last_word, "!")
        return func(*args)

    counter.calls = 0
    return counter


@count_function_calls
@print_function_name
def find_primary_numbers_with_map_and_filter(input_list):
    return list(map(lambda element: element,
                    filter(lambda element: not list(filter(lambda divider: element % divider == 0, range(2, element))),
                           input_list)))


@count_function_calls
@print_function_name
def find_primary_numbers_with_list_comprehension(input_list):
    return [element for element in input_list if all(element % divider != 0 for divider in range(2, element))]


@count_function_calls
@print_function_name
def generate_fibonacci_sequence(length_of_sequence):
    a, b = 0, 1
    for i in range(0, length_of_sequence):
        yield b
        a, b = b, a + b


@count_function_calls
@print_function_name
def read_file_and_count_words(file_path):
    try:
        with open(file_path, 'r', encoding='UTF-8') as input_file:
            input_data = input_file.read()
            words = input_data.split()
            return words
    except FileNotFoundError as Ex:
        print(Ex)


def main():
    zadanie_5()
    zadanie_6()
    zadanie_7()
    zadanie_8()
    zadanie_9()


if __name__ == "__main__":
    main()
