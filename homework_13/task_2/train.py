from .train_car import TrainCar


class Train:
    def __init__(self):
        self.__train_cars: list[TrainCar] = list()
        self.__train_head = TrainHead()

    def add_train_car(self, train_car: TrainCar):
        train_car.self_number = self.len() + 1
        self.__train_cars.append(train_car)
        return self

    @property
    def train_cars(self):
        return self.__train_cars

    def len(self):
        return len(self.__train_cars)

    def __str__(self):
        result = f"<=[{self.__train_head}]"

        for train_car in self.__train_cars:
            result += f"-[{train_car.self_number}]"

        return result


class TrainHead:
    __instance = None
    __name = "HEAD"

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(TrainHead, cls).__new__(cls)
        return cls.__instance

    def __str__(self):
        return self.__name
