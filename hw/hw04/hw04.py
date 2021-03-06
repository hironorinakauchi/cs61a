###########
# Objects #
###########

# Q1

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, snacks, price):
    	self.balance = 0
    	self.snacks = snacks
    	self.price = price
    	self.amt_snacks = 0
		    
    def deposit(self, amt):
    	self.amount = amt
    	if self.amt_snacks == 0:
    		return 'Machine is out of stock. Here is your $%d.' % self.amount
    	else:
    		self.balance += self.amount
    		return 'Current balance: $%d' % self.balance

    def restock(self, amt_snacks):
    	self.amt_snacks += amt_snacks
    	return 'Current {} stock: {}'.format(self.snacks, self.amt_snacks)

    def vend(self):
    	if self.amt_snacks == 0:
    		if self.balance > 0:
    			return "Machine is out of stock. Here is your $%d." % self.balance
    		else:
 		   		return "Machine is out of stock."
    	else:
    		if self.balance < self.price:
    			return 'You must deposit ${} more.'.format(self.price - self.balance)
    		else:
    			pre_balance = self.balance
    			self.balance = 0
    			if pre_balance - self.price != 0:
    				self.amt_snacks -= 1
    				return 'Here is your {} and ${} change.'.format(self.snacks, pre_balance - self.price)
    			else:
    				self.amt_snacks -= 1
    				return 'Here is your %s.' % self.snacks

# Q2
class interval:
    """A range of floating-point values.

    >>> a = interval(1, 4)
    >>> a
    interval(1, 4)
    >>> print(a)
    (1, 4)
    >>> a.low
    1
    >>> a.high
    4
    >>> a.low = 3    # .low and .high are read-only
    AttributeError
    >>> a.width
    3
    >>> a.width = 4
    AttributeError
    >>> b = interval(2, -2)  # Order doesn't matter
    >>> print(b, b.low, b.high)
    (-2, 2) -2 2
    >>> a + b
    interval(-1, 6)
    >>> a - b
    interval(-1, 6)
    >>> a * b
    interval(-8, 8)
    >>> b / a
    interval(-2.0, 2.0)
    >>> a / b
    ValueError
    >>> -a
    interval(-4, -1)
    """
    def __init__(self, n1, n2):
    	self.lw = n1 if min(n1, n2) == n1 else n2
    	self.hg = n2 if max(n1, n2) == n2 else n1
    	# self._name = name

    def high(self):
    	return self.hg

    @property
    def high(self):
    	return self.hg

    def low(self):
    	return self.lw 

    @property
    def low(self):
    	return self.lw

    def width(self):
    	return self.hg - self.lw

    @property
    def width(self):
    	return self.hg - self.lw

    def __repr__(self):
    	return "interval("+str(self.lw)+", "+str(self.hg)+")"
    
    def __str__(self):
    	return "("+str(self.lw)+", "+str(self.hg)+")"

    def __add__(self, class2):
    	min_class = min(self.lw + class2.lw, self.lw + class2.hg, self.hg + class2.lw)
    	max_class = max(self.hg + class2.lw, self.hg + class2.hg, self.hg + class2.lw)
    	return interval(min_class, max_class)

    def __sub__(self, class2):
    	min_class = min(self.lw - class2.lw, self.lw - class2.hg, self.hg - class2.lw)
    	max_class = max(self.hg - class2.lw, self.hg - class2.hg, self.hg - class2.lw)
    	return interval(min_class, max_class)

    def __truediv__(self, class2):
    	if class2.high > 0 and class2.low < 0:
    		raise ValueError("ValueError") 
    	min_class = min(self.lw / class2.low, self.lw / class2.high, self.hg / class2.low, self.hg / self.hg)
    	max_class = max(self.lw / class2.low, self.lw / class2.high, self.hg / class2.low, self.hg / self.hg)
    	return interval(min_class, max_class)
    	# return "interval({0}{1}".format((__mul__(self), class2(1/class2.high, 1/class2.low)), k)
    def __mul__(self, class2):
    	min_class = min(self.lw * class2.lw, self.lw * class2.hg, self.hg * class2.lw)
    	max_class = max(self.hg * class2.lw, self.hg * class2.hg, self.hg * class2.lw)
    	return interval(min_class, max_class)
    
    def __neg__(self):
    	return interval(- self.hg, - self.lw)

   #whats the difference between using add func and __add__?   
# Q3

class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    def __init__(self, var):
    	self._vendor = var

    def ask(self, request, *args):
    	if "please" in request:
            function = request[7:]
            if hasattr(self._vendor, function):
            	return getattr(self._vendor, function)(*args)
            else:
            	return "Thanks for asking, but I know not how to " + function + "."
    	else:
        	return "You must learn to say please first."

# Q4, Q5, and Q6

class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    >>> len(s)
    3
    >>> s[2]
    3
    >>> s = Link.empty
    >>> len(s)
    0
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __len__(self):
        """ Return the number of items in the linked list.

        >>> s = Link(1, Link(2, Link(3)))
        >>> len(s)
        3
        >>> s = Link.empty
        >>> len(s)
        0
        >>> len(ints_list(100000)) # Check for iterative solution
        100000
        """
        k = 0
        s = self
        while s != Link.empty:
        # if it hits the pointer it adds 1 to k
        	s = s.rest
        	k += 1
        return k


    # The following method may be useful for implementation of the
    # __getitem__ and insert methods.
    def _get_link(self, i):
        """An internal utility method that returns the Ith Link after
        self (I == 0 returns self, I == 1 returns self.rest, etc.).  Returns
        empty if I is len(self).  Raises IndexError unless 0 <= I <= len(self).
        >>> L = Link(1, Link(2, Link(3)))
        >>> L._get_link(0)
        Link(1, Link(2, Link(3)))
        >>> L._get_link(1)
        Link(2, Link(3))
        >>> L._get_link(2)
        Link(3)
        >>> L._get_link(3)
        ()
        >>> L._get_link(4)
        Traceback (most recent call last):
           ...
        IndexError: list index out of range
        >>> L._get_link(-1)
        Traceback (most recent call last):
           ...
        IndexError: list index out of range
        >>> (ints_list(100000))._get_link(1).first
        2
        """
        if i < 0:
            raise IndexError("list index out of range")
        elif i == 0:
        	return len(self)
       	elif i == len(self):
       		return empty
        else: #elif i > len(self)
        	raise IndexError("list index out of range")
        	

    def __getitem__(self, i):
        """Returns the element found at index I.

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1]
        2
        >>> s[2]
        3
        >>> (ints_list(100000))[1]  # Check for iterative solution
        2
        """
        """
		link
			first[0]
			rest(empty or another link)
				first[1]
				rest
		i.g. t = link
		[0] = t.first
		[1] = t.rest.first
		[2] = t.rest.rest.first
        """
        if i < 0:
            i = len(self) + i
        k = 0
       	s = self
        while k < i:
        	s = s.rest
        	k += 1
        return s.first
        #     return self. (rest * i).first
        # if i == 0:
        # 	return self._get_link(self.first, i)
        # else:
        # 	rest = self.rest
        # 	while i > 0:
        # 		s2, i = s2.rest, i - 1 # what's the difference between _get_link(self,) and self.rest
        # 	return s2.firstz

    def __add__(self, lst):
        """Returns the result of non-destructively appending LST to the
        end of the sequence starting with self.
        """	
        k = 0
        s = self
        while s != Link.empty:
        	s = s.rest
        	k += 1
        return Link(self.first, Link(k, lst))


    def insert(self, k, val):
        """Destructively insert VAL into the list headed by SELF at index
        K, moving the previous item K and later items right.  Returns the
        resulting linked list.  Assumes 0 <= K <= len(self).
        """
        if k <= 0:
        	return self
        elif k > len(self):
        	raise IndexError
        elif k == len(self):
        	counter = 0
	        s = self
	        while counter <= k:
	        	s.rest = self.rest
	        	counter += 1
	       	s.rest = Link(val, self.rest)
	        return Link(self.first, s.rest)
        else:	
	        counter = 0
	        s = self
	        while counter <= k:
	        	s.rest = self.rest
	        	counter += 1
	       	s.rest = Link(val, self.rest)
	        return Link(self.first, s.rest)



# ints_list is used to test that a method does not use recursion by making
# sure that a very long list does not cause a large recursion depth.
def ints_list(k):
    """A linked list containing the numbers 1 to K."""
    if k < 1:
        return Link.empty
    p = result = Link(1)
    for i in range(2, k + 1):
        p.rest = Link(i)
        p = p.rest
    return result

def add(L0, L1):
    """Return the list formed by non-destructively appending the items in L1
    to the end of those in L0.

    >>> s = Link(1, Link(2))
    >>> s + Link.empty
    Link(1, Link(2))
    >>> s + Link(3, Link(4))
    Link(1, Link(2, Link(3, Link(4))))
    >>> s   # Non-destructive
    Link(1, Link(2))
    >>> add(Link.empty, s)
    Link(1, Link(2))
    >>> s = ints_list(100000) + Link(100001)  # Check for iterative solution
    """
    if L0 is Link.empty:
    	return L1
    else:
        return L0 + L1

def insert(L, k, val):
    """Destructively insert VAL into L at position K, returning the
    resulting list.  Assumes 0 <= K <= len(L).

    >>> L = Link(1, Link(2, Link(3)))
    >>> L.insert(1, 5)
    Link(1, Link(5, Link(2, Link(3))))
    >>> L
    Link(1, Link(5, Link(2, Link(3))))
    >>> L.insert(4, 6)  # Insert off the end.
    Link(1, Link(5, Link(2, Link(3, Link(6)))))
    >>> L.insert(0, 7)  # Insert at front
    Link(7, Link(1, Link(5, Link(2, Link(3, Link(6))))))
    >>> L  # New element is "left of" L
    Link(1, Link(5, Link(2, Link(3, Link(6)))))
    >>> L.insert(6, 8)
    IndexError
    >>> insert((), 0, 3)
    Link(3)
    """
    if L is Link.empty:
    	return Link(val)
    else:
         return L.insert(k, val)

class Tree:
    def __init__(self, label, children=()):
        self.label = label
        for branch in children:
            assert isinstance(branch, Tree)
        self.children = list(children)

    def __repr__(self):
        if self.children:
            children_str = ', ' + repr(self.children)
        else:
            children_str = ''
        return 'Tree({0}{1})'.format(self.label, children_str)

    def is_leaf(self):
        return not self.children

# Q7

def same_shape(t1, t2):
    """Returns whether two Trees t1, t2 have the same shape. Two trees have the
    same shape iff they have the same number of children and each pair
    of corresponding children have the same shape.

    >>> t, s = Tree(1), Tree(3)
    >>> same_shape(t, t)
    True
    >>> same_shape(t, s)
    True
    >>> t = Tree(1, [Tree(2), Tree(3)])
    >>> same_shape(t, s)
    False
    >>> s = Tree(4, [Tree(7)])
    >>> same_shape(t, s)
    False
    """
    if len(t1.children) != len(t2.children):
    	return False
    for c1, c2 in zip(t1.children, t2.children):
    	if not same_shape(c1, c2): # once we find the one that doesn't work, we can immmediately return false
    		return False
    return True
    # return len(Tree.__repr__(t1)) == len(Tree.__repr__(t2))

# Q8

def long_paths(tree, n):
    """Return a list all paths in tree with length at least n.

    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12)])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    Link(0, Link(1, Link(2)))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(5))))
    Link(0, Link(6, Link(7, Link(8))))
    Link(0, Link(6, Link(9)))
    Link(0, Link(11, Link(12)))
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(5))))
    Link(0, Link(6, Link(7, Link(8))))
    >>> long_paths(whole, 4)
    []
    """
    if tree.is_leaf():
    	if n > 0:
    		return []
    	if n <= 0:
    		return [Link(tree.label)]
    else:
    	list_of_children = []
    	for child in tree.children:
    		list_of_children += long_paths(child, n - 1)
    	final_list = []
    	for child in list_of_children:
    		final_list.append(Link(tree.label, child))
    return final_list

