from abc import ABC, abstractmethod
class BaseMenu(ABC):
    @abstractmethod
    def CreateMenu(self, instanse):
        pass

    @abstractmethod
    def DestroyMenu(self, instanse):
        pass