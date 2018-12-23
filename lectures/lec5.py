from operator import add
def combine_funcs(op):
	def combined(f,g):
		def eval(x):
			return op(f(x), g(x))
		return eval
	return combined 

# add_func = combine_funcs(add)

def newton_solve(func, deriv, start, tolerace):
	def close_enough(x):
		return abs(func(x)) < tolerance
	def newton_update(x):
		return x - func(x) / deriv(x)

def square_root(a):
	return newton_solve(lambda x: x*x - a, lambda x: 2*x,
						a/2, 1e-5)

def logarithm(a, base=2):
	return newton_solve(lambda x: base**x-a,
						lambda x: x*base**(x-1),
						1, 1e-5)

