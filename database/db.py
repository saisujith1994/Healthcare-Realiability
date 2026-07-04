import sqlite3

DATABASE = "data/claims.db"

def get_connection():

    return sqlite3.connect(DATABASE)