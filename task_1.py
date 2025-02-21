import logging
from abc import ABC, abstractmethod

logger = logging.getLogger("transport_info")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

fh = logging.FileHandler("transport.log")
fh.setLevel(logging.ERROR)
fh.setFormatter(formatter)
logger.addHandler(fh)

class Vehicle(ABC):
    def __init__(self, make, model, region):
        self.make = make
        self.model = model
        self.region = region

    def start_engine(self):
        logger.info(f"{self.make} {self.model} ({self.region} Spec): Мотор заведено")

    def get_region(self):
        return f"Region of {self.make} {self.model} is {self.region}"

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

class USVehicleFactory(VehicleFactory):
    REGION = "USA"

    def create_car(self, make, model):
        return Car(make, model, self.REGION)

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, self.REGION)

class EUVehicleFactory(VehicleFactory):
    REGION = "EURO"

    def create_car(self, make, model):
        return Car(make, model, self.REGION)

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, self.REGION)

usa_factory = USVehicleFactory()
europe_factory = EUVehicleFactory()

vehicle1 = usa_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()
print(vehicle1.get_region())

vehicle2 = europe_factory.create_motorcycle("BMW", "R 1250 GS")
vehicle2.start_engine()
print(vehicle2.get_region())
