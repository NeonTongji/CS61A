from lnk_tree_class_def import *

def eval_with_add(t):
    """Evaluate an expression tree of * and + using only addition.
    >>> plus = Tree('+', [Tree(2), Tree(3)])
    >>> eval_with_add(plus)
    5
    >>> times = Tree('*', [Tree(2), Tree(3)])
    >>> eval_with_add(times)
    6
    >>> deep = Tree('*', [Tree(2), plus, times])
    >>> eval_with_add(deep)
    60
    >>> eval_with_add(Tree('*'))
    1
    """
    if t.label == '+':
        return sum([eval_with_add(b) for b in t.branches])
    elif t.label == '*':
        total = 1
        for b in t.branches:
            total, term = 0, total
            for _ in range(eval_with_add(b)):
                total = total + term
        return total
    else:
        return t.label
