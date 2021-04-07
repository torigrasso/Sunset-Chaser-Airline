import unittest
from Customer import Customer


class CustomerTest(unittest.TestCase):

    def test_createCustomer(self):
        Customer("newCustomer", "p@ssW0rd")
        # check DB to see if it worked

    def test_existingCustomer(self):
        user = Customer("user1")
        self.assertEqual(user.username, "user1")
        self.assertEqual(user.password, "12345")

    def test_satisfactionScoreB(self):
        user = Customer("user7")
        self.assertEqual(user.satisfaction, 0)

    def test_satisfactionScoreT(self):
        user = Customer("user1")
        self.assertEqual(user.satisfaction, 15)

    def test_satisfactionScoreF1(self):
        user = Customer("")
        self.assertEqual(user.satisfaction, 15)

    def test_satisfactionScoreF2(self):
        user = Customer("")
        self.assertEqual(user.satisfaction, 15)

    def test_satisfactionScoreF3(self):
        user = Customer("")
        self.assertEqual(user.satisfaction, 15)


if __name__ == '__main__':
    unittest.main()
