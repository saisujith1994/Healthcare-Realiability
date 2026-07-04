from database.db import get_connection

def get_overpaid_patients():
    conn=get_connection()
    cursor= conn.cursor()
    cursor.execute("""
    SELECT patient_id, SUM(primary_paid_amount + secondary_paid_amount - allowed_amount) AS overpaid_amount
    FROM claims
    GROUP BY patient_id
    having SUM(primary_paid_amount + secondary_paid_amount - allowed_amount)> sum(allowed_amount)""")

    results = cursor.fetchall()
    conn.close()

    return results