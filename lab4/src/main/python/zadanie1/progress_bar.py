from time import sleep
from progressbar import ProgressBar


class ProgressBarObserver:

    def __init__(self):
        self.__progress_bar = ProgressBar(max_value=100)
        self.__is_finished = False

    def update_progress(self, progress):
        self.__progress_bar.update(progress)


    def is_finished(self):
        return self.__is_finished

    def on_finished(self):
        print("Task finished !")
        self.__is_finished = True
