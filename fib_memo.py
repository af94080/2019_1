from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1} # the base cases

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
def fib(n: int) -> int:
	if n not in memo:
		memo[n] = fib(n-1) + fib(n-2) # memoization
	return memo[n]

print(fib(10))
