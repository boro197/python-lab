from abc import ABC, abstractmethod


class BodyWorkWashingInterface(ABC):
    @abstractmethod
    def clean_bodywork(self):
        pass


class BodyWorkWaterCleaning(BodyWorkWashingInterface):
    def clean_bodywork(self):
        print("Cleaning bodywork with water")


class BodyWorkChemicalCleaning(BodyWorkWashingInterface):
    def clean_bodywork(self):
        print("Cleaning bodywork with chemicals")
