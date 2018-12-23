def your_course_username():
    """Return your course username. 

    >>> username = your_course_username()
    >>> username.startswith('cs61a-')
    True
    """
    return "cs61a-agf"

from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return abs(a**2+b**2+c**2)-pow(min(a,b,c),2)
    #return (max(a,b,c)**2) + (max(min(a,b), min(a,c), min(b,c))**2)

def largest_factor(n):
    """Return the largest factor of n*n-1 that is smaller than n.

    >>> largest_factor(4) # n*n-1 is 15; factors are 1, 3, 5, 15
    3
    >>> largest_factor(9) # n*n-1 is 80; factors are 1, 2, 4, 5, 8, 10, ...
    8
    """

    x = n*n-1
    for i in range(1, x+1):
        if x % i == 0:
            if i < n:
               factor = i
    return factor

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return 1 == 1

def t():
    return 1

def f():
    return 1 / 0

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    step = 1
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n//2
            step += 1
            print(n)
        elif n % 2 != 0:
            n = (3*n)+1
            step += 1
            print(n)
    return step

challenge_question_program = """
"ILOVECS = "ILOVEEECS = chr(73) + chr(76) + chr(79) + chr(86) + chr(69) + chr(67) + chr(83) + chr(32) + chr(61) + chr(32) + chr(34); ILOVEEECS += ILOVECS; print(repr("ILOVEEECS = chr(73) + chr(76) + chr(79) + chr(86) + chr(69) + chr(67) + chr(83) + chr(32) + chr(61) + chr(32) + chr(34); ILOVEEECS += ILOVECS; print(ILOVEEECS) + chr(34); print(ILOVECS)")) + chr(34); print(ILOVECS)";ILOVEEECS = chr(73) + chr(76) + chr(79) + chr(86) + chr(69) + chr(67) + chr(83) + chr(32) + chr(61) + chr(32) + chr(34); ILOVEEECS += ILOVECS; print(ILOVEEECS + chr(34));print(repr("ILOVEEECS = chr(73) + chr(76) + chr(79) + chr(86) + chr(69) + chr(67) + chr(83) + chr(32) + chr(61) + chr(32) + chr(34); ILOVEEECS += ILOVECS; print(ILOVEEECS) + chr(34); print(ILOVECS)"))
"

"""


# c = [(x) for x in [67,83,61,65] if x > 61];print(list(map(chr,c))) 
# c = [(x) for x in [67,83,61,65] if x > 61];print(list(map(chr,c)));
# print(list(map(chr, c = [(x) for x in [67, 83, 61, 65] if x > 61])))
# doesnt work since map() doesnt take keyword arguments
# c = [(x) for x in [67, 83, 61, 65]] if (list(map(chr, c)))[0] == eval(repr(c))
# ILOVECS = "ILOVEEECS = chr(73) + chr(76) + chr(79) + chr(86) + chr(69) + chr(67) + chr(83) + chr(32) + chr(61) + chr(32) + chr(34)"
# ILOVEEECS = chr(73) + chr(76) + chr(79) + chr(86) + chr(69) + chr(67) + chr(83) + chr(32) + chr(61) + chr(32) + chr(34); ILOVEEECS += ILOVECS; print(ILOVEEECS)
# which returns 