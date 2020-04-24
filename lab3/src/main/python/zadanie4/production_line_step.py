from abc import ABC, abstractmethod


class ProductionLineStep(ABC):
    @abstractmethod
    def __call__(self, previous_step_result):
        pass
