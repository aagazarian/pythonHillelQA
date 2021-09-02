class Passenger:
    def __init__(
            self,
            name: str,
            seat_number: int,
            departure: str,
            destination: str
    ):
        self.__name = name
        self.__seat_number = seat_number
        self.__departure = departure
        self.__destination = destination

    def __pretty_key(self, key: str) -> str:
        return key.replace(f"_{self.__class__.__name__}__", "")

    @property
    def seat_number(self):
        return self.__seat_number

    @staticmethod
    def __pretty_value(value) -> str:
        if type(value) == str:
            return f'"{value}"'
        else:
            return value

    def __str__(self):
        result = f"{self.__class__.__name__}: ""{""\n"
        count = 0
        for key, value in self.__dict__.items():
            if count == (len(self.__dict__.items()) - 1):
                result += f'\t"{self.__pretty_key(key)}": {self.__pretty_value(value)}\n'
            else:
                result += f'\t"{self.__pretty_key(key)}": {self.__pretty_value(value)},\n'
            count += 1

        return f"{result} ""}"""


if __name__ == '__main__':
    passenger1 = Passenger("John", 11, "Kyiv", "Munich")
    print(passenger1)
