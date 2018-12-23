from utils import *

# Q1
from math import sqrt
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    return sqrt((get_lat(city1) - get_lat(city2))**2 + (get_lon(city1) - get_lon(city2))**2)
# Q2
def closer_city(lat, lon, city1, city2):
    """ Returns the name of either city1 or city2, whichever is closest
        to coordinate (lat, lon).

        >>> berkeley = make_city('Berkeley', 37.87, 112.26)
        >>> stanford = make_city('Stanford', 34.05, 118.25)
        >>> closer_city(38.33, 121.44, berkeley, stanford)
        'Stanford'
        >>> bucharest = make_city('Bucharest', 44.43, 26.10)
        >>> vienna = make_city('Vienna', 48.20, 16.37)
        >>> closer_city(41.29, 174.78, bucharest, vienna)
        'Bucharest'
    """
    # lon should be closer to your location (smaller difference)
    if abs(lon - get_lon(city1)) < abs(lon - get_lon(city2)):
        if get_lat(city1) < get_lat(city2):
            return get_name(city1)
    else:
        return get_name(city2)



# Q3
def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    # def multiply(a, b):
    #     if b == 0:
    #         return 0
    #     else:
    #         return multiply(a, b) + a

    if b == 0:
        return c
    else:
        return ab_plus_c(a, b-1, c) + a 

# if b == 0:
#         return a + c
#     else:
#         return ab_plus_c(a, b-1, c) + a 

# def multiply(a, b):
#     if b == 0:
#         return 0
#     else:
#         return multiply(a, b) + a
        

# Q4
def is_prime(n):
    """Returns True if n is a prime number and False otherwise. 

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def detector(m):
        if m >= n:
            return True
        elif n % m == 0:
            return False
        return detector(m+1)
    return detector(2)
    # if n < 1:
    #     return True
    # elif n%10 in [2,3,5,7]:
    #     return is_prime(n//10)
    # else:
    #     return False

    # if n <= 1:
    #     return False
    # else:
    #     num = n // is_prime(n+1)
    #     if num == 0:
    #         return False
    #     else:
    #         return True
    # since prime #s is only divisible by 1 and itslef, I'm going to...
    # divide #s from 2 to n-1 to see if its divisible or not
    # if helper says finds n to be divisible by any # other than n and itself, 
    # it'll return False (meaning there's a factor somewhere in between besides 1 and n itself)
    # if it goes all the way down to 1, (meaning helper can't find any factor besides 1 and n itself)
    # it'll return True! 


    # def divisible_or_not(number1):
    #     number2 = 2

    #     if number1 == number2:
    #         return True
    #     elif number1 % number2 == 0:
    #         return False
    #     else: # if number1 is not divisible by number2
    #         number2 += 1
    #         return divisible_or_not(number1)

    # if n < 1:
    #     return False
    # else:
    #     if divisible_or_not(n):
    #         return True
    #     else:
    #         return False


# Q5
def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    total = 0
    def even_or_odd(n):
        total = 0
        if n % 2 ==0:
            total = total + even_term(n)
            return total
        else:
            total = total + odd_term(n)
            return total

    if n == 0:
        return 0
    elif n % 2 == 0:
        # total = total + even_term(n)
        return even_or_odd(n-1)
    else:
        # total = total + odd_term(n)
        return even_or_odd(n-1)

