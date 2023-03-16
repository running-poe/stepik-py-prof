import time
import calendar



def func(*args):
	count = args[0]
	res = []
	for y in args[1:]:
		res.append(str(calendar.isleap(int(y))))

	return res
'''
n = int(input())
inp = []

for i in range(n):
	inp.append(input())

for el in inp:
	print(calendar.isleap(int(el)))

'''