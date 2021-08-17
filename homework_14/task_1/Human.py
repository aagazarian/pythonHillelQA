from Action import Action


class Human:
    def __init__(self,
                 name: str,
                 age: int,
                 action_name: str
                 ):
        self.__name = name
        self.__age = age
        self.__action = Action(action_name)

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def action(self):
        return self.__action

    def __str__(self):
        return f"name: {self.__name}, age: {self.__age}, action: {self.action()}"


if __name__ == '__main__':
    humans = []
    actions = ["Dancing", "Jumping", "Driving", "Walking", "Seating", "Playing"]

    for i in range(1, 6):
        humans.append(Human(f"HumanName_{i}", (20+i), actions[i]))

    for human in humans:
        print(f"name: {human.name}, age: {human.age}, action: {human.action()}")
    # Nice it is the best solution for now from the group
