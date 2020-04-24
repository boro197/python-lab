class CountNumberOfExecutions:
    def __init__(self, func):
        self.__func = func
        self.__calls = 0

    def __call__(self, *args, **kwargs):
        self.__calls += 1
        last_word = "times"
        if self.__calls == 1:
            last_word = "time"
        else:
            last_word = "times"
        print('Function called', self.__calls, last_word, "!")
        return self.__func(*args, **kwargs)


class PrintDecoratedFunctionName:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        decorator = '*' * 5
        print('\n{0}{1}{0}\n'.format(decorator, self.__func.__name__))
        return self.__func(*args, **kwargs)
