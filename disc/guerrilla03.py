
def combine_skipper(f, lst):
    """
    >>> lst = [4, 7, 3, 2, 1, 8, 5, 6]
    >>> f = lambda l: sum(l)
    >>> lst = combine_skipper(f, lst)
    >>> lst
    [11, 1, 3, 2, 9, 5, 5, 6]
    >>> lst2 = [4, 3, 2, 1]
    >>> lst2 = combine_skipper(f, lst2)
    >>> lst2
    [7, 1, 2, 1]
    """
    n, i= 0, 0
    while n < len(lst) // 4:
        lst[i] , lst[i + 1] = f(lst[i : i + 2]), i + 1
        n, i = n + 1, i + 4
    return lst


def rational(n, d):
    return [n, d]

def numer(r):
    return r[0]

def denom(r):
    return r[1]

def add_rational(x, y):
    return rational(numer(x) * denom(y) + numer(y) * denom(x), denom(x) * denom(y))

from math import pow
def rational_pow(x, e):
    """
    >>> r = rational_pow(rational(2, 3), 2)
    >>> numer(r)
    4
    >>> denom(r)
    9
    >>> r2 = rational_pow(rational(9, 72), 0)
    >>> numer(r2)
    1
    >>> denom(r2)
    1
    """
    return rational(int(pow(numer(x), e)), int(pow(denom(x), e)))

def inverse_rational(x):
    """ Returns the inverse of the given non-zero rational number
    >>> r = rational(2, 3)
    >>> r_inv = inverse_rational(r)
    >>> numer(r_inv)
    3
    >>> denom(r_inv)
    2
    >>> r2 = rational_pow(rational(3, 4), 2)
    >>> r2_inv = inverse_rational(r2)
    >>> numer(r2_inv)
    16
    >>> denom(r2_inv)
    9
    """
    return rational(denom(x), numer(x))

def div_rationals(x, y): # Hint: Use functions defined in Question 2
    """ Returns x / y for given rational x and non-zero rational y
    >>> r1 = rational(2, 3)
    >>> r2 = rational(3, 2)
    >>> div_rationals(r1, r2)
    [4, 9]
    >>> div_rationals(r1, r1)
    [6, 6]
    """
    y_div = inverse_rational(y)
    return rational(numer(x) * numer(y_div), denom(x) * denom(y_div))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def approx_e(iter):
    e = rational(0, 1)
    for i in range(iter):
        e = add_rational(e, rational(1, factorial(i)))
    return e

#Tree
from tree_def import *

def is_min_heap(t):
    for b in branches(t):
        if label(t) > label(b) or not is_min_heap(b):
            return False
    return True

def largest_product_path(tree):
    """
    >>> largest_product_path(None)
    0
    >>> largest_product_path(tree(3))
    3
    >>> t = tree(3, [tree(7, [tree(2)]), tree(8, [tree(1)]), tree(4)])
    >>> largest_product_path(t)
    42
    """
    if not is_tree(tree):
        return 0
    elif is_leaf(tree):
        return label(tree)
    else:
        paths = [label(tree) * largest_product_path(b) for b in branches(tree)]
        return max(paths)

def level_order(tree):
    """
    >>> t = tree(3, [tree(7, [tree(2, [tree(8), tree(1)]), tree(5)])])
    >>> level_order(t)
    [3 7 2 5 8 1]
    >>> level_order(tree(3))
    [3]
    >>> level_order(None)
    []
    """
    if not is_tree(tree):
        return []
    current_level, next_level = [label(tree)], [tree]
    while next_level:
        find_next = []
        for b in next_level:
            find_next.extend(branches(b))
        next_level = find_next
        current_level.extend([label(t) for t in next_level])
    return current_level

