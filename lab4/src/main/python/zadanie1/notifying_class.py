from time import sleep


class NotifyingClass:

    def __init__(self):
        self.__observers = []

    def start_process(self):
        for i in range(0, 101):
            self.notify_progress(i)
            sleep(0.1)
        self.notify_finished()

    def register_observer(self, observer):
        self.__observers.append(observer)

    def notify_progress(self, progress):
        """
        Notify all observers about an event.
        """
        for obs in self.__observers:
            obs.update_progress(progress)

    def notify_finished(self):
        for obs in self.__observers:
            obs.on_finished()
