class WashCar:
    def __init__(self, bodywork_cleaning_strategy, wheels_cleaning_strategy):
        self.__bodywork_cleaning_strategy = bodywork_cleaning_strategy
        self.__wheels_cleaning_strategy = wheels_cleaning_strategy

    def __call__(self, *args, **kwargs):
        self.__bodywork_cleaning_strategy.clean_bodywork()
        self.__wheels_cleaning_strategy.clean_wheels()
