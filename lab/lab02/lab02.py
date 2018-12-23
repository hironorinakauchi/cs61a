"""Lab 2: Higher Order Functions & Lambdas & Recursions"""

def lambda_curry2(func):
    """
    Returns a Curried version of a two argument function func.
    >>> from operator import add
    >>> x = lambda_curry2(add)
    >>> y = x(3)
    >>> y(5)
    8
    """
    "*** YOUR CODE HERE ***"
    # return lambda x, z: func(x, z)
    return lambda x: lambda y: func(x, y)


def adder(f1, f2):
    """
    Return a function that takes in a single variable x, and returns
    f1(x) + f2(x). You can assume the result of f1(x) and f2(x) can be
    added together, and they both take in one argument.

    >>> identity = lambda x: x       # returns input
    >>> square = lambda x: x**2
    >>> a1 = adder(identity, square) # x + x^2
    >>> a1(4)
    20
    >>> a2 = adder(a1, identity)     # (x + x^2) + x
    >>> a2(4)
    24
    >>> a2(5)
    35
    >>> a3 = adder(a1, a2)           # (x + x^2) + (x + x^2 + x)
    >>> a3(4)
    44
    """
    return lambda x: f1(x) + f2(x)

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...
    
    And here's how we define it:
def skip_mul(n):
    if n == 0:
        return 0
    else:
        return n * skip_mul(n - 2)

What is wrong with this definition?
Choose the number of the correct choice:
0) The base case is flawed: it misses the case where n == 1
1) None of the above
2) The variable n does not change, causing a infinite loop
3) The recursive case should be skip_mul(n - 1)

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2  * 0
    0
    """
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return n * skip_mul(n - 2)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.
    def count_up(n):
    i = 1
    if i == n:
        return
    print(i)
    i += 1
    count_up(n-1)
    
    What's is wrong with this definition?
Choose the number of the correct choice:
0) The variable i resets back to 1 for each function call, printing 1 all the time
1) The return statement before the recursive call is missing
2) The recursive call should be count_up(n+1)
3) Should use return i instead of print(i)

    def count_up(n):
    i = 1
    if i > n:
        return
    else:
        print(i)
        i += 1
        count_up(n)

What is wrong with this definition?
Choose the number of the correct choice:
0) The variable n does not change, causing a infinite loop
1) Should use return i instead of print(i)
2) i is a local variable, which is not allowed in recursive functions
3) The return statement in the recursive case is missing
    """
    def counter(i):
        if i <= 1:
            return 1
        else:
            counter = 0
            while counter < i:
                return counter(i-1)
                # instead of i -= 1
    counter(1)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    # if max(a,b) % min(a,b) == 0:
    #     return min(a,b)
    # elif min(a,b) and max(a,b)%min(a.b)
    if max(a,b) % min(a,b) == 0:
        return min(a,b)
    # elif a > b and not(a % b == 0):
    else:
        return gcd(b, a%b)
