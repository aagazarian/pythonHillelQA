from typing import List

from ..task_1.passenger import Passenger


class TrainCar:
    def __init__(self, seat_amount: int):
        self.__seat_amount = seat_amount
        self.__number = None
        self.__passengers: List[Passenger] = list()

    def add_passenger(self, passenger: Passenger):
        if len(self.__passengers) < self.__seat_amount:
            self.__passengers.append(passenger)
        else:
            print(
                f"TrainCar is almost full. Following Passenger wasn't added:\n{passenger}"
            )
        return self

    def __str__(self):
        result = "["
        index = 0
        for passenger in self.__passengers:
            if index != 0:
                result += f"{str(passenger)}".replace("Passenger: ", ",")
            else:
                result += f"{str(passenger)}".replace("Passenger: ", "")
            index += 1
        return f"{result}]"

    @property
    def passengers(self):
        return self.__passengers

    @property
    def self_number(self):
        return self.__number

    @self_number.setter
    def self_number(self, value):
        self.__number = value

    def len(self):
        return len(self.__passengers)
