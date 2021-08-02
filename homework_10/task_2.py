from datetime import date


class Employee:
    """A class used to represent the Employee object

        Attributes
        ----------
        first_name: str
            the first name of the Employee. Required
        last_name: str
            the last name of the Employee. Required
        birth_date: date
            date of birthday of Employee. Required
        start_date: date
            date when Employee starts work. Required
        is_fired: bool
            information about Employee:is hired or no. Required
        position: str
            Employee's position. Optional
        salary: float
            Employee's salary Optional

        Methods
        -------
        def new_employee(cls,
                     first_name: str,
                     last_name: str,
                     birth_date: date,
                     start_date: date,
                     is_fired: bool)
             This method creates new instance of Employee with required fields
        get_full_name(self)
             This method returns full Employee's name
        get_full_info(self)
             This method returns full info about Employee
        """

    def __init__(
            self,
            first_name: str,
            last_name: str,
            birth_date: date,
            start_date: date,
            is_fired: bool,
            position: str = None,
            salary: float = None
    ):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birth_date = birth_date
        self.__start_date = start_date
        self.__is_fired = is_fired
        self.__position = position
        self.__salary = salary

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name) -> None:
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name) -> None:
        self.__last_name = last_name

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, birth_date) -> None:
        self.__birth_date = birth_date

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date) -> None:
        self.__start_date = start_date

    @property
    def is_fired(self):
        return self.__is_fired

    @is_fired.setter
    def is_fired(self, is_fired) -> None:
        self.__is_fired = is_fired

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position) -> None:
        self.__position = position

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary) -> None:
        self.__salary = salary

    @classmethod
    def new_employee(cls,
                     first_name: str,
                     last_name: str,
                     birth_date: date,
                     start_date: date,
                     is_fired: bool):
        """This method creates new instance of Employee with required fields"""
        return cls(first_name,
                   last_name,
                   birth_date,
                   start_date,
                   is_fired)

    def get_full_name(self):
        """This method returns full Employee's name """
        return f"{self.__first_name} {self.__last_name}"

    def get_full_info(self):
        """This method returns full info about Employee"""
        return (f"full name: {self.get_full_name()}\n"
                f"birth date: {self.__birth_date}\n"
                f"start_date: {self.__start_date}\n"
                f"is_fired: {self.__is_fired}\n"
                f"position: {self.__position}\n"
                f"salary: {self.__salary}\n")


if __name__ == '__main__':
    employee_1: Employee = Employee.new_employee('Arpine', 'Agazarian', date(1990, 12, 27), date(2020, 1, 28), False)

    employee_1.position = "QA"
    employee_1.salary = 5000.550
    print(employee_1.get_full_info())
 # Well done but I suggest to remove setters from this class since you are
    # not sure is it needed to modificate separate field like name from global
    # scope
    # -1 point
# And I want to see some logic in this class for modification of state like in company class
#  -1 point