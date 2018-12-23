#############
# Iterators #
#############

# Q2
class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        "*** YOUR CODE HERE ***"
        self.start = start
        self.end = end
        self.current = start

    def __next__(self):
        "*** YOUR CODE HERE ***"
        if self.start > self.end:
            raise StopIteration
        self.current = self.start
        self.start += 1
        return self.current

    def __iter__(self):
        "*** YOUR CODE HERE ***"
        return IteratorRestart(self.start, self.end)

# Q4
class Str:
    """
    >>> s = Str("hello")
    >>> for char in s:
    ...     print(char)
    ...
    h
    e
    l
    l
    o
    >>> for char in s:    # a standard iterator does not restart
    ...     print(char)
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, word):
        self.word = word
        self.current = 0
        self.tracker = 0

    def __next__(self):
        if self.current >= len(self.word):
            raise StopIteration
        self.tracker = self.current
        self.current += 1
        return self.word[self.tracker]
    
    def __iter__(self):
        return self

##############
# Generators #
##############

# Q6
def countdown(n):
    """
    >>> from types import GeneratorType
    >>> type(countdown(0)) is GeneratorType # countdown is a generator
    True
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    while n >= 0:
        yield n
        n -= 1

class Countdown:
    """
    >>> from types import GeneratorType
    >>> type(Countdown(0)) is GeneratorType # Countdown is an iterator
    False
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, n):
        self.start = n
    def __iter__(self):
        while self.start >= 0:
            yield self.start
            self.start -= 1

# Q7
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    while n != 1:
        yield n # from start to the one before last 
        if n % 2 == 0:
            n //= 2
        else:
            n = (3*n) + 1
    yield n # only yields the very last val
