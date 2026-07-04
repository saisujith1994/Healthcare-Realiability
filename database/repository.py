from database.db import get_connection

def insert_claims(claim):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO claims (claims_id, patient_id, allowed_amount, primary_paid_amount, secondary_paid_amount)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(claims_id) DO NOTHING
    """, (claim["claims_id"], claim["patient_id"], claim["allowed_amount"], claim["primary_paid_amount"], claim["secondary_paid_amount"]))

    conn.commit()
    conn.close()
def get_all_claims():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM claims")
    claims = cursor.fetchall()

    conn.close()
    return claims