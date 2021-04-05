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

    


if __name__ == '__main__':
    unittest.main()
