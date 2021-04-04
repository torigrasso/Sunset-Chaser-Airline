import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import sqlite3
from sqlite3 import Error

from Customer import Customer
from Manager import Manager
from Flight import Flight


# controller.USER after a refresh will give the user


# Connect to DB
def create_connection(file):
    conn = None
    try:
        conn = sqlite3.connect(file)
    except Error as e:
        print(e)
    return conn


# ------- Customer Pages -------
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        conn = create_connection("airline.db")
        cursor = conn.cursor()

        # ----Logo and Title----
        load = Image.open("logo.png")
        load = load.resize((150, 85), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=0, column=0, columnspan=2)
        title = ttk.Label(self, text="Sunset Chaser Airlines")
        title.grid(row=1, column=0, pady=10, columnspan=2)

        # ---- Login ----
        def logIn():
            user = username1_entry.get()
            pw = pw_entry.get()
            # Check if User/Pass match DB
            with conn:
                cursor.execute("SELECT * FROM CUSTOMER")
                row = cursor.fetchall()
                for r in row:
                    if r[0] == user:
                        if str(r[1]) == pw:
                            # Navigate To Customer Portal
                            controller.refresh_user(user)
                            controller.show_frame(CustomerPortal)
                            return

            # Throw Error If They Do Not Match
            error1['text'] = "Either the Username or PW is not correct"

        login = ttk.Label(self, text="Customer Login")
        login.grid(row=2, column=0, pady=10, columnspan=2)
        username1_label = ttk.Label(self, text="Username:")
        username1_label.grid(row=3, column=0, padx=10, pady=4)
        username1_entry = ttk.Entry(self, width=20)
        username1_entry.grid(row=3, column=1, padx=10, pady=4)
        pw_label = ttk.Label(self, text="Password:")
        pw_label.grid(row=4, column=0, padx=10, pady=4)
        pw_entry = ttk.Entry(self, width=20, show="*")
        pw_entry.grid(row=4, column=1, padx=10, pady=4)
        submit1 = ttk.Button(self, text="Submit", command=lambda: logIn())
        submit1.grid(row=5, column=0, columnspan=2, pady=5)
        error1 = ttk.Label(self, text="", foreground="#ff0000")
        error1.grid(row=6, column=0, columnspan=2, pady=5)

        # ---- Sign Up ----
        def signUp():
            # Make sure entries are not empty
            user = username2_entry.get()
            pw1 = pw1_entry.get()
            pw2 = pw2_entry.get()
            if user != "" and pw1 != "":

                # Check if username is taken or not
                with conn:
                    cursor.execute("SELECT * FROM CUSTOMER")
                    row = cursor.fetchall()
                    for r in row:
                        if r[0] == user:
                            error2['text'] = "Username already taken"
                            return

                # Check That PW Match
                if pw1 != pw2:
                    error2['text'] = "Passwords do not match"
                    return

                # Add New Manager to DB
                Customer(user, pw1)

                # Navigate To Manager Portal
                controller.refresh_user(user)
                controller.show_frame(CustomerPortal)

        sign_up = ttk.Label(self, text="Need an account? Sign up here")
        sign_up.grid(row=7, column=0, pady=10, columnspan=2)
        username2_label = ttk.Label(self, text="Username:")
        username2_label.grid(row=8, column=0, padx=10, pady=4)
        username2_entry = ttk.Entry(self, width=20)
        username2_entry.grid(row=8, column=1, padx=10, pady=4)
        pw1_label = ttk.Label(self, text="Password:")
        pw1_label.grid(row=9, column=0, padx=10, pady=4)
        pw1_entry = ttk.Entry(self, width=20, show="*")
        pw1_entry.grid(row=9, column=1, padx=10, pady=4)
        pw2_label = ttk.Label(self, text="Re-Enter Password:")
        pw2_label.grid(row=10, column=0, padx=10, pady=4)
        pw2_entry = ttk.Entry(self, width=20, show="*")
        pw2_entry.grid(row=10, column=1, padx=10, pady=4)
        submit2 = ttk.Button(self, text="Submit", command=lambda: signUp())
        submit2.grid(row=11, column=0, columnspan=2, pady=5)
        error2 = ttk.Label(self, text="", foreground="#ff0000")
        error2.grid(row=12, column=0, columnspan=2, pady=5)

        # ---- Button To Manager Portal ----
        manager_button = ttk.Button(self, text="Manager Portal", command=lambda: controller.show_frame(ManagerSignIn))
        manager_button.grid(row=13, column=0, pady=20, columnspan=2)


class CustomerPortal(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ----Home/Current Flight/Sign Out----
        home_button = ttk.Button(self, text="Home", command=lambda: controller.show_frame(CustomerPortal))
        home_button.grid(row=0, column=0, pady=10)
        flight_label = ttk.Label(self, text="Flight NUM")
        flight_label.grid(row=0, column=1, pady=10)
        sign_out_button = ttk.Button(self, text="Sign Out", command=lambda: controller.show_frame(HomePage))
        sign_out_button.grid(row=0, column=2, pady=10)

        # ----Logo and Titles----
        load = Image.open("logo.png")
        load = load.resize((150, 85), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=1, column=0, padx=100, columnspan=3)
        title1 = ttk.Label(self, text="Sunset Chaser Airlines")
        title1.grid(row=2, column=0, padx=20, pady=2, columnspan=3)
        title2 = ttk.Label(self, text="Customer Portal")
        title2.grid(row=3, column=0, padx=20, pady=2, columnspan=3)

        # ----Buttons----
        get_tickets_button = ttk.Button(self, text="Get Tickets", command=lambda: controller.show_frame(BuyTickets))
        get_tickets_button.grid(row=4, column=0, padx=20, pady=12, columnspan=3)
        view_ticket_button = ttk.Button(self, text="View Seats", command=lambda: controller.show_frame(ViewSeatsCustomer))
        view_ticket_button.grid(row=5, column=0, padx=20, pady=12, columnspan=3)


class BuyTickets(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ----Home/Current Flight/Sign Out----
        home_button = ttk.Button(self, text="Home", command=lambda: controller.show_frame(CustomerPortal))
        home_button.grid(row=0, column=0, pady=10)
        flight_label = ttk.Label(self, text="Flight NUM")
        flight_label.grid(row=0, column=1, pady=10)
        sign_out_button = ttk.Button(self, text="Sign Out", command=lambda: controller.show_frame(HomePage))
        sign_out_button.grid(row=0, column=2, pady=10)

        # ----Logo and Titles----
        load = Image.open("logo.png")
        load = load.resize((150, 85), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=1, column=0, padx=100, columnspan=3)
        title1 = ttk.Label(self, text="Sunset Chaser Airlines")
        title1.grid(row=2, column=0, padx=20, pady=2, columnspan=3)
        title2 = ttk.Label(self, text="Customer Portal")
        title2.grid(row=3, column=0, padx=20, pady=2, columnspan=3)
        title3 = ttk.Label(self, text="What type of seat(s) do you need?")
        title3.grid(row=4, column=0, padx=20, pady=2, columnspan=3)

        # ----Ticket Options----
        s = tk.StringVar()
        ticket_options = ttk.Combobox(self, state="readonly", width=27, textvariable=s)
        ticket_options['values'] = ('Business Traveler (1) - Business Select',
                                    'Business Traveler (1) - Normal Seating',
                                    'Tourist Travelers (2)',
                                    'Family Travelers (2 adults + 1 child)',
                                    'Family Travelers (2 adults + 2 child)',
                                    'Family Travelers (2 adults + 3 child)')

        ticket_options.grid(row=5, column=0, pady=20, columnspan=3)
        ticket_options.current(0)
        submit = ttk.Button(self, text="Submit", command=lambda: controller.show_frame(ConfirmSeats))
        submit.grid(row=6, column=0, columnspan=3, padx=10)


class ConfirmSeats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ----Home/Current Flight/Sign Out----
        home_button = ttk.Button(self, text="Home", command=lambda: controller.show_frame(CustomerPortal))
        home_button.grid(row=0, column=0, pady=10)
        flight_label = ttk.Label(self, text="Flight NUM")
        flight_label.grid(row=0, column=1, pady=10)
        sign_out_button = ttk.Button(self, text="Sign Out", command=lambda: controller.show_frame(HomePage))
        sign_out_button.grid(row=0, column=2, pady=10)

        # ----Logo and Titles----
        load = Image.open("logo.png")
        load = load.resize((150, 85), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=1, column=0, padx=100, columnspan=3)
        title1 = ttk.Label(self, text="Sunset Chaser Airlines")
        title1.grid(row=2, column=0, padx=20, pady=2, columnspan=3)
        title2 = ttk.Label(self, text="Customer Portal")
        title2.grid(row=3, column=0, padx=20, pady=2, columnspan=3)

        # ----Show Seat Options & Confirm Button----


class TicketGenerated(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ----Home/Current Flight/Sign Out----
        home_button = ttk.Button(self, text="Home", command=lambda: controller.show_frame(CustomerPortal))
        home_button.grid(row=0, column=0, pady=10)
        flight_label = ttk.Label(self, text="Flight NUM")
        flight_label.grid(row=0, column=1, pady=10)
        sign_out_button = ttk.Button(self, text="Sign Out", command=lambda: controller.show_frame(HomePage))
        sign_out_button.grid(row=0, column=2, pady=10)

        # ----Logo and Titles----
        load = Image.open("logo.png")
        load = load.resize((150, 85), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=1, column=0, padx=100, columnspan=3)
        title1 = ttk.Label(self, text="Sunset Chaser Airlines")
        title1.grid(row=2, column=0, padx=20, pady=2, columnspan=3)
        title2 = ttk.Label(self, text="Customer Portal")
        title2.grid(row=3, column=0, padx=20, pady=2, columnspan=3)

        # ----Display Ticket Info----


class ViewSeatsCustomer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ----Home/Current Flight/Sign Out----
        home_button = ttk.Button(self, text="Home", command=lambda: controller.show_frame(CustomerPortal))
        home_button.grid(row=0, column=0, pady=10)
        flight_label = ttk.Label(self, text="Flight NUM")
        flight_label.grid(row=0, column=1, pady=10)
        sign_out_button = ttk.Button(self, text="Sign Out", command=lambda: controller.show_frame(HomePage))
        sign_out_button.grid(row=0, column=2, pady=10)

        # ----Logo and Titles----
        load = Image.open("logo.png")
        load = load.resize((150, 85), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=1, column=0, padx=100, columnspan=3)
        title1 = ttk.Label(self, text="Sunset Chaser Airlines")
        title1.grid(row=2, column=0, padx=20, pady=2, columnspan=3)
        title2 = ttk.Label(self, text="Customer Portal")
        title2.grid(row=3, column=0, padx=20, pady=2, columnspan=3)

        # ----Seat View / Ticket View----


# ------- Manager Pages -------

class ManagerSignIn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        conn = create_connection("airline.db")
        cursor = conn.cursor()

        # ----Logo and Title----
        load = Image.open("logo.png")
        load = load.resize((150, 85), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=0, column=0, columnspan=2)
        title = ttk.Label(self, text="Sunset Chaser Airlines")
        title.grid(row=1, column=0, pady=10, columnspan=2)

        # ---- Login ----
        def logIn():
            user = username1_entry.get()
            pw = pw_entry.get()
            # Check if User/Pass match DB
            with conn:
                cursor.execute("SELECT * FROM MANAGER")
                row = cursor.fetchall()
                for r in row:
                    if r[0] == user:
                        if str(r[1]) == pw:
                            # Navigate To Manager Portal
                            controller.refresh_user(user)
                            controller.show_frame(ManagerPortal)
                            return

            # Throw Error If They Do Not Match
            error1['text'] = "Either the Username or PW is not correct"

        login = ttk.Label(self, text="Manager Login")
        login.grid(row=2, column=0, pady=10, columnspan=2)
        username1_label = ttk.Label(self, text="Username:")
        username1_label.grid(row=3, column=0, padx=10, pady=4)
        username1_entry = ttk.Entry(self, width=20, textvariable=" ")
        username1_entry.grid(row=3, column=1, padx=10, pady=4)
        pw_label = ttk.Label(self, text="Password:")
        pw_label.grid(row=4, column=0, padx=10, pady=4)
        pw_entry = ttk.Entry(self, width=20, show="*")
        pw_entry.grid(row=4, column=1, padx=10, pady=4)
        submit1 = ttk.Button(self, text="Submit", command=lambda: logIn())
        submit1.grid(row=5, column=0, columnspan=2, pady=5)
        error1 = ttk.Label(self, text="", foreground="#ff0000")
        error1.grid(row=6, column=0, columnspan=2, pady=5)

        # ---- Sign Up ----
        def signUp():
            user = username2_entry.get()
            pw1 = pw1_entry.get()
            pw2 = pw2_entry.get()
            code = code_entry.get()
            # Make sure entries are not empty
            if user != "" and pw1 != "" and code != "":

                # Check if username is taken or not
                with conn:
                    cursor.execute("SELECT * FROM MANAGER")
                    row = cursor.fetchall()
                    for r in row:
                        if r[0] == user:
                            error2['text'] = "Username already taken"
                            return

                # Check That PW Match
                if pw1 != pw2:
                    error2['text'] = "Passwords do not match"
                    return

                # Add New Manager to DB
                Manager(user, pw1, code)

                # Navigate To Manager Portal
                controller.refresh_user(user)
                controller.show_frame(ManagerPortal)

        sign_up = ttk.Label(self, text="Need an account? Sign up here")
        sign_up.grid(row=7, column=0, pady=10, columnspan=2)
        username2_label = ttk.Label(self, text="Username:")
        username2_label.grid(row=8, column=0, padx=10, pady=4)
        username2_entry = ttk.Entry(self, width=20)
        username2_entry.grid(row=8, column=1, padx=10, pady=4)
        pw1_label = ttk.Label(self, text="Password:")
        pw1_label.grid(row=9, column=0, padx=10, pady=4)
        pw1_entry = ttk.Entry(self, width=20, show="*")
        pw1_entry.grid(row=9, column=1, padx=10, pady=4)
        pw2_label = ttk.Label(self, text="Re-Enter Password:")
        pw2_label.grid(row=10, column=0, padx=10, pady=4)
        pw2_entry = ttk.Entry(self, width=20, show="*")
        pw2_entry.grid(row=10, column=1, padx=10, pady=4)
        code_label = ttk.Label(self, text="Security Code:")
        code_label.grid(row=11, column=0, padx=10, pady=4)
        code_entry = ttk.Entry(self, width=20, show="*")
        code_entry.grid(row=11, column=1, padx=10, pady=4)
        submit2 = ttk.Button(self, text="Submit", command=lambda: signUp())
        submit2.grid(row=12, column=0, columnspan=2, pady=5)
        error2 = ttk.Label(self, text="", foreground="#ff0000")
        error2.grid(row=13, column=0, columnspan=2, pady=5)

        # ---- Button Back To Customer Portal ----
        manager_button = ttk.Button(self, text="Customer Portal", command=lambda: controller.show_frame(HomePage))
        manager_button.grid(row=14, column=0, pady=20, columnspan=2)


class ManagerPortal(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ----Home/Current Flight/Sign Out----
        home_button = ttk.Button(self, text="Home", command=lambda: controller.show_frame(ManagerPortal))
        home_button.grid(row=0, column=0, pady=10)
        flight_label = ttk.Label(self, text="Flight NUM")
        flight_label.grid(row=0, column=1, pady=10)
        sign_out_button = ttk.Button(self, text="Sign Out", command=lambda: controller.show_frame(ManagerSignIn))
        sign_out_button.grid(row=0, column=2, pady=10)

        # ----Logo and Titles----
        load = Image.open("logo.png")
        load = load.resize((150, 85), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=1, column=0, padx=100, columnspan=3)
        title1 = ttk.Label(self, text="Sunset Chaser Airlines")
        title1.grid(row=2, column=0, padx=20, pady=2, columnspan=3)
        title2 = ttk.Label(self, text="Manager Portal")
        title2.grid(row=3, column=0, padx=20, pady=2, columnspan=3)

        # ----Buttons----
        report_button = ttk.Button(self, text="Satisfactory Report", command=lambda: controller.show_frame(SatisfactoryScore))
        report_button.grid(row=4, column=0, padx=20, pady=12, columnspan=3)
        end_flight_button = ttk.Button(self, text="End Flight", command=lambda: controller.show_frame(EndFlight))
        end_flight_button.grid(row=5, column=0, padx=20, pady=12, columnspan=3)
        view_seats_button = ttk.Button(self, text="View Seats", command=lambda: controller.show_frame(ViewSeatsManager))
        view_seats_button.grid(row=6, column=0, padx=20, pady=12, columnspan=3)


class EndFlight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ----Home/Current Flight/Sign Out----
        home_button = ttk.Button(self, text="Home", command=lambda: controller.show_frame(ManagerPortal))
        home_button.grid(row=0, column=0, pady=10, columnspan=3)
        flight_label = ttk.Label(self, text="Flight NUM")
        flight_label.grid(row=0, column=3, pady=10, columnspan=6)
        sign_out_button = ttk.Button(self, text="Sign Out", command=lambda: controller.show_frame(ManagerSignIn))
        sign_out_button.grid(row=0, column=9, pady=10, columnspan=3)

        # ----Logo and Titles----
        load = Image.open("logo.png")
        load = load.resize((150, 85), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=1, column=0, padx=100, columnspan=12)
        title1 = ttk.Label(self, text="Sunset Chaser Airlines")
        title1.grid(row=2, column=0, padx=20, pady=2, columnspan=12)
        title2 = ttk.Label(self, text="Manager Portal")
        title2.grid(row=3, column=0, padx=20, pady=7, columnspan=12)

        def endFlight():
            f = Flight()
            f.end_flight()
            f.create_new_flight()
            controller.show_frame(ManagerPortal)

        # ----End The Flight----
        confirm_text = ttk.Label(self, text="Are you sure you would like to end this flight?")
        confirm_text.grid(row=4, column=0, padx=20, pady=10, columnspan=12)
        confirm_button = ttk.Button(self, text="Confirm", command=lambda: endFlight())
        confirm_button.grid(row=5, column=0, padx=20, pady=2, columnspan=12)


class ViewSeatsManager(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ----Home/Current Flight/Sign Out----
        home_button = ttk.Button(self, text="Home", command=lambda: controller.show_frame(ManagerPortal))
        home_button.grid(row=0, column=0, pady=10, columnspan=3)
        flight_label = ttk.Label(self, text="Flight NUM")
        flight_label.grid(row=0, column=3, pady=10, columnspan=6)
        sign_out_button = ttk.Button(self, text="Sign Out", command=lambda: controller.show_frame(ManagerSignIn))
        sign_out_button.grid(row=0, column=9, pady=10, columnspan=3)

        # ----Logo and Titles----
        load = Image.open("logo.png")
        load = load.resize((150, 85), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=1, column=0, padx=100, columnspan=12)
        title1 = ttk.Label(self, text="Sunset Chaser Airlines")
        title1.grid(row=2, column=0, padx=20, pady=2, columnspan=12)
        title2 = ttk.Label(self, text="Manager Portal")
        title2.grid(row=3, column=0, padx=20, pady=7, columnspan=12)

        # ----Display Seat GUI----
        f = Flight()
        seats = f.get_seats()
        r = 4
        c = 0
        for i in range(len(seats)):
            if seats[i] == 'None':
                color = 'green'
            else:
                color = 'red'
            s = ttk.Label(self, text=f.get_seat_number(i), foreground=color)
            s.grid(row=r, column=c, padx=5, pady=5)
            c += 1
            if c == 12:
                c = 0
                r += 1


class SatisfactoryScore(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        conn = create_connection("airline.db")
        cursor = conn.cursor()
        f = Flight()

        # ----Home/Current Flight/Sign Out----
        home_button = ttk.Button(self, text="Home", command=lambda: controller.show_frame(ManagerPortal))
        home_button.grid(row=0, column=0, pady=10, columnspan=3)
        flight_label = ttk.Label(self, text="Flight NUM")
        flight_label.grid(row=0, column=3, pady=10, columnspan=6)
        sign_out_button = ttk.Button(self, text="Sign Out", command=lambda: controller.show_frame(ManagerSignIn))
        sign_out_button.grid(row=0, column=9, pady=10, columnspan=3)

        # ----Logo and Titles----
        load = Image.open("logo.png")
        load = load.resize((150, 85), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=1, column=0, padx=100, columnspan=12)
        title1 = ttk.Label(self, text="Sunset Chaser Airlines")
        title1.grid(row=2, column=0, padx=20, pady=2, columnspan=12)
        title2 = ttk.Label(self, text="Manager Portal")
        title2.grid(row=3, column=0, padx=20, pady=7, columnspan=12)

        # ----Display Score----
        info1 = ttk.Label(self, text="The Satisfaction Idex reflects a group of randomly chosen customers")
        info2 = ttk.Label(self, text="and their satisfaction with the flight.")
        info1.grid(row=4, column=0, padx=5, columnspan=12)
        info2.grid(row=5, column=0, padx=5, columnspan=12)

        # get previous flight score
        flight_num = f.number - 1
        with conn:
            cursor.execute("SELECT * FROM FLIGHT WHERE NUMBER=?", (flight_num,))

        rows = cursor.fetchall()
        score = rows[0][1]

        score_label = tk.Label(self, text=str(score))
        score_label.grid(row=6, column=0, pady=15, columnspan=12)
