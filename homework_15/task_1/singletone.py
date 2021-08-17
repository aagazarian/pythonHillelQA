class MainCashDesk:
    __instance = None

    def __new__(cls, name, balance):
        if cls.__instance is None:
            cls.__instance = super(MainCashDesk, cls).__new__(cls)
            cls.__instance.__name = name
            cls.__instance.__balance = balance
        return cls.__instance


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
