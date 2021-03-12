import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import sqlite3
from sqlite3 import Error

from Customer import Customer
from Manager import Manager
from Flight import Flight


class GUIContainer(tk.Tk):

    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # styling for widgets
        style = ttk.Style(self)
        style.theme_use('classic') # need to do this on mac
        style.configure('TLabel', background='white', foreground='black')
        style.configure('TButton', background='white', foreground='black')
        style.configure('TEntry', background='white', foreground='black')

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (HomePage, ManagerSignIn, CustomerPortal, BuyTickets, ViewSeatsCustomer, ManagerPortal,
                  ViewSeatsManager, EndFlight, SatisfactoryScore):

            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

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
        login = ttk.Label(self, text="Login")
        login.grid(row=2, column=0, pady=10, columnspan=2)
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(row=3, column=0, padx=10, pady=4)
        username_entry = ttk.Entry(self, width=20)
        username_entry.grid(row=3, column=1, padx=10, pady=4)
        pw_label = ttk.Label(self, text="Password:")
        pw_label.grid(row=4, column=0, padx=10, pady=4)
        pw_entry = ttk.Entry(self, width=20, show="*")
        pw_entry.grid(row=4, column=1, padx=10, pady=4)
        submit1 = ttk.Button(self, text="Submit", command=lambda: controller.show_frame(CustomerPortal))
        submit1.grid(row=5, column=0, columnspan=2, pady=5)

        # ---- Sign Up ----
        sign_up = ttk.Label(self, text="Need an account? Sign up here")
        sign_up.grid(row=6, column=0, pady=10, columnspan=2)
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(row=7, column=0, padx=10, pady=4)
        username_entry = ttk.Entry(self, width=20)
        username_entry.grid(row=7, column=1, padx=10, pady=4)
        pw1_label = ttk.Label(self, text="Password:")
        pw1_label.grid(row=8, column=0, padx=10, pady=4)
        pw1_entry = ttk.Entry(self, width=20, show="*")
        pw1_entry.grid(row=8, column=1, padx=10, pady=4)
        pw2_label = ttk.Label(self, text="Re-Enter Password:")
        pw2_label.grid(row=9, column=0, padx=10, pady=4)
        pw2_entry = ttk.Entry(self, width=20, show="*")
        pw2_entry.grid(row=9, column=1, padx=10, pady=4)
        submit2 = ttk.Button(self, text="Submit", command=lambda: controller.show_frame(CustomerPortal))
        submit2.grid(row=10, column=0, columnspan=2, pady=5)

        # ---- Button To Manager Portal ----
        manager_button = ttk.Button(self, text="Manager Portal", command=lambda: controller.show_frame(ManagerSignIn))
        manager_button.grid(row=11, column=0, pady=20, columnspan=2)


class ManagerSignIn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="2")
        label.grid(row=0, column=4, padx=10, pady=10)
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(CustomerPortal))
        button1.grid(row=1, column=1, padx=10, pady=10)


class CustomerPortal(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="3")
        label.grid(row=0, column=4, padx=10, pady=10)
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(BuyTickets))
        button1.grid(row=1, column=1, padx=10, pady=10)


class BuyTickets(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="4")
        label.grid(row=0, column=4, padx=10, pady=10)
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(ViewSeatsCustomer))
        button1.grid(row=1, column=1, padx=10, pady=10)


class ViewSeatsCustomer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="5")
        label.grid(row=0, column=4, padx=10, pady=10)
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(ManagerPortal))
        button1.grid(row=1, column=1, padx=10, pady=10)


class ManagerPortal(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="6")
        label.grid(row=0, column=4, padx=10, pady=10)
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(EndFlight))
        button1.grid(row=1, column=1, padx=10, pady=10)


class EndFlight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="7")
        label.grid(row=0, column=4, padx=10, pady=10)
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(ViewSeatsManager))
        button1.grid(row=1, column=1, padx=10, pady=10)


class ViewSeatsManager(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="8")
        label.grid(row=0, column=4, padx=10, pady=10)
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(SatisfactoryScore))
        button1.grid(row=1, column=1, padx=10, pady=10)


class SatisfactoryScore(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="9")
        label.grid(row=0, column=4, padx=10, pady=10)
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(HomePage))
        button1.grid(row=1, column=1, padx=10, pady=10)



