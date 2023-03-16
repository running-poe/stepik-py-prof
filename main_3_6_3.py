import time
from math import factorial                   # функция из модуля math


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

start_time = time.perf_counter()
factorial_recurrent(100)
res_time = time.perf_counter() - start_time
print(res_time)

start_time = time.perf_counter()
factorial_classic(100)
res_time = time.perf_counter() - start_time
print(res_time)

start_time = time.perf_counter()
factorial(100)
res_time = time.perf_counter() - start_time
print(res_time)

