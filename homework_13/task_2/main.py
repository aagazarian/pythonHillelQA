from homework_13.task_1.passenger import Passenger
from homework_13.task_2.train import Train
from homework_13.task_2.train_car import TrainCar

if __name__ == '__main__':
    train = Train()

    train\
        .add_train_car(TrainCar(10)
                       .add_passenger(Passenger("John", 2, "Kyiv", "Odessa"))
                       .add_passenger(Passenger("Oles", 3, "Kyiv", "Dnipro"))
                       .add_passenger(Passenger("Yevgen", 5, "Kyiv", "Odessa"))
                       .add_passenger(Passenger("Max", 9, "Kyiv", "Vinnytsa"))
                       .add_passenger(Passenger("Sergey", 8, "Kyiv", "Vinnytsa"))
                       )\
        .add_train_car(TrainCar(3)
                       .add_passenger(Passenger("Marta", 1, "Kyiv", "Odessa"))
                       .add_passenger(Passenger("Ivan", 2, "Kyiv", "Bila Tserkva"))
                       .add_passenger(Passenger("Fedor", 3, "Kyiv", "Odessa"))
                       .add_passenger(Passenger("Petr", 4, "Kyiv", "Odessa"))
                       ) \
        .add_train_car(TrainCar(8)
                       .add_passenger(Passenger("Alyona", 5, "Kyiv", "Bila Tserkva"))
                       .add_passenger(Passenger("Volodymyr", 8, "Kyiv", "Odessa"))
                       .add_passenger(Passenger("Alex", 2, "Kyiv", "Bila Tserkva"))
                       .add_passenger(Passenger("Petr", 6, "Kyiv", "Vinnytsa"))
                       )

    print(f"\nTrain: {train}")
    print(f"Train length: {train.len()}\n")
    for train_car in train.train_cars:
        print(f"TrainCar length (passenger amount) in train_car Number: '{train_car.self_number}' is '{train_car.len()}'")

    # print all passengers:
    for train_car in train.train_cars:
        print(f"\nPassengers in train_car Number: {train_car.self_number}:")
        print(train_car)

    # print one passenger
    print(f"\nOne passenger in 1st TrainCar:\n{train.train_cars[0].passengers[0]}")
