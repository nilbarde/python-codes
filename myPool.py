import multiprocessing
import time
from tqdm import tqdm

class MultiprocessingTimer:
    def __init__(self, target, args=(), kwargs=None, timeout=None, max_workers=None):
        """
        Initialize the MultiprocessingTimer object.

        Args:
            target (function): The target function to be executed in parallel.
            args (tuple): The arguments to be passed to the target function.
            kwargs (list): The list of dictionaries, each representing keyword arguments for the corresponding task.
            timeout (float): The maximum duration (in seconds) for the tasks to run.
            max_workers (int): The maximum number of worker processes.

        """
        self.target = target
        self.args = args
        self.kwargs = kwargs or [{}] * len(args)  # If kwargs is not provided, default to empty dictionary for each task
        self.timeout = timeout
        self.max_workers = max_workers

    def run(self):
        """
        Execute the target function in parallel using multiprocessing.

        Returns:
            list: A list of tuples containing the original arguments and the corresponding results.

        """
        results = []
        completed_tasks = 0

        with multiprocessing.Pool(processes=self.max_workers) as pool:
            # Submit tasks to the pool
            tasks = [pool.apply_async(self.target, arg, kwarg) for arg, kwarg in zip(self.args, self.kwargs)]

            # Create a progress bar
            with tqdm(total=len(tasks), desc="Tasks completed") as pbar:
                start_time = time.time()
                while time.time() - start_time < self.timeout:
                    time.sleep(1)
                    completed_tasks = sum(task.ready() for task in tasks)
                    pbar.update(completed_tasks - pbar.n)

                # Terminate the remaining tasks
                pool.terminate()

                # Collect the results
                for task, arg, kwarg in zip(tasks, self.args, self.kwargs):
                    if task.ready():
                        result = task.get()
                        results.append((arg, result))
                    else:
                        results.append((arg, None))

        return results
