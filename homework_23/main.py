from homework_23.entities.user import User
from homework_23.repositories.user_repository import UserRepository

if __name__ == '__main__':
    user_repository = UserRepository()
    user2add_1 = User(0, "Dan", "dan@gmail.com", age=32)
    user2add_2 = User(0, "Dan1", "dan1@gmail.com", age=32)
    user2update = User(18, "MR John", "john_mr@gmail.com", 24)

    # user_repository.add_one(user2add_1)
    # user_repository.add_one(user2add_2)
    #
    # users = user_repository.get_all()
    # for user in users:
    #     print(user)
    #
    user_repository.delete_by_email("dan@gmail.com")
    #
    # users = user_repository.get_all()
    # for user in users:
    #     print(user)

    user_repository.update_by_id(user2update.id, user2update)

    users = user_repository.get_all()
    for user in users:
        print(user)
