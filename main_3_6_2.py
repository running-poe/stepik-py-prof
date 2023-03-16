import time

def get_the_fastest_func(funcs, arg):
	res = []
	for f in funcs:
		start_time = time.perf_counter()
		f(arg)
		res_time = time.perf_counter() - start_time
		res.append((f, res_time))

	res.sort(key=lambda x: x[1])
	return res[0][0]

def add(a):
    time.sleep(3)
    return a + a
def minus(a):
    time.sleep(2)
    return a - a
def multyp(a):
    time.sleep(4)
    return a*a

funcs = [add, minus, multyp]

print(get_the_fastest_func(funcs, 2))