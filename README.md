# Multiprocessing code

# myPool class


initialization arguments
1. poolsize
	- type: int
	- description:
		- size of multiprocessing thread
		- poolsize numbers of threads will be created to execute the process
2. max_time
	- type: int
	- description:
		- max allowed execution time (in seconds)
		- after max_time pool will be terminated
		- all uncomplete threads will be returned as None
3. update_interval
	- type: int
	- description:
		- progress will be updated every update_interval seconds
		- time spent on execution of threads will be checked after every progress update
			- if time spent is more than max_time then pool will be terminated



start function arguments
1. Inputs
	1. fun
		- type: callable function
		- description:
			- function accepting n number of arguments
	2. args_list
		- type: iterable object
		- description:
			- start function will call fun with every argument in args_list
			- list of tuple is one example for args_list
			- refer example-1 for function accepting 2 arguments
			- refer example-2 for function accepting no argument
2. Returns
	1. res
		- list of returns from fun on args_list
