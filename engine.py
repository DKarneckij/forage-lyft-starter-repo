from abc import ABC, abstractmethod

class Engine(ABC): 
    
    @abstractmethod
    def needs_service():
        '''Returns true if engine needs to be changed based on engines criteria'''

class CapuletEngine(Engine):

    miles_between_change = 30000

    def __init__(self, last_service_mileage, current_milage):
        self.last_service_milage = last_service_mileage
        self.current_milage = current_milage

    def needs_service(self):
        return (self.current_milage - self.last_service_milage) >= self.miles_between_change

class WilloughbyEngine(Engine):

    miles_between_change = 60000

    def __init__(self, last_service_mileage, current_milage):
        self.last_service_milage = last_service_mileage
        self.current_milage = current_milage

    def needs_service(self):
        return (self.current_milage - self.last_service_milage) >= self.miles_between_change


class SternmanEngine(Engine):

    def __init__(self, warning_light):
        self.warning_light = warning_light

    def needs_service(self):
        return self.warning_light

