from reliability.circuit_breaker import CircuitBreaker
from api.faulty_api import get_claims_from_api
from database.repository import insert_claims
from database.analytics import get_overpaid_patients

def run_system():
    print("[INFO] Starting the system execution...")
    cb= CircuitBreaker(failure_threshold=2, recovery_timeout=5)

    print("[INFO] Fetching claims from API with circuit breaker...")
    claims= cb.call(get_claims_from_api)
    if not claims:
        print("[INFO] No claims fetched from API.")
        return
    print(f"[INFO] Loading into Database: {len(claims)} claims fetched.")

    for claim in claims:
        try:
            insert_claims([{
                "claim_id": int(claim["claims_id"]),
                "patient_id": 100,   # simplified for demo
                "allowed_amount": 150,
                "primary_paid": claim["amount"] * 0.6,
                "secondary_paid": claim["amount"] * 0.4
            }])
            print(f"[INFO] Claim ID {claim['claims_id']} inserted into the database.")
        except Exception as e:
            print(f"[ERROR] Failed to insert claim ID {claim['claims_id']}: {e}")
    print("[INFO] Running analytics to find overpaid patients...")
    overpaid_patients = get_overpaid_patients()
    if overpaid_patients:
        print("[INFO] Overpaid patients found:")
        for patient in overpaid_patients:
            print(f"Patient ID: {patient['patient_id']}, Overpaid Amount: {patient['overpaid_amount']}")
    else:
        print("[INFO] No overpaid patients found.")
    print("[INFO] System execution completed.")

if __name__=="__main__":
    run_system()