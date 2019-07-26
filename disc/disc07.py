from lnk_tree_class_def import *

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest
    ()
    """
    def mul_list(lst):
        result = 1
        for i in lst:
            result *= i
        return result

    m_lnk = Link(mul_list([lnk.first for lnk in lst_of_lnks]))
    cursor = m_lnk
    while all([lnk.rest != Link.empty for lnk in lst_of_lnks]):
        index = 0
        for lnk in lst_of_lnks[:]:
            lst_of_lnks[index] = lnk.rest
            index += 1
        cursor.rest = Link(mul_list([lnk.first for lnk in lst_of_lnks]))
        cursor = cursor.rest
    return m_lnk

def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(5))
    """
    while lnk != Link.empty:
        while lnk.rest != Link.empty and lnk.first == lnk.rest.first:
            lnk.rest = lnk.rest.rest
        lnk = lnk.rest

def even_weighted(lst):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i * lst[i] for i in range(len(lst)) if i % 2 == 0]

def quicksort_list(lst):
    """
    >>> quicksort_list([3, 1, 4])
    [1, 3, 4]
    """
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    less = [ i for i in lst if i < pivot]
    greater = [i for i in lst if i > pivot]
    return quicksort_list(less) + [pivot] + quicksort_list(greater)

def max_product(lst):
    """Return the maximum product that can be formed using lst
    without using any consecutive numbers
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if not lst:
        return 1
    elif len(lst) == 1:
        return lst[0]
    return max(lst[0] * max_product(lst[2:]), max_product(lst[1:]))


def redundant_map(t, f):
    """
    >>> double = lambda x: x*2
    >>> tree = Tree(1, [Tree(1), Tree(2, [Tree(1, [Tree(1)])])])
    >>> redundant_map(tree, double)
    >>> print_levels(tree)
    [2] # 1 * 2 ˆ (1) ; Apply double one time
    [4, 8] # 1 * 2 ˆ (2), 2 * 2 ˆ (2) ; Apply double two times
    [16] # 1 * 2 ˆ (2 ˆ 2) ; Apply double four times
    [256] # 1 * 2 ˆ (2 ˆ 3) ; Apply double eight times
    """
    t.label = f(t.label)
    new_f = lambda x: f(f(x))
    for b in t.branches:
        redundant_map(b, new_f)

