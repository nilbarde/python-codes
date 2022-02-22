from multiprocessing import Pool
import time
from tqdm import tqdm


def caller(args):
    i, fun, args_call = args
    return (i, fun(*args_call))


class myPool(object):
    def __init__(self, poolsize=4, max_time=6000, update_interval=1):
        """
        Input:
            poolsize:
                multiprocessing number of threads
            max_time:
                maximum time required to execute all tasks (in seconds)
                note:
                    after time limit all working threads will be closed
                    all incomplete nodes will return None
            update_interval:
                progress will be updated every (update_interval) seconds
        """
        self.poolsize = poolsize
        self.pool = Pool(self.poolsize)
        self.time_max = max_time
        self.time_status = update_interval

    def callback(self, args):
        """
        Internal function to store results
        Do not call from outside
        """
        i, res = args
        self.results[i] = res

    def start(self, fun=None, args_list=[]):
        """
        Function to be called
        Inputs:
            fun:
                function to be called
            args_list:
                list of arguments to be passed to fun
                note:
                    args_list should be list of tuple
                    tuple can contain multiple arguments
        """
        self.fun = fun
        self.args_list = args_list

        self.calls = []
        self.results = [None for _ in range(len(self.args_list))]
        for i, args in enumerate(self.args_list):
            call = self.pool.apply_async(
                caller,
                args=((i, self.fun, args), ),
                callback=self.callback
            )
            self.calls.append(call)

        self.time_start = time.time()
        self.total_threads = len(self.args_list)
        time_spent = 0
        self.progress = tqdm(total=self.total_threads, desc="Pool", position=0)

        while (time_spent < self.time_max) and self.calls:
            time.sleep(self.time_status)
            remaining_calls = []
            for call in self.calls:
                try:
                    call.successful()
                except:
                    remaining_calls.append(call)
            time_now = time.time()
            time_spent = time_now - self.time_start
            self.progress.update(len(self.calls) - len(remaining_calls))
            self.calls = remaining_calls[:]

        self.pool.terminate()
        self.pool.close()
        self.pool.join()
        res = self.results

        self.progress.close()
        self.clear_memory()

        return res

    def clear_memory(self):
        del self.results
        del self.calls
        del self.progress
        del self.total_threads
        del self.time_start
        del self.time_max
        del self.time_status
        del self.fun
        del self.args_list
        del self.poolsize
