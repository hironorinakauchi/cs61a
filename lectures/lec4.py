def sum_squares(n):
	"""
	the sum of K**2 from 1 to N (inclusive)
	"""
	if n < 1:
		return 0
	else:
		return n**2 + sum_squares(n-1)

# how do we do the same thing with a while loop?

def sum_squares2(n):
	total, c = 0, 1
	while c <= n:
		total, c = total + c**2, c + 1
	return total

# fibinacci sequence

def fib(n):
	"""the n Fibonacci number, N>=0"""
	assert n >= 0
	if n <= 1:
		return n
	else:
		return fib(n-2) + fib(n-1)

# but this function takes long time to compute so...

def fib2(fk1, fk, k, n):
	"""assuming Fk1 and Fk2 are fib(k-1) and fib(k) in the Fibonacci
	sequence and that N>=K, return fib(N)."""
	if n == k: return fk
	else:	   return fib2(fk, fk1+fk, k+1, n)
def fib(n):
	if n <= 1: return n
	else:	   return fib2(0, 1, 1, n)

# or you can turn one of these above into iteration like below
# optimization: since the var. n doesn't change, just leave it off

def fib3(n):
	if n <= 1: return n
	fk1, fk, k = 0, 1, 1
	while n != k:
		fk1, fk, k = fk, fk1+fk, k+1
	return fk

# but fib2 is just an auxiliary function. you can tuck it away inside fib
# called "nested function"

def fib(n):
	def fib2(fk1, fk, k):
		if n == k: return fk
		else:	   return fib2(fk, fk1 + fk, k+1)
	if n <= 1:	return n
	else: 		return fib2(0, 1, 1)