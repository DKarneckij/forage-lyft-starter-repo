from abc import ABC, abstractmethod
from battery import *
from engine import *


class Serviceable(ABC):

    @abstractmethod
    def needs_service(self):
        '''Returns true if a component of the object needs to be serviced'''

class Car(Serviceable):

    def __init__(self, Engine, Battery):
        self.engine = Engine
        self.battery = Battery

    def needs_service(self):
        return True if self.engine.needs_service() or self.battery.needs_service() else False

class CarFactory(ABC):

    def create_calliope(last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)
        

    def create_glissade(last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    def create_palindrome(last_service_date, warning_light):
        engine = SternmanEngine(warning_light)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)
    
    def create_rorschach(last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)

    def create_thovex(last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)

