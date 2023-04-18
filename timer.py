"""
Timer class

"""
import time


class Timer:
    def __init__(self):
        self.start_time = time.time()
        self.time = 0

    def update_time(self):
        current_time = time.time()
        self.time = current_time - self.start_time

    def reset_timer(self):
        self.start_time = time.time()

    def get_time(self):
        return self.time

    def __str__(self):
        return time.strftime("%M:%S", time.gmtime(self.time))
