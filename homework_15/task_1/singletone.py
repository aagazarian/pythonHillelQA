class MainCashDesk:
    __instance = None

    def __new__(cls, name, balance):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__name = name
            cls.__instance.__balance = balance
        return cls.__instance

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance


if __name__ == '__main__':
    desk1 = MainCashDesk("Main cash desk", 800)
    desk2 = MainCashDesk("Desk2", 990)
    desk3 = MainCashDesk("Desk3", 1002)

    print(desk1)
    print(desk2)
    print(desk3)

    print(id(desk1))
    print(id(desk2))
    print(id(desk3))


# Nice but it is not a singleton -5 poitns
# take a look on constructor which I added
# every time after __new__ python will follow to __init__ and reassign
# attributes for all references
# instance still same but it is has side effects which should be in singleton
