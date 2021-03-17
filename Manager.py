import sqlite3
from sqlite3 import Error


class Manager:

    def __init__(self, username, password, auth_code):
        self.username = username
        self.password = password
        self.auth_code = auth_code

        # ---- Add To Database ----
        def create_connection(file):
            conn = None
            try:
                conn = sqlite3.connect(file)
            except Error as e:
                print(e)
            return conn

        conn = create_connection("airline.db")
        c = conn.cursor()

        insert_string = "INSERT INTO MANAGER (USER, PASSWORD, AUTH_CODE) VALUES (?, ? , ?)"

        with conn:
            c.execute(insert_string, [self.username, str(self.password), int(self.auth_code)])
