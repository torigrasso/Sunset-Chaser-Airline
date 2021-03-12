import unittest
from Flight import Flight

class MyTestCase(unittest.TestCase):
    def test_addBussiness(self):
        flight = Flight(000)
        flight.create_new_flight()
        flight.add_business("tg")
        flight.add_business("gt")


if __name__ == '__main__':
    unittest.main()
