## Recursive Objects ##

# Q2
def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.

    >>> link = list_to_link([1, 2, 3])
    >>> print_link(link)
    <1 2 3>
    """
    if len(lst) == 0:
        return Link.empty
    else:
        return Link(lst[0], list_to_link(lst[1:]))  

# Q3
def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print_link(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print_link(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print_link(l1)
    <0 1>
    """
    def link_list(link):
        if link == Link.empty:
            return []
        else:
            return [link.first] + link_list(link.rest)

    linked_list1 = link_list(link)
    modified_list = list(filter(lambda el: el != value, linked_list1))
    linked_list2 = list_to_link(modified_list)
    link.first = linked_list2.first
    link.rest = linked_list2.rest

# Linked List Class
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
        """
        return 1 + len(self.rest)

    def __getitem__(self, i):
        """Returning the element found at index i.

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1]
        2
        >>> s[2]
        3
        """
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

def print_link(link):
    """Print elements of a linked list link.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' + helper(link).rstrip() + '>')

def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' + helper(link.first).rstrip() + '> ' + helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)

# Tree Class
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
