from .stack import Stack


class MinMaxStack(Stack):
    def __init__(self):
        super().__init__()

    def __get_super_stack(self):
        stack = []
        while not self.is_empty():
            stack.append(self.top())
            self.pop()

        for element in stack:
            self.push(element)

        return stack

    def min_element(self):
        return min(self.__get_super_stack())

    def max_element(self):
        return max(self.__get_super_stack())
