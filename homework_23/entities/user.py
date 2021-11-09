import json


class User:
    def __init__(
        self,
        id: int,
        name: str,
        email: str,
        age: int
    ):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__age = age

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return json.dumps(self.__dict__, sort_keys=True, indent=4)
