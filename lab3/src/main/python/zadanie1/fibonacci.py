class FibonacciGenerator:

    def __init__(self, number_of_elements):
        self.__current_iteration = 0
        self.__number_of_elements = number_of_elements
        self.__previous_element = 0
        self.__current_element = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_iteration >= self.__number_of_elements:
            raise StopIteration

        return_value = -1

        if self.__current_iteration <= 1:
            return_value = self.__current_iteration
        else:
            temp = self.__current_element
            self.__current_element = self.__current_element + self.__previous_element
            self.__previous_element = temp
            return_value = self.__current_element

        self.__current_iteration = self.__current_iteration + 1

        return return_value
