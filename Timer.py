import time

class Timer:
    def __init__(self):
        self.end_time = time.time()
     
    def is_over(self, start_time_, second):
        self.end_time = time.time()
        if self.end_time - start_time_ >= second:
            return True
        return False