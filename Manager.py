from Connection import create_connection


class Manager:

    def __init__(self, username, password, auth_code):
        self.username = username
        self.password = password
        self.auth_code = auth_code

        conn = create_connection("airline.db")
        c = conn.cursor()

        # Add To Database
        insert_string = "INSERT INTO MANAGER (USER, PASSWORD, AUTH_CODE) VALUES (?, ? , ?)"
        with conn:
            c.execute(insert_string, [self.username, str(self.password), int(self.auth_code)])

