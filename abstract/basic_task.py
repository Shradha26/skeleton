from abc import ABC, abstractmethod


class BasicTask(ABC):
    def __init__(self, logger=None):
        self.taskname = None
        self.logger = logger

    @abstractmethod
    def gather_input(self):
        return

    @abstractmethod
    def execute(self):
        return
