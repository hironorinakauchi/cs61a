## Sets + Orders of Growth ##

# Q2
def find_duplicates(lst):
    """Returns True if lst has any duplicates and False if it does not.

    >>> find_duplicates([1, 2, 3, 4, 5])
    False
    >>> find_duplicates([1, 2, 3, 4, 2])
    True
    >>> find_duplicates(list(range(100000)) + [-1]) # make sure you have linear time
    False
    """
    "*** YOUR CODE HERE ***"
    set_lst = set(lst)
    if list(set_lst) != lst:
        return True
    else:
        return False

# Q3
def pow(n,k):
    """Computes n^k.

    >>> pow(2, 3)
    8
    >>> pow(4, 2)
    16
    >>> a = pow(2, 100000000) # make sure you have log time
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    elif k == 1:
        return n
    elif k % 2 == 1:
        return n * pow(n, k - 1)
    else:
        pow2 = pow(n, k / 2)
        return pow2**2




