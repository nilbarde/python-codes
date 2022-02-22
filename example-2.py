from myPool import myPool
import time


def wait_print():
    time.sleep(1)
    return -1


if __name__ == "__main__":
    x = [(), (), (), (), (), ()]

    pool = myPool(4, max_time=7)
    results = pool.start(wait_print, x)
    print(results)
