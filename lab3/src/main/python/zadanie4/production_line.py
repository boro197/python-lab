class ProductionLine:
    def __init__(self, first_step, first_step_arg):
        self.__first_step = first_step
        self.__first_step_arg = first_step_arg
        self.__steps = []

    def add_step(self, step):
        self.__steps.append(step)

    def execute(self):
        print('Executing: {0}'.format(self.__first_step.__class__.__name__))
        result_of_previous_step = self.__first_step(self.__first_step_arg)
        for step in self.__steps:
            print('Executing: {0}'.format(step.__class__.__name__))
            result_of_previous_step = step(result_of_previous_step)
