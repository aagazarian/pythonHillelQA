class Company:
    """A class used to represent the Company object

    Attributes
    ----------
    name: str
        the name of the Company. Required
    foundation_year: int
        the foundation year of Company. Required
    email: str
        email of Company
    employee_amount: int
        amount of employees in Company
    budget: float
        budget of Company
    income: float
        income of Company

    Methods
    -------
    create_new_company(cls, name: str, foundation_year: int)
        This method creates new instance of Company with required fields: name and foundation_year
    get_company_info(self)
         Return all company's information
    get_profitability(self)
         Return the profitability in percents. Income divided by budget and multiplied by 100
    """

    def __init__(
            self,
            name: str,
            foundation_year: int,
            email: str = None,
            employee_amount: int = None,
            budget: float = None,
            income: float = None
    ):
        self.__name = name
        self.__foundation_year = foundation_year
        self.__email = email
        self.__employee_amount = employee_amount
        self.__budget = budget
        self.__income = income

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name) -> None:
        self.__name = name

    @property
    def foundation_year(self) -> int:
        return self.__foundation_year

    @foundation_year.setter
    def foundation_year(self, foundation_year) -> None:
        self.__foundation_year = foundation_year

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email) -> None:
        self.__email = email

    @property
    def employee_amount(self):
        return self.__employee_amount

    @employee_amount.setter
    def employee_amount(self, employee_amount) -> None:
        self.__employee_amount = employee_amount

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, budget) -> None:
        self.__budget = budget

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, income) -> None:
        self.__income = income

    @classmethod
    def create_new_company(cls, name: str, foundation_year: int):
        """This method creates new instance of Company with required fields: name and foundation_year"""
        return cls(name, foundation_year)

    def get_profitability(self) -> float:
        """This method returns result of profitability calculation"""
        if type(self.__income) == float and\
                self.__income > 0 and\
                type(self.__budget) == float and\
                self.__budget > 0:
            profitability = self.__income / self.__budget * 100
        else:
            raise Exception("Impossible to calculate profitability")
        return profitability

    def get_company_info(self):
        """This method returns a string with all company information"""
        return (f"company name: {self.__name}\n"
                f"foundation year: {self.__foundation_year}\n"
                f"email: {self.__email}\n"
                f"employee_amount: {self.__employee_amount}\n"
                f"budget: {self.__budget}\n"
                f"income: {self.__income}\n"
                f"profitability: {self.get_profitability()}\n")


if __name__ == '__main__':
    global_logic: Company = Company.create_new_company("Global Logic", 2003)
    toshiba: Company = Company.create_new_company("Toshiba", 1987)

    global_logic.email = "info@globallogic.com"
    global_logic.employee_amount = 4500
    global_logic.budget = 4500000.00
    global_logic.income = 98000.87

    toshiba.email = "info@toshiba.com"
    toshiba.employee_amount = 12348
    toshiba.budget = 12000233.98
    toshiba.income = 8700234.32

    print("Global Logic:")
    print(global_logic.get_company_info())

    print("\nToshiba:")
    print(toshiba.get_company_info())

    # Well done but I suggest to remove setters from this class since you are
    # not sure is it needed to modificate separate field like name from global
    # scope
    # -1 point