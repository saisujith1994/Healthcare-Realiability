from reliability.circuit_breaker import CircuitBreaker
from api.faulty_api import get_claims_from_api

cb= CircuitBreaker(failure_threshold=3, recovery_timeout=10)

for i in range(10):
    print(f"[INFO] Attempt {i+1}: Fetching claims from API...")
    claims= cb.call(get_claims_from_api)
    print(f"[INFO] Claims fetched: {claims}")