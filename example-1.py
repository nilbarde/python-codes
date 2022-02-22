from myPool import myPool
import time


def wait_print(t, p):
    time.sleep(t)
    return p**2


if __name__ == "__main__":
    x = [(1, 1), (3, 2), (2, 3), (10, 4), (2, 5), (3, 7)]

    pool = myPool(4, max_time=7)
    results = pool.start(wait_print, x)
    print(results)
