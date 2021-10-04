import pytest

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
        # Good but exception raises in method __is_alive so you should check it in another test.
        # this test more like integration nether unit
        # no try except in test should be

    def test_is_alive_exception_unit_oriented(self, monkeypatch):
        monkeypatch.setattr(
            self.human_101,
            "_Human__status",
            "dead"
        )
        with pytest.raises(Exception) as error:
            self.human_101._Human__is_alive()
            assert error.value == f"{self.human_101._Human__name} already dead..."
