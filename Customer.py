import json
from Connection import create_connection


class Customer:

    def __init__(self, username, password=""):

        # If the user is already created we need to pull from the database
        conn = create_connection("airline.db")
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
                    break

        if exists is False:
            self.username = username
            self.password = password
            self.flight_num = ''
            self.type = ''
            self.seats = []
            seats_string = json.dumps(self.seats)
            self.satisfaction = 0

            # Add to DB
            insert_string = "INSERT INTO CUSTOMER (USER, PASSWORD, FLIGHT_NUMBER, TRAVEL_TYPE, SEATS, SATISFACTION) VALUES (?, ?, ?, ?, ?, ?)"
            with conn:
                c.execute(insert_string, [str(self.username), str(self.password), self.flight_num, str(self.type), seats_string, self.satisfaction])

    def update_DB(self):
        conn = create_connection("airline.db")
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
        self.satisfaction = self.calculate_satisfaction()
        self.update_DB()

    def calculate_satisfaction(self):
        score = 0

        # Prefer Business Select section
        if self.type == "BT-BS":
            if 0 <= int(self.seats[0]) <= 11:
                score = 0
            else:
                score = -5

        # Prefer normal section
        elif self.type == "BT-N":
            if int(self.seats[0]) >= 12:
                score = 0
            else:
                score = -5

        # Travel in twos and prefer to stay together and at least one window seat
        elif self.type == "TT":
            seat1 = int(self.seats[0])
            seat2 = int(self.seats[1])

            # grouped together
            if abs(seat1 - seat2) == 1:
                score += 10
            else:
                score -= 10

            # window seat preference
            if (seat1 % 6 == 0 or seat2 % 6 == 0) or ((seat1+1) % 6 == 0 or (seat2+1) % 6 == 0):
                score += 5

        # Travel two adults with 1-3 kids. Prefer to stay together and as many aisle seats as possible
        elif self.type == "FT-1" or self.type == "FT-2" or self.type == "FT-3":

            # Aisle seat preference
            for seat in self.seats:
                # check if aisle seat
                if (int(seat) % 3 == 0) or (int(seat)+1 % 3):
                    # check that it is not window seat
                    if (int(seat) % 6 != 0) and ((int(seat)+1) % 6 != 0):
                        score += 5
                        break

            # Grouping seat preference
            broken_up = True

            if self.type == "FT-1":
                adult1 = int(self.seats[0])
                adult2 = int(self.seats[1])
                child1 = int(self.seats[2])

                if abs(adult1 - adult2) == 1:
                    if abs(adult2 - child1) == 1:
                        broken_up = False

            elif self.type == "FT-2":
                adult1 = int(self.seats[0])
                adult2 = int(self.seats[1])
                child1 = int(self.seats[2])
                child2 = int(self.seats[3])

                if abs(adult1 - adult2) == 1:
                    if abs(adult2 - child1) == 1:
                        if abs(child1 - child2) == 1:
                            broken_up = False

            elif self.type == "FT-3":
                adult1 = int(self.seats[0])
                adult2 = int(self.seats[1])
                child1 = int(self.seats[2])
                child2 = int(self.seats[3])
                child3 = int(self.seats[4])

                if abs(adult1 - adult2) == 1:
                    if abs(adult2 - child1) == 1:
                        if abs(child1 - child2) == 1:
                            if abs(child2 - child3) == 1:
                                broken_up = False

            if broken_up is True:
                score -= 10
            else:
                score += 10

        return score

    def get_ticket_info(self):
        return str(self.flight_num), self.type, self.seats
