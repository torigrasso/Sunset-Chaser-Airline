import sqlite3
from sqlite3 import Error


def create_connection(file):
    conn = None
    try:
        conn = sqlite3.connect(file)
    except Error as e:
        print(e)
    return conn
