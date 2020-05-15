from zadanie1 import PrintDecoratedFunctionName, ProgressBarObserver, NotifyingClass
from zadanie2 import WashCar, WheelsChemicalCleaning, BodyWorkWaterCleaning, WheelsWaterCleaning, BodyWorkChemicalCleaning
from zadanie3 import Component

@PrintDecoratedFunctionName
def zadanie_1():
    processor = NotifyingClass()
    bars = [ProgressBarObserver()]

    for bar in bars:
        processor.register_observer(bar)

    processor.start_process()
    tasks_finished = False
    while not tasks_finished:
        tasks_finished = True
        for bar in bars:
            tasks_finished == tasks_finished and bar.is_finished()


@PrintDecoratedFunctionName
def zadanie_2():
    wash = WashCar(BodyWorkWaterCleaning(), WheelsChemicalCleaning())
    wash_second = WashCar(BodyWorkChemicalCleaning(), WheelsWaterCleaning())
    print("Cleaning first car")
    wash()
    print()
    print("Cleaning second car")
    wash_second()


@PrintDecoratedFunctionName
def zadanie_3():
    pc = Component(200, "Obudowa komputera PC")
    motherboard = Component(1000, "Płyta główna")
    motherboard.add_component(Component(500, "Karta graficzna"))
    motherboard.add_component(Component(200, "Karta sieciowa"))
    motherboard.add_component(Component(400, "Karta dźwiękowa"))
    motherboard.add_component(Component(500, "Dysk"))
    pc.add_component(motherboard)
    pc.print_description()


@PrintDecoratedFunctionName
def zadanie_4():
    pass


def main():
    #zadanie_1()
    #zadanie_2()
    zadanie_3()
    zadanie_4()


if __name__ == "__main__":
    main()
