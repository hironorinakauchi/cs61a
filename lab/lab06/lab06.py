## Lab 6: OOP and Nonlocal ##

# Question 1
def vending_machine(snacks):
    """Cycles through list of snacks.
    
    >>> vender = vending_machine(['chips', 'chocolate', 'popcorn'])
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(['brownie'])
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    count = 0
    def get_snack():
        nonlocal count
        snack = snacks[count]
        count += 1
        if count == len(snacks):
            count = 0
        return snack
    return get_snack