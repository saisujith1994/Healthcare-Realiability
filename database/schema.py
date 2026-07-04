from database.db import get_connection

def create_tables():
    conn= get_connection()
    cursor= conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS claims (
        claims_id INTEGER PRIMARY KEY,
        patient_id INTEGER,
        allowed_amount REAL,
        primary_paid_amount REAL,
        secondary_paid_amount REAL
    )""")

    conn.commit()
    conn.close()
if __name__=="__main__":
    create_tables()