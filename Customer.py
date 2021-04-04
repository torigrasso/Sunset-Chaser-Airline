import sqlite3
from sqlite3 import Error


class Customer:

    def __init__(self, username, password):

        # If the user is already created we need to pull from the database
        conn = self.create_connection("airline.db")
        c = conn.cursor()
        exists = False
        with conn:
            c.execute("SELECT * FROM CUSTOMER")
            rows = c.fetchall()
            for r in rows:
                if r[0] == username:
                    exists = True
                    self.username = r[0]
                    self.password = r[1]
                    self.current_type = r[2]
                    self.current_flight = r[3]
                    self.current_seats = r[4]
                    self.current_satisfaction = r[5]

        if exists is False:
            self.username = username
            self.password = password
            self.current_type = None
            self.current_flight = None
            self.current_seats = None
            self.current_satisfaction = 0

            # Add to DB
            insert_string = "INSERT INTO CUSTOMER (USER, PASSWORD, SATISFACTION) VALUES (?, ?, ?)"
            with conn:
                c.execute(insert_string, [str(self.username), str(self.password), self.current_satisfaction])

    # Connect to the DB
    def create_connection(self, file):
        conn = None
        try:
            conn = sqlite3.connect(file)
        except Error as e:
            print(e)
        return conn

    def get_tickets(self):
        pass

    def get_seats(self):
        pass

