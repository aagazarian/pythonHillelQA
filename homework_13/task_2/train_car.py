from homework_13.task_1.passenger import Passenger


class TrainCar:
    def __init__(
            self,
            seat_amount: int
    ):
        self.__seat_amount = seat_amount
        self.__self_number = None
        self.__passengers: list[Passenger] = list()

    def add_passenger(self, passenger: Passenger):
        if len(self.__passengers) < self.__seat_amount:
            self.__passengers.append(passenger)
        else:
            print(f"TrainCar is almost full. Following Passenger wasn't added:\n{passenger}")
        return self

    def __str__(self):
        result = "["
        index = 0
        for passenger in self.__passengers:
            if index != 0:
                result += f"{passenger.__str__()}".replace("Passenger: ", ",")
            else:
                result += f"{passenger.__str__()}".replace("Passenger: ", "")
            index += 1
        return f"{result}]"

    @property
    def passengers(self):
        return self.__passengers

    @property
    def self_number(self):
        return self.__self_number

    @self_number.setter
    def self_number(self, value):
        self.__self_number = value

    def len(self):
        return len(self.__passengers)
