import unittest
from Flight import Flight


class FlightTest(unittest.TestCase):

    def test_addBussinessSelect(self):
        flight = Flight()
        options = flight.add_business(True)
        flight.confirm([options[0]], "user1")

    def test_addBussinessNormal(self):
        flight = Flight()
        options = flight.add_business(False)
        flight.confirm([options[0]], "user2")

    def test_addTourist(self):
        flight = Flight()
        options = flight.add_tourist()
        flight.confirm(options[0], "user6")

    def test_addFamilyOne(self):
        flight = Flight()
        options = flight.add_family(1)
        flight.confirm(options[0], "user13")

    def test_addFamilyTwo(self):
        flight = Flight()
        options = flight.add_family(2)
        flight.confirm(options[0], "user14")

    def test_addFamilyThree(self):
        flight = Flight()
        options = flight.add_family(3)
        flight.confirm(options[0], "user15")


if __name__ == '__main__':
    unittest.main()

