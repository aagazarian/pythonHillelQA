from typing import List

from homework_23.entities.user import User
from homework_23.models.user_model import UserModel
from homework_23.session import session


class UserRepository:
    def __init__(self):
        self.__session = session

    def get_all(self) -> List[User]:
        users = []
        for user in self.__session.query(UserModel).all():
            users.append(User(user.id, user.name, user.email, user.age))
        return users

    def delete_by_email(self, email: str):
        self.__session.query(UserModel).\
            filter(UserModel.email == email).\
            delete()
        self.__session.commit()

    def update_by_id(self, id, user: User):
        self.__session.query(UserModel).\
            filter(UserModel.id == id).\
            update({
                'name': user.name,
                'email': user.email,
                'age': user.age
            })
        self.__session.commit()

    def add_one(self, user: User):
        self.__session.add(UserModel(name=user.name, email=user.email, age=user.age))
        self.__session.commit()
