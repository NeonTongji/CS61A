from tree_def import *

def tree_max(t):
    """Return the maximum label in a tree.
    >>> t = tree(4, [tree(2, [tree(1)]), tree(10)])
    >>> tree_max(t)
    10
    """
    labels = [label(t)] + [label(b) for b in branches(t)]
    return max(labels)

def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    if all([is_leaf(b) for b in branches(t)]):
        return 1
    else:
        heights = [1 + height(b) for b in branches(t)]
        return max(heights)

def square_tree(t):
    """Return a tree with the square of every element in t"""
    square = lambda x: x * x 
    label_s = square(label(t))
    if is_leaf(t):
        return tree(label_s)
    else:
        return tree(label_s, [square_tree(b) for b in branches(t)])

def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if label(tree) == x:
        return [label(tree)]
    for b in branches(tree):
        path = find_path(b, x)
        if path:
            return [label(tree)] + path

def prune(t, k):
    """returns a new tree that contains only the first k levels of the original tree"""
    if k == 0:
        return tree(label(t))
    else:
        return tree(label(t), [prune(b, k - 1) for b in branches(t)])
    
def hailstone_tree(n, h):
    """Generates a tree of hailstone numbers that will
    reach N, with height H.
    >>> hailstone_tree(1, 0)
    [1]
    >>> hailstone_tree(1, 4)
    [1, [2, [4, [8, [16]]]]]
    >>> hailstone_tree(8, 3)
    [8, [16, [32, [64]], [5, [10]]]]
    """
    if h == 0:
        return tree(n)
    left = hailstone_tree(n * 2, h - 1)
    if ((n - 1) // 3) % 2 != 0 and (n - 1) % 3 == 0:
        right = hailstone_tree((n - 1) // 3, h - 1)
        return tree(n, [left, right])
    return tree(n, [left])

