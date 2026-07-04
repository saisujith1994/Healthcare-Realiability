import random

def get_claims_from_api():

    if random.random() < 0.5:
        raise Exception("API is down")
    return [
        {
            "claims_id": 1,
            "amount": 1000.00
        },
        {
            "claims_id": 2,
            "amount": 2000.00
        }
    ]