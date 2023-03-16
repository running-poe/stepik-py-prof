import time


def for_and_append(iterable):  # с использованием цикла for и метода append()
	result = []
	for elem in iterable:
		result.append(elem)
	return result


def list_comprehension(iterable):  # с использованием списочного выражения
	return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
	return list(iterable)


start_time = time.monotonic()
for_and_append(range(1_000_000))
res_time = time.monotonic() - start_time
print(res_time)

start_time = time.monotonic()
list_comprehension(range(1_000_000))
res_time = time.monotonic() - start_time
print(res_time)

start_time = time.monotonic()
list_function(range(1_000_000))
res_time = time.monotonic() - start_time
print(res_time)

