import tkinter as tk
from tkinter import ttk

from GUIPages import HomePage, ViewSeatsCustomer, CustomerPortal, BuyTickets, ConfirmSeats, TicketGenerated
from GUIPages import ManagerSignIn, ManagerPortal, ViewSeatsManager, EndFlight, SatisfactoryScore


class GUIContainer(tk.Tk):

    def __init__(self, user="", type="", *args, **kwargs,):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.title("Sunset Chaser Airlines")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # styling for widgets
        style = ttk.Style(self)
        style.theme_use('classic')  # need to do this on mac
        style.configure('TLabel', background='white', foreground='black')
        style.configure('TButton', background='white', foreground='black')
        style.configure('TEntry', background='white', foreground='black')
        style.configure('TCombobox', selectbackground='white', background='orange', foreground='black')

        # initializing frames to an empty array
        self.frames = {}

        # variable to know who is logged in and helps with page info related to user
        self.USER = user
        self.USERTYPE = type

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (HomePage, ManagerSignIn, CustomerPortal, BuyTickets, ConfirmSeats, TicketGenerated,
                  ViewSeatsCustomer, ManagerPortal, ViewSeatsManager, EndFlight, SatisfactoryScore):

            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def refresh_user(self, user, type):
        self.destroy()
        self.__init__(user, type)
