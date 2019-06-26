from tree_def import *

def complete(t, d, k):
    if not branches(t):
        return d == 0
    bs = [complete(b, d - 1, k) for b in branches(t)]
    return len(branches(t)) == k and all(bs)

def closest(t):
    diff = abs(label(t) - sum([label(b) for b in branches(t)]))
    return min([diff] + [closest(b) for b in branches(t)])

def is_path(t, path):
    """Return whether a given path exists in a tree, beginning
    at the root.
    >>> t = tree(1, [
        tree(2, [tree(4), tree(5)]),
        tree(3, [tree(6), tree(7)])
        ])
    >>> is_path(t, [1, 2])
    True
    >>> is_path(t, [1, 2, 4])
    True
    >>> is_path(t, [2, 4])
    False
    """
    if label(t) != path[0]:
        return False
    if label(t) == path[0] and len(path) == 1:
        return True
    return any([is_path(b, path[1:]) for b in branches(t)])
