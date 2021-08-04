from abc import ABC, abstractmethod


class Vehicle(ABC):
    """A class used to represent the Vehicle object

        Attributes
        ----------
        model: str
            the model of vehicle. Required
        color: str
            the color of vehicle. Required
        seat_amount: int
            the number of seat of vehicle. Required

        Methods
        -------
        def drive(self)
            This method returns the string with description how the object is driving
        def stop(self)
            This method returns the string with description how the object is stopping

    """
    def __init__(
            self,
            model: str,
            color: str,
            seat_amount: int
    ):
        self._model = model,
        self._color = color,
        self._seat_amount = seat_amount

    @abstractmethod
    def drive(self):
        return f"{self._model[0]} with color: {self._color[0]} is driving"

    @abstractmethod
    def stop(self):
        return f"{self._model[0]} with amount of seat  {self._seat_amount} is stopping"


class LandVehicle(Vehicle):
    def __init__(
            self,
            model: str,
            color: str,
            seat_amount: int,
            wheels_amount: int
    ):
        super().__init__(model, color, seat_amount)
        self._wheels_amount = wheels_amount

    @abstractmethod
    def drive(self):
        return f"{Vehicle.drive(self)} on the roads"

    @abstractmethod
    def stop(self):
        return f"{Vehicle.drive(self)} on the roads"

    @abstractmethod
    def honking(self):
        return f"{type(self)} is honking"


class AirCraft(Vehicle):
    def __init__(
            self,
            model: str,
            color: str,
            seat_amount: int,
            engine_amount: int
    ):
        super().__init__(model, color, seat_amount)
        self._engine_amount = engine_amount

    @abstractmethod
    def drive(self):
        return f"{Vehicle.drive(self)} on the runway"

    @abstractmethod
    def stop(self):
        return f"{Vehicle.stop(self)} on the runway"

    @abstractmethod
    def takes_off(self):
        return f"{type(self._model)} is taking off"

    @abstractmethod
    def landing(self):
        return f"{self._model[0]} with engine amount {self._engine_amount} is landing"


class Car(LandVehicle):
    def __init__(
            self,
            model: str,
            color: str,
            seat_amount: int,
            wheels_amount: int,
            engine_type: str,
            door_amount: int,
            gearbox_type: str
    ):
        super().__init__(model, color, seat_amount, wheels_amount)
        self._engine_type = engine_type
        self._door_amount = door_amount
        self._gearbox_type = gearbox_type

    def drive(self):
        return f"{LandVehicle.drive(self)} very fast"

    def stop(self):
        return f"{LandVehicle.stop(self)} very fast"

    def honking(self):
        return f"{LandVehicle.honking(self)} pipi"


class Bicycle(LandVehicle):
    def __init__(
            self,
            model: str,
            color: str,
            seat_amount: int,
            wheels_amount: int,
            is_mountain: bool,
            brakes_type: str
    ):
        super().__init__(model, color, seat_amount, wheels_amount)
        self._is_mountain = is_mountain
        self._brakes_type = brakes_type

    def drive(self):
        return f"{LandVehicle.drive(self)} slower then car"

    def stop(self):
        return f"{LandVehicle.drive(self)} slower then car"

    def honking(self):
        return f"{LandVehicle.honking(self)} dzin-dzin"


class Plane(AirCraft):
    def __init__(
            self,
            model: str,
            color: str,
            seat_amount: int,
            engine_amount: int,
            wings_length: float
    ):
        super().__init__(model, color, seat_amount, engine_amount)
        self._wings_length = wings_length

    def drive(self):
        return f"{AirCraft.drive(self)} on runway with speed 280 km/h"

    def stop(self):
        return f"{AirCraft.stop(self)} with wings length {self._wings_length} on runway"

    def takes_off(self):
        return f"{AirCraft.takes_off(self)} horizontally"

    def landing(self):
        return f"{AirCraft.landing(self)} horizontally"


class Helicopter(AirCraft):
    def __init__(
            self,
            model: str,
            color: str,
            seat_amount: int,
            engine_amount: int,
            blade_length: float
    ):
        super().__init__(model, color, seat_amount, engine_amount)
        self._blade_length = blade_length

    def drive(self):
        return f"{AirCraft.drive(self)} on runway with speed 10 km/h"

    def stop(self):
        return f"{AirCraft.stop(self)} on runway"

    def takes_off(self):
        return f"{AirCraft.takes_off(self)} vertically"

    def landing(self):
        return f"{AirCraft.landing(self)} and with length of blade {self._blade_length} vertically"


if __name__ == '__main__':

    car1: Car = Car("bmw", "blue", 5, 4, "diesel", 4, "automatic")
    car2: Car = Car("renault", "red", 5, 4, "diesel", 4, "automatic")
    print(car1.drive())
    print(car2.drive())

    bicycle: Vehicle = Bicycle("COUB", "yellow", 1, 2, True, "hydraulic")
    print(bicycle.drive())

    plane: Plane = Plane("ModelPlane", "white", 10, 2, 100.05)
    print(plane.stop())

    helicopter: Helicopter = Helicopter("ModelHelicopter", "grey", 2, 1, 50.05)
    print(helicopter.landing())
