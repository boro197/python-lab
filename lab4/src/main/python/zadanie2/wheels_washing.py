from abc import ABC, abstractmethod


class WheelsWashingInterface(ABC):
    @abstractmethod
    def clean_wheels(self):
        pass


class WheelsWaterCleaning(WheelsWashingInterface):
    def clean_wheels(self):
        print("Cleaning wheels with water")


class WheelsChemicalCleaning(WheelsWashingInterface):
    def clean_wheels(self):
        print("Cleaning wheels with chemicals")
