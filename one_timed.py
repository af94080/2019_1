import time

def timeit(func):
	def exec_func(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()	
		print(f'func took {end-start} seconds')
		return result
	return exec_func


@timeit
def fibonacci(n):
	"""return nth element of fib series"""
	if n < 2:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
