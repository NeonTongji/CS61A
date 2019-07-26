from BTree_def import *

class GrootTree(BTree):
    """A binary tree with a parent."""
    def __init__(self, label, left = BTree.empty, right = BTree.empty):
        BTree.__init__(self, label, left, right)
        self.parent = BTree.empty
        if left != BTree.empty:
            self.left.parent = self
        if right != BTree.empty:
            self.right.parent = self

def fib_groot(n):
    if n == 0 or n == 1:
        return GrootTree(n)
    else:
        left, right = fib_groot(n - 2), fib_groot(n - 1)
        return GrootTree(left.label + right.label, left, right)

def paths(g, s):
    """The number of paths through g with label s
    >>> t = fib_groot(3)
    >>> paths(t, [1])
    0
    >>> paths(t, [2])
    1
    >>> paths(t, [2, 1, 2, 1, 0])
    2
    >>> paths(t, [2, 1, 0, 1, 0])
    1
    >>> paths(t, [2, 1, 2, 1, 2, 1])
    8
    """
    if g is BTree.empty or g.label != s[0]:
        return 0
    elif len(s) == 1:
        return 1
    else:
        xs = [g.left, g.right, g.parent]
        return sum([paths(x, s[1:]) for x in xs])

from lnk_tree_class_def import *

def double_up(s):
    """Mutate s by inserting elements so that each element is next to an equal.
    >>> s = Link(3, Link(4))
    >>> double up(s)
    2   # return the number of insertion
    >>>s
    Link(3, Link(3, Link(4, Link(4))))
    """
    if s is Link.empty:
        return 0
    elif s.rest is Link.empty:
        s.rest = Link(s.first)
        return 1
    elif s.first == s.rest.first:
        return double_up(s.rest.rest)
    else:
        s.rest = Link(s.first, s.rest)
        return 1 + double_up(s.rest.rest)


