import time
from contextlib import contextmanager


class cm_timer_1():
    def __init__(self):
        pass

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('time:', time.perf_counter()-self.start)


@contextmanager
def cm_timer_2():
    a = time.perf_counter()
    yield
    print('time:', time.perf_counter()-a)
