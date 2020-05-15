from zadanie1 import PrintDecoratedFunctionName, ProgressBarObserver, NotifyingClass


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
    pass


@PrintDecoratedFunctionName
def zadanie_3():
    pass


@PrintDecoratedFunctionName
def zadanie_4():
    pass


def main():
    zadanie_1()
    zadanie_2()
    zadanie_3()
    zadanie_4()


if __name__ == "__main__":
    main()
