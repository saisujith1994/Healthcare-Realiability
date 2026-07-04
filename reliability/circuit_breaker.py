import time
from reliability.state import State

class CircuitBreaker:
    def __init__(self, failure_threshold=3, recovery_timeout=10):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.state = State.CLOSED
        self.last_failure_time = None
    
    def call(self, func, *args, **kwargs):
        if self.state==State.OPEN:
            if time.time()- self.last_failure_time> self.recovery_timeout:
                self.state= State.HALF_OPEN
            else:
                print("[CIRCUIT OPEN] Circuit is open. Request blocked.")
                return None
        try:
            result= func(*args, **kwargs)
            self._reset()
            return result
        except Exception as e:
            self._record_failure()
            print(f"[ERROR] {e}")
            return None
    def _reset(self):
        self.failure_count=0
        self.state= State.CLOSED
        self.last_failure_time= None
    
    def _record_failure(self):
        self.failure_count+=1
        self.last_failure_time= time.time()
        if self.failure_count>= self.failure_threshold:
            self.state= State.OPEN
            print("[CIRCUIT OPEN] Circuit is now open due to repeated failures.")