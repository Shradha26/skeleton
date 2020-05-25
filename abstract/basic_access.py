from abc import ABC, abstractmethod


class BasicAccess(ABC):
    def __init__(self):
        self.collection = None

    @abstractmethod
    def create(self, obj):
        return

    @abstractmethod
    def read(self):
        return

    @abstractmethod
    def update(self, obj):
        return

    @abstractmethod
    def delete(self, obj):
        return
