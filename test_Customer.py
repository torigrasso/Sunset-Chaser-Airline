import unittest
from Customer import Customer
from Connection import create_connection


class CustomerTest(unittest.TestCase):

    def test_createCustomer(self):
        Customer("newCustomer", "p@sSw0rD")
        # check DB now to see that the manager was created
        conn = create_connection("airline.db")
        c = conn.cursor()

        # Check if User/Pass match DB
        with conn:
            c.execute("SELECT * FROM CUSTOMER WHERE USER=?", ("newCustomer",))
            rows = c.fetchall()

            username = rows[0][0]
            password = rows[0][1]

        self.assertEqual(username, "newCustomer")
        self.assertEqual(password, "p@sSw0rD")

    def test_existingCustomer(self):
        user = Customer("user1")
        self.assertEqual(user.username, "user1")
        self.assertEqual(user.password, "12345")

    def test_satisfactionScoreB(self):
        user = Customer("user1")
        self.assertEqual(user.satisfaction, 0)

    def test_satisfactionScoreT(self):
        user = Customer("user3")
        self.assertEqual(user.satisfaction, 15)

    def test_satisfactionScoreF1(self):
        user = Customer("user4")
        self.assertEqual(user.satisfaction, 15)

    def test_satisfactionScoreF2(self):
        user = Customer("user5")
        self.assertEqual(user.satisfaction, 15)

    def test_satisfactionScoreF3(self):
        user = Customer("user6")
        self.assertEqual(user.satisfaction, 15)


if __name__ == '__main__':
    unittest.main()


