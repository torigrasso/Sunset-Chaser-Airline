import unittest
from Flight import Flight


class MyTestCase(unittest.TestCase):

    def test_addBussinessSelect(self):
        flight = Flight()
        options = flight.add_business("user1", True)
        flight.confirm([options[0]], "user1")

    def test_addBussinessNormal(self):
        flight = Flight()
        options = flight.add_business("user2", False)
        flight.confirm([options[0]], "user2")

    def test_addTourist(self):
        flight = Flight()

    def test_addFamilyOne(self):
        flight = Flight()

    def test_addFamilyTwo(self):
        flight = Flight()

    def test_addFamilyThree(self):
        flight = Flight()


if __name__ == '__main__':
    unittest.main()
