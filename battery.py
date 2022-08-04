from abc import ABC, abstractmethod
from dateutil.relativedelta import relativedelta

class Battery(ABC):
    
    @abstractmethod
    def needs_service():
        '''Returns true if battery needs to change based on battery criteria'''

class SpindlerBattery(Battery):

    time_between_service = 2
    
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return self.time_between_service <= relativedelta(
            self.current_date, self.last_service_date).years

class NubbinBattery(Battery):

    time_between_service = 4
    
    def __init__(self, last_service_date, current_date):
        self.last_service_date = self
        self.current_date = current_date

    def needs_service(self):
        return self.time_between_service <= relativedelta(
            self.current_date, self.last_service_date).years
