from abstract.basic_executor import BasicExecutor
from abc import abstractmethod


class SerialExecutor(BasicExecutor):
    def __init__(self):
        self.order = None
        self.taskmap = None

    @abstractmethod
    def run(self):
        pass
