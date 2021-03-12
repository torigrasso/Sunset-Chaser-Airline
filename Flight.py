

class Flight:

    def __init__(self, number):
        self.number = number
        self.score = None
        self.seats = []
        self.seat_names = ["1A", "1B", "1C", "1D", "1E", "1F", "2A", "2B", "2C", "2D", "2E", "2F", "3A", "3B", "3C",
                           "3D", "3E", "3F", "4A", "4B", "4C", "4D", "4E", "4F", "5A", "5B", "5C", "5D", "5E", "5F",
                           "6A", "6B", "6C", "6D", "6E", "6F", "7A", "7B", "7C", "7D", "7E", "7F", "8A", "8B", "8C",
                           "8D", "8E", "8F", "9A", "9B", "9C", "9D", "9E", "9F", "10A", "10B", "10C", "10D", "10E",
                           "10F", "11A", "11B", "11C", "11D", "11E", "11F", "12A", "12B", "12C", "12D", "12E", "12F",
                           "13A", "13B", "13C", "13D", "13E", "13F", "14A", "14B", "14C", "14D", "14E", "14F", "15A",
                           "15B", "15C", "15D", "15E", "15F", "16A", "16B", "16C", "16D", "16E", "16F", "17A", "17B",
                           "17C", "17D", "17C", "17E", "17F", "18A", "18B", "18C", "18D", "18E", "18F", "19A", "19B",
                           "19C", "19D", "19C", "19E", "19F", "20A", "20B", "20C", "20D", "20E", "20F"]
        self.active = True

    def create_new_flight(self):
        self.seats = [None]*120
        self.active = True

    def get_seat_number(self, indices):
        seats = []
        for i in indices:
            seats.append(self.seat_names[i])
        return seats

    def get_seats(self):
        return self.seats

    def add_business(self, user, business_select):
        # traveler chooses to sit in business select
        if business_select:
            # loop through the first two rows
            for i in range(0,13):
                if self.seats[i] is None:
                    self.seats[i] = user
                    return self.seats[i]
            # if nothing was found in business select
            for i in range(13, len(self.seats)):
                if self.seats[i] is None:
                    self.seats[i] = user
                    return self.seats[i]

        else:
            for i in range(13, len(self.seats)):
                if self.seats[i] is None:
                    self.seats[i] = user
                    return self.seats[i]
            # if nothing was found in normal seating
            for i in range(0,13):
                if self.seats[i] is None:
                    self.seats[i] = user
                    return self.seats[i]

    def reassign(self):
        pass

    def confirm(self, suggested):
        pass

    def add_tourist(self, user):
        pass

    def add_family(self, user, child_count):
        pass

    def end_flight(self):
        self.active = False
        self.calculate_satisfactory_score()

    def calculate_satisfactory_score(self):
        pass
