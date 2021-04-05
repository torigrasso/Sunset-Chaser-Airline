import sqlite3
from sqlite3 import Error
from random import randint
import json
from Customer import Customer

class Flight:

    def __init__(self):

        conn = self.create_connection("airline.db")
        c = conn.cursor()

        # get the current flight's info
        with conn:
            c.execute("SELECT * FROM FLIGHT WHERE ACTIVE=?", ("True",))

        rows = c.fetchall()

        self.number = rows[0][0]
        self.score = rows[0][1]
        self.seats = json.loads(rows[0][2])
        self.active = rows[0][3]
        self.customer_list = json.loads(rows[0][4])

        self.seat_names = ["1A", "1B", "1C", "1D", "1E", "1F", "2A", "2B", "2C", "2D", "2E", "2F", "3A", "3B", "3C",
                           "3D", "3E", "3F", "4A", "4B", "4C", "4D", "4E", "4F", "5A", "5B", "5C", "5D", "5E", "5F",
                           "6A", "6B", "6C", "6D", "6E", "6F", "7A", "7B", "7C", "7D", "7E", "7F", "8A", "8B", "8C",
                           "8D", "8E", "8F", "9A", "9B", "9C", "9D", "9E", "9F", "10A", "10B", "10C", "10D", "10E",
                           "10F", "11A", "11B", "11C", "11D", "11E", "11F", "12A", "12B", "12C", "12D", "12E", "12F",
                           "13A", "13B", "13C", "13D", "13E", "13F", "14A", "14B", "14C", "14D", "14E", "14F", "15A",
                           "15B", "15C", "15D", "15E", "15F", "16A", "16B", "16C", "16D", "16E", "16F", "17A", "17B",
                           "17C", "17D", "17C", "17E", "17F", "18A", "18B", "18C", "18D", "18E", "18F", "19A", "19B",
                           "19C", "19D", "19C", "19E", "19F", "20A", "20B", "20C", "20D", "20E", "20F"]

    # Connect to the DB
    def create_connection(self, file):
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
        customer_string = json.dumps(self.customer_list)
        # get the current flight's info
        with conn:
            c.execute("UPDATE FLIGHT SET SCORE=? WHERE NUMBER=?", (self.score, self.number))
            c.execute("UPDATE FLIGHT SET SEATS=? WHERE NUMBER=?", (seats_string, self.number))
            c.execute("UPDATE FLIGHT SET CUSTOMERS=? WHERE NUMBER=?", (customer_string, self.number))
            c.execute("UPDATE FLIGHT SET ACTIVE=? WHERE NUMBER=?", (str(self.active), self.number))

    def create_new_flight(self):
        self.seats = ['None']*120
        self.active = 'True'
        self.number += 1
        self.customer_list = ['']

        conn = self.create_connection("airline.db")
        c = conn.cursor()

        seats_string = json.dumps(self.seats)
        customer_string = json.dumps(self.customer_list)

        # Add To Database
        insert_string = "INSERT INTO FLIGHT (NUMBER, SCORE, SEATS, ACTIVE, CUSTOMERS) VALUES (?, ? , ?, ?, ?)"
        with conn:
            c.execute(insert_string, [self.number, self.score, seats_string, str(self.active), customer_string])

        # initiate again
        self.__init__()

    def get_seat_number(self, indice):
        return self.seat_names[indice]

    def get_seats(self):
        return self.seats

    def add_business(self, user, business_select):

        # give the user three options if possible
        options = []

        # traveler chooses to sit in business select
        if business_select:
            # loop through the first two rows
            for i in range(0,13):
                if self.seats[i] == 'None':
                    options.append(i)

                if len(options) == 3:
                    return options

            # if nothing was found in business select
            for i in range(13, len(self.seats)):
                if self.seats[i] == 'None':
                    options.append(i)
                if len(options) == 3:
                    return options

        else:
            # loop through the first two rows
            for i in range(13, len(self.seats)):
                if self.seats[i] == 'None':
                    options.append(i)
                if len(options) == 3:
                    return options

            # if nothing was found in normal seating
            for i in range(0,13):
                if self.seats[i] == 'None':
                    options.append(i)
                if len(options) == 3:
                    return options

        return options

    def confirm(self, seats, user):
        # assign seat
        for s in seats:
            self.seats[s] = user
        # add to customer list
        if user not in self.customer_list:
            self.customer_list.append(user)
        # update the database
        self.update_DB()

        # update customer's information
        c = Customer(user)
        c.confirm_tickets(seats)

    def add_tourist(self, user):
        pass

    def add_family(self, user, child_count):
        pass

    def end_flight(self):
        self.active = 'False'
        self.calculate_satisfactory_score()

        self.update_DB()

    def calculate_satisfactory_score(self):
        if len(self.customer_list < 10):
            groups = self.customer_list
        else:
            temp = self.customer_list
            groups = []
            # find random customers to poll
            for i in range(10):
                randomI = randint(0, len(self.customer_list-1))
                groups[i] = temp[randomI]
                # remove customer after selecting so you do not chose them again
                temp.pop(randomI)

        # calculate results by traveler type
        #for customer in groups:





        # set self.score

