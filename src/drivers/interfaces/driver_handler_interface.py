from abc import ABC, abstractmethod
from typing import List

class DriverHandlerInterface(ABC):

    @abstractmethod
    def standarf_derivation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)
    
    @abstractmethod
    def variance(self, numbers: List[float]) -> float:
        return self.__np.var(numbers)
    
    @abstractmethod
    def average(self, numbers: List[float]) -> float:
        pass