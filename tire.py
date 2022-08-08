from abc import ABC, abstractmethod

class Tire(ABC):

    @abstractmethod
    def needs_service():
        '''Return true if tire needs service based on relative criteria'''

class CarriganTire(Tire):

    def __init__(self, array):
        self.array = array
    
    def needs_service(self):
        for num in self.array:
            if num >= 0.9:
                return True
        return False

class CarriganTire(Tire):

    def __init__(self, array):
        self.array = array

    def needs_service(self):
        total = 0
        for num in self.array:
            total += num
        if num >= 3: return True; return False

