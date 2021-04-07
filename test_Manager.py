import unittest
from Manager import Manager


class ManagerTest(unittest.TestCase):

    def createManager(self):
        Manager("newManager", "p@sSw0rD", "321")
        # check DB now to see that the managere was created


if __name__ == '__main__':
    unittest.main()
