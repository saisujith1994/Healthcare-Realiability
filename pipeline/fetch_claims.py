import requests

def fetch_claims():
    url ="http://localhost:5000/claims"

    try:
        response=requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        print("[INFO] Api call successful.")
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Api call failed: {e}")
        return []
if __name__=="__main__":
    claims= fetch_claims()

    for c in claims:
        print("----------------------------")
        print(f"Claims ID: {c['claims_id']}\nPatient ID: {c['patient_id']}\nAllowed Amount: {c['allowed_amount']}\nPrimary Paid Amount: {c['primary_paid_amount']}\nSecondary Paid Amount: {c['secondary_paid_amount']}")
