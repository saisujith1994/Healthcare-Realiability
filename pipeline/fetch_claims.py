import requests
from database.repository import insert_claims, get_all_claims
from database.analytics import get_overpaid_patients

def fetch_claims():
    url ="http://localhost:5000/claims"

    try:
        response=requests.get(url,timeout=5)
        response.raise_for_status()  # Raise an exception for HTTP errors

        print("[INFO] Api call successful.")
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Api call failed: {e}")
        return []

def run_pipeline():
    print("[INFO] Starting the pipeline execution...")

    claims= fetch_claims()

    for claim in claims:

        total_paid= claim["primary_paid_amount"] + claim["secondary_paid_amount"]   
        if total_paid<=0:
            print(f"[WARNING] Claim ID {claim['claims_id']} has zero or negative total paid amount. Skipping insertion.")
            continue

        print(f"[INFO] Inserting claim ID {claim['claims_id']} into the database.")
        insert_claims(claim)

    print("[INFO] Pipeline execution completed.")





if __name__=="__main__":

    run_pipeline()
    print("[INFO] Fetching all claims from the database...")

    claims= get_all_claims()

    for c in claims:
        print("----------------------------")
        print(f"Claims ID: {c['claims_id']}\nPatient ID: {c['patient_id']}\nAllowed Amount: {c['allowed_amount']}\nPrimary Paid Amount: {c['primary_paid_amount']}\nSecondary Paid Amount: {c['secondary_paid_amount']}")
    
    print("[INFO] Fetching overpaid patients...")
    overpaid_patients = get_overpaid_patients()

    if not overpaid_patients:
        print("[INFO] No overpaid patients found.")
    else:
        print("[INFO] Overpaid patients:")
        for patient in overpaid_patients:
            print(f"Patient ID: {patient['patient_id']}, Overpaid Amount: {patient['overpaid_amount']}")