import sqlite3
from sqlite3 import Error
import json


class Customer:

    def __init__(self, username, password=""):

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
                    self.flight_num = r[2]
                    self.type = r[3]
                    self.seats = json.loads(r[4])
                    self.satisfaction = r[5]

        if exists is False:
            self.username = username
            self.password = password
            self.type = 'None'
            self.flight_num = 'None'
            self.seats = 'None'
            self.satisfaction = 0

            # Add to DB
            insert_string = "INSERT INTO CUSTOMER (USER, PASSWORD, SATISFACTION) VALUES (?, ?, ?)"
            with conn:
                c.execute(insert_string, [str(self.username), str(self.password), self.satisfaction])

    @staticmethod
    def create_connection(file):
        conn = None
        try:
            conn = sqlite3.connect(file)
        except Error as e:
            print(e)
        return conn

    def update_DB(self):
        conn = self.create_connection("airline.db")
        c = conn.cursor()

        seats_string = json.dumps(self.seats)

        with conn:
            c.execute("UPDATE CUSTOMER SET FLIGHT_NUMBER=? WHERE USER=?", (self.flight_num, self.username))
            c.execute("UPDATE CUSTOMER SET TRAVEL_TYPE=? WHERE USER=?", (self.type, self.username))
            c.execute("UPDATE CUSTOMER SET SEATS=? WHERE USER=?", (seats_string, self.username))
            c.execute("UPDATE CUSTOMER SET SATISFACTION=? WHERE USER=?", (self.satisfaction, self.username))

    def confirm_tickets(self, seats, num):
        self.seats = seats
        self.flight_num = num
        self.calculate_satisfaction(self.type)
        self.update_DB()

    def calculate_satisfaction(self, travelType):
        score = 0

        # Prefer Business Select section
        if travelType == "BT-BS":
            if 0 <= int(self.seats[0]) <= 11:
                score = 0
            else:
                score = -5

        # Prefer normal section
        elif travelType == "BT-N":
            if int(self.seats[0]) >= 12:
                score = 0
            else:
                score = -5

        # Travel in twos and prefer to stay together and at least one window seat
        elif travelType == "TT":

            pass

        # Travel two adults with 1-3 kids. Prefer to stay together and as many aisle seats as possible
        elif travelType == "FT":
            pass

        return score

    def get_ticket_info(self):
        return str(self.flight_num), self.type, self.seats

    def get_seats(self):
        return self.seats
