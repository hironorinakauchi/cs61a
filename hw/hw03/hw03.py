##############################################################
# An alternative implementation of the tree data abstraction #
##############################################################

def tree(label, children=[]):
    for branch in children:
        assert is_tree(branch), 'children must be trees'
    return (label, children)

def label(tree):
    return tree[0]

def children(tree):
    return tree[1]

def is_tree(tree):
    if type(tree) is not tuple or len(tree) != 2 \
           or (type(tree[1]) is not list and type(tree[1]) is not tuple):
        return False
    for branch in children(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not children(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the label.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for child in children(t):
        print_tree(child, indent + 1)

# Linked List definition
empty = 'empty'


def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))


def link(first, rest=empty):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]


def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]


def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]


def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)

#############
# Sequences #
#############

def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    if lst == []:
        return []
    elif type(lst[0]) == list:
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return [lst[0]] + flatten(lst[1:])

def interleave(s0, s1):
    """Interleave linked lists s0 and s1 to produce a new linked
    list.

    >>> evens = link(2, link(4, link(6, link(8, empty))))
    >>> odds = link(1, link(3, empty))
    >>> print_link(interleave(odds, evens))
    1 2 3 4 6 8
    >>> print_link(interleave(evens, odds))
    2 1 4 3 6 8
    >>> print_link(interleave(odds, odds))
    1 1 3 3
    """
    if s0 is empty:
        return s1
    if s1 is empty:
        return s0
    return link(first(s0), link(first(s1), interleave(rest(s0), rest(s1))))


###########
# Merging #
###########

def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    if lst1 == []:
        return lst2
    if lst2 == []:
        return lst1
    else:
        if lst1[0] > lst2[0]:
            return [lst2[0]] + merge(lst1, lst2[1:])
        else:
            return [lst1[0]] + merge(lst1[1:], lst2)
    """
    else:
    

    """

def mergesort(seq):
    """Mergesort algorithm.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """
    sorted_list = []
    k = 0
    while seq:
        min_value = seq[0]
        for i in seq:
            if i < min_value:
                min_value = i
        sorted_list.append(min_value)
        seq.remove(min_value)
        k += 1
    return sorted_list

###########
# Mobiles #
###########

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree(None, [left, right])

def sides(m):
    """Select the sides of a mobile."""
    return children(m)

def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])

def length(s):
    """Select the length of a side."""
    return label(s)

def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    return children(s)[0]

def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    return tree(size)

def size(w):
    """Select the size of a weight."""
    return label(w)

def is_weight(w):
    """Whether w is a weight, not a mobile."""
    if is_leaf(w):
        return True
    else:
        return False

def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        return sum([total_weight(end(s)) for s in sides(m)])

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    if is_weight(m):
        return True
    else:
        leftSide = label(sides(m))
        rightSide = children(sides(m))
        left=length(leftSide)*total_weight(end(leftSide))
        right=length(rightSide)*total_weight(end(rightSide))
        return left == right and balanced(end(leftSide)) and balanced(end(rightSide))
###########
# Exprs   #
###########

import re

OPERATORS = ('*', '+', '-')

# Alternative names of parts of an expression tree.

def left_opnd(expr):
    return children(expr)[0]

def right_opnd(expr):
    return children(expr)[1]

def oper(expr):
    return label(expr)

# Useful constants:

ZERO = tree('0')
ONE = tree('1')

def same_expr(expr0, expr1):
    """Return true iff expression trees EXPR0 and EXPR1 are identical."""
    if oper(expr0) != oper(expr1):
        return False
    elif is_leaf(expr0):
        return True
    else:
        return same_expr(left_opnd(expr0), left_opnd(expr1)) and \
               same_expr(right_opnd(expr0), right_opnd(expr1))
def postfix_to_expr(postfix_expr):
    """Return an expression tree equivalent to POSTFIX_EXPR, a string
    in postfix ("reverse Polish") notation.  In postfix, one writes
    E1 OP E2 (where E1 and E2 are expressions and OP is an operator) as
    E1' E2' OP, where E1' and E2' are the postfix versions of E1 and E2. For
    example, '2*(3+x)' is written '2 3 x + *' and '2*3+x' is `2 3 * x +'.
    >>> print_tree(postfix_to_expr("2 3 x + *"))
    *
      2
      +
        3
        x
    """

    E = re.split(r'\s+', postfix_expr.strip())
    def expr():
        """Removes and returns an expression from the end of E.  Modifies
        the list E, which is a list of operands and operators taken from a
        postfix expression string."""
        op = E.pop()
        if op in OPERATORS:
            right = expr()
            left = expr()
            return tree(op, [left, right])
        else:
            return tree(op)
    return expr()

def expr_to_infix(expr):
    """A string containing a standard infix denotation of the expression
    tree EXPR"""
    if is_leaf(expr):
        return str(label(expr))
    else:
        return "({} {} {})".format(expr_to_infix(left_opnd(expr)), 
                                   label(expr),
                                   expr_to_infix(right_opnd(expr)))
    
def expr_to_postfix(expr):
    """The inverse of postfix_to_expr."""
    if is_leaf(expr):
        return str(oper(expr))
    else:
        return "{} {} {}".format(expr_to_postfix(left_opnd(expr)),
                                 expr_to_postfix(right_opnd(expr)),
                                 oper(expr))

def simplify(expr):
    """EXPR must be an expression tree involving the operators
    '+', '*', and '-' in inner nodes; numbers and strings (standing for
    variable names) in leaves.  Returns an equivalent, simplified version
    of EXPR.
    >>> def simp(postfix_expr):
    ...     return expr_to_infix(simplify(postfix_to_expr(postfix_expr)))
    >>> simp("x y + 0 *")
    '0'
    >>> simp("0 x y + *")
    '0'
    >>> simp("x y + 0 +")
    '(x + y)'
    >>> simp("0 x y + +")
    '(x + y)'
    >>> simp("x y + 1 *")
    '(x + y)'
    >>> simp("1 x y + *")
    '(x + y)'
    >>> simp("x y + x y + -")
    '0'
    >>> simp("x y y - + x - a b * *")
    '0'
    >>> simp("x y 3 * -")
    '(x - (y * 3))'
    >>> simp("x y 0 + 3 * -")
    '(x - (y * 3))'
    """
    """
    oper = will get lable
    leftopnd(expr)
    rightopnd(expr)
    simplify the children before comparing
    base case - leaf (not always be operator)
    leaf(1) = tree(1)
    same_expr()
    
    0 = tree(0)
    1 = tree(1)
    """
    if is_leaf(expr):
        return expr
    if oper(expr) == '*':
        if simplify(left_opnd(expr)) == ZERO:
            return ZERO
        if simplify(right_opnd(expr)) == ZERO:
            return ZERO
        if simplify(right_opnd(expr)) == ONE:
            return simplify(left_opnd(expr))
        if simplify(left_opnd(expr)) == ONE:
            return simplify(right_opnd(expr))    

    if oper(expr) == '+':
        if simplify(left_opnd(expr)) == ZERO:
            return simplify(right_opnd(expr))
        if simplify(right_opnd(expr)) == ZERO:
            return simplify(left_opnd(expr))

    if oper(expr) == '-':
        if same_expr(simplify(left_opnd(expr)), simplify(right_opnd(expr))):
            return ZERO
        if simplify(left_opnd(expr)) == ZERO:
            return simplify(right_opnd(-expr))
        if simplify(right_opnd(expr)) == ZERO:
            return simplify(left_opnd(expr))

    return tree(oper(expr), [simplify(left_opnd(expr)), simplify(right_opnd(expr))])


###########
# Extra   #
###########

def place_queens(size):
    """Return a list. p, of length SIZE in which p[r] is the column in
    which to place a queen in row r (0 <= r < SIZE) such that no two
    queens are attacking each other.  Return None if there is no such
    configuration.
    >>> place_queens(2) == None
    True
    >>> place_queens(3) == None
    True
    >>> check_board(4, place_queens(4))
    True
    >>> check_board(8, place_queens(8))
    True
    >>> check_board(14, place_queens(14))
    True
    """
    if check_board(, place_queens(size)):
        return None
    elif 
    else:
        return place_queens(size+1) or place_queens(size-1)


def check_board(n, cols):
    """Check that COLS is a valid solution to the N-queens problem
    (N == len(COLS)).  COLS has the format returned by place_queens."""
    if cols is None:
        return False
    if n != len(cols):
        return False
    if set(cols) != set(range(n)):
        return False
    if n != len(set([ r + c for r, c in enumerate(cols) ])):
        return False
    if n != len(set([ r - c for r, c in enumerate(cols) ])):
        return False
    return True

def print_board(cols):
    """Print a board, COLS, returned by place_queens (as a list of column
    positions of queens for each row)."""
    if cols is None:
        print("No solution")
    else:
        for c in cols:
            print("- " * c + "Q " + "- " * (len(cols) - c - 1))

"""Example:
> print_board(place_queens(5))
Q - - - - 
- - Q - - 
- - - - Q 
- Q - - - 
- - - Q - 
"""

        
        


        
