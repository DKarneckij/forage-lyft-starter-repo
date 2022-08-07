from abc import ABC, abstractmethod
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Battery(ABC):
    
    @abstractmethod
    def needs_service():
        '''Returns true if battery needs to change based on battery criteria'''

class SpindlerBattery(Battery):

    time_between_service = 2
    
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.time_between_service < relativedelta(
            datetime.today().date(), self.last_service_date).years

class NubbinBattery(Battery):

    time_between_service = 4
    
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.time_between_service < relativedelta(
            datetime.today().date(), self.last_service_date).years
