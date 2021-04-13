import unittest
from Manager import Manager
from Connection import create_connection


class ManagerTest(unittest.TestCase):

    def test_createManager(self):

        Manager("newManager", "p@sSw0rD", "321")

        # check DB now to see that the manager was created
        conn = create_connection("airline.db")
        c = conn.cursor()

        # Check if User/Pass match DB
        with conn:
            c.execute("SELECT * FROM MANAGER WHERE USER=?", ("newManager",))
            rows = c.fetchall()

            username = rows[0][0]
            password = rows[0][1]
            code = rows[0][2]

        self.assertEqual(username, "newManager")
        self.assertEqual(password, "p@sSw0rD")
        self.assertEqual(code, 321)


if __name__ == '__main__':
    unittest.main()


