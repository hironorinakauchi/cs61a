def GCD(n1, n2):
	if n1 % n2 == 0:
		return n2
	else:
		return gcd(n2, n1%n2)

def gcd(m, n):
	if m == n:
		return m
	elif m > n:
		return gcd(m-n, n)
	else:
		return gcd(m, n-m)

def make_rat(n, d):
	"""the rational number n/d, assuming n, d are integers, d != 0"""
	g = gcd(n, d)
	n //= g
	d //= g
	return lambda flag: n if flag == 0 else d

def numer(r):
	"""the numerator of rational number r"""
	n0, n1, d0, d1 = x(0), y(0), x(1), y(1)
	n, d = n0 * d1 + n1 * d0, d0 * d1
	# instead of doing this below you could do make_rat again
	# since its doing the same thing
	g = gcd(n,d)
	n, d = n // g, d // g
	return lambda flag: n if flag == 0 else d 

def denom(r):
	"""the denominator of rational number r"""
# these functions can be replaced with...


def add_rat(x, y):
	return make_rat(numer(x) * denom(y) + numer(y) * denom(x),
					denom(x) * denom(y))

def mul_rat(x, y):
	return make_rat(numer(x) * numer(y), denom(x) * denom(y))