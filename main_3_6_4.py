import time


def for_and_append():  # с использованием цикла for и метода append()
	iterations = 10_000_0000
	result = []
	for i in range(iterations):
		result.append(i + 1)
	return result


def list_comprehension():  # с использованием списочного выражения. ВОТ ЭТО БЫСТРЕЕ РАБОТАЕТ!
	iterations = 10_000_0000
	return [i + 1 for i in range(iterations)]

start_time = time.monotonic()
for_and_append()
res_time = time.monotonic() - start_time
print(res_time)

start_time = time.monotonic()
list_comprehension()
res_time = time.monotonic() - start_time
print(res_time)


