import time


class TimerContextManager:
    def __init__(self):
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"Time taken: {elapsed_time} seconds")


with TimerContextManager():
    result = 1
    for i in range(1, 100001):
        result *= i
    print(result)
    
