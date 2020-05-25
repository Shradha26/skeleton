from abc import ABC, abstractmethod


class BasicExecutor(ABC):

    @abstractmethod
    def run(self):
        return
