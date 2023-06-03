MultiprocessingTimer
====================

MultiprocessingTimer is a Python class that enables executing a target function in parallel using multiprocessing. It provides a convenient way to distribute tasks among multiple worker processes and track their progress.

Usage
-----

To use the MultiprocessingTimer class, follow these steps:

1. Import the necessary modules:

    ```python
    from multiprocessing_timer_class import MultiprocessingTimer
    ```

2. Define your target function. This function will be executed in parallel for each task:

    ```python
    def my_function(arg, kwarg1=None, kwarg2=None):
        result = 0
        # Your target function code here
        # ...
        return result
    ```

3. Create an instance of the MultiprocessingTimer class, providing the target function, arguments, and optional parameters:

    ```python
    args = [1, 2, 3, 4, 5]
    kwargs = [{'kwarg1': 'value1'}, {'kwarg2': 'value2'}, {}, {}, {'kwarg1': 'value3', 'kwarg2': 'value4'}]
    timer = MultiprocessingTimer(target=my_function, args=args, kwargs=kwargs, timeout=6, max_workers=2, progress_update_interval=2)
    ```

4. Call the `run()` method to start the parallel execution:

    ```python
    results = timer.run()
    ```

5. The `run()` method returns a list containing the results of the completed tasks. You can iterate over the results to process them as needed.

Features
--------

- Executes a target function in parallel for each task using multiprocessing.
- Supports passing arguments to the target function through the `args` parameter.
- Supports passing keyword arguments to the target function through the `kwargs` parameter, where each task can have its own set of keyword arguments.
- Allows specifying a timeout for the tasks using the `timeout` parameter.
- Provides a progress bar using the `tqdm` library to track the completion of tasks.
- Allows controlling the frequency of updates to the progress bar using the `progress_update_interval` parameter.
- Terminates the remaining tasks if the timeout is reached.
- Collects and returns the results of completed tasks.

Dependencies
------------

The following dependencies are required to use the MultiprocessingTimer class:

- `multiprocessing`: The built-in multiprocessing module in Python.
- `time`: The built-in time module in Python.
- `tqdm`: A Python library for creating progress bars.

Installation
------------

To install the required dependencies, use the following command:

```sh
pip install tqdm
```
