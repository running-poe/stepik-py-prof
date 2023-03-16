import time

def add(*args):
	return sum(*args)

def calculate_it(func, *args):
	start_time = time.perf_counter()
	res = func(args)
	res_time = time.perf_counter() - start_time
	return res, res_time

print(calculate_it(add, 1, 2))

