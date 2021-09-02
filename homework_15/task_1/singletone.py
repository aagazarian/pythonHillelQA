class SingleInstanceMetaClass(type):
    def __init__(cls, name, balance, dic):
        cls.__single_instance = None
        super().__init__(name, balance, dic)

    def __call__(cls, *args, **kwargs):
        if cls.__single_instance is None:
            single_obj = cls.__new__(cls)
            single_obj.__init__(*args, **kwargs)
            cls.__single_instance = single_obj
        return cls.__single_instance


class MainCashDesk(metaclass=SingleInstanceMetaClass):
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
