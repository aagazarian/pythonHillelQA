from .human import Human


class TestHuman:
    def setup_class(self):
        self.human_correct = Human("John", 33, "male")
        self.human_100 = Human("Anna", 100, "female")
        self.human_101 = Human("Bob", 101, "male")

    def test_age(self):
        assert self.human_correct.age == 33

    def test_gender(self):
        assert self.human_correct.gender == "male"

    def test_change_gender(self):
        self.human_correct.change_gender("female")
        assert self.human_correct.gender == "female"

    def test_change_gender_exception(self):
        try:
            self.human_101.change_gender("male")
        except Exception as e:
            assert e.__str__() == "Bob already has gender 'male'"

    def test_change_gender_invalid(self):
        human = Human("Alex", 12, "man")
        try:
            human.change_gender("woman")
        except Exception as e:
            assert e.__str__() == "Not correct name of gender"
        assert human.gender == "man"

    def test_grow(self):
        self.human_correct.grow()
        assert self.human_correct.age == 34

    def test_grow_dead(self):
        self.human_100.grow()
        assert self.human_100.age == 100

    def test_is_alive_exception(self):
        self.human_101.grow()
        try:
            self.human_101.grow()
        except Exception as ex:
            assert ex.__str__() == "Bob is already dead..."
        assert self.human_101.age == 101
