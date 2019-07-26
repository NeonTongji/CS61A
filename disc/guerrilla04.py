
def make_max_finder():
    """
    >>> m = make_max_finder()
    >>> m([5, 6, 7])
    7
    >>> m([1, 2, 3])
    7
    >>> m([9])
    9
    >>> m2 = make_max_finder()
    >>> m2([1])
    1
    """
    max_num = 0
    def max_finder(lst):
        nonlocal max_num
        if max(lst) > max_num:
            max_num = max(lst)
        return max_num
    return max_finder

from lnk_tree_class_def import *

def filter_tree(t, fn):
    """
    >>> t = Tree(1, [Tree(2), Tree(3, [Tree(4)]), Tree(6, [Tree(7)])])
    >>> filter_tree(t, lambda x: x % 2 != 0)
    >>> t
    tree(1, [Tree(3)])
    >>> t2 = Tree(2, [Tree(3), Tree(4), Tree(5)])
    >>> filter_tree(t2, lambda x: x != 2)
    >>> t2
    Tree(2)
    """
    if not fn(t.label):
        t.branches = []
    else:
        for b in t.branches[:]:
            if not fn(b.label):
                t.branches.remove(b)
            else:
                filter_tree(b, fn)

def nth_level_tree_map(fn, tree, n):
    """Mutates a tree by mapping a function all the elements of a tree.
    >>> tree = Tree(1, [Tree(7, [Tree(3), Tree(4), Tree(5)]), Tree(2, [Tree(6), Tree(4)])])
    >>> nth_level_tree_map(lambda x: x + 1, tree, 2)
    >>> tree
    Tree(2, [Tree(7, [Tree(4), Tree(5), Tree(6)]), Tree(2, [Tree(7), Tree(5)])])
    """
    def tree_map_helper(tree, level):
        if level % n == 0:
            tree.label = fn(tree.label)
        if not tree.is_leaf():
            for b in tree.branches:
                tree_map_helper(b, level + 1)
    tree_map_helper(tree, 0)

class Plant:
    is_zombie = False
    def __init__(self):
        """A Plant has a Leaf, a list of sugars created so far,
        and an initial height of 1"""
        self.height = 1
        self.leaves = [Leaf(self)]
        self.materials = []
        self.age = 0

    def absorb(self):
        """Calls the leaf to create sugar"""
        for leaf in self.leaves:
            leaf.absorb()
            leaf.age += 1
            if leaf.age >= 2:
                leaf.death()
        if not self.is_zombie:
            self.age += 1
            if self.age >= 20:
                self.death()

    def grow(self):
        """A Plant uses all of its sugars, each of which increases
        its height by 1"""
        for sugar in self.materials[:]:
            sugar.activate()
            self.height += 1
            sugar.leaf.sugar_used += 1
        for leaf in self.leaves[:]:
            leaf.age += 1
            if leaf.age >= 2:
                leaf.death()
        if not self.is_zombie:
            self.age += 1
            if self.age >= 20:
                self.death()

    def death(self):
        self.is_zombie = True
        for leaf in self.leaves[:]:
            leaf.death()


class Leaf:
    def __init__(self, plant): # Source is a Plant instance
        """A Leaf is initially alive, and keeps track of how many
        sugars it has created"""
        self.plant = plant
        self.alive = True
        self.sugar_used = 0
        self.age = 0

    def absorb(self):
        """If this Leaf is alive, a Sugar is added to the plant’s
        list of sugars"""
        if self.alive:
            self.plant.materials.append(Sugar(self, self.plant))
    
    def death(self):
        self.plant.leaves.remove(self)
        self.plant.leaves.append(Leaf(self.plant))
        if self.plant.is_zombie:
            self.plant.leaves.append(Leaf(self.plant))

    def __repr__(self):
        return '|Leaf|'

            
class Sugar:
    sugars_created = 0
    def __init__(self, leaf, plant):
        self.leaf = leaf
        self.plant = plant
        Sugar.sugars_created += 1
    
    def activate(self):
        """A sugar is used, then removed from the Plant which
        contains it"""
        self.plant.materials.remove(self)
    
    def __repr__(self):
        return '|Sugar|'

      
def seq_in_link(link, sub_link):
    """
    >>> lnk1 = Link(1, Link(2, Link(3, Link(4))))
    >>> lnk2 = Link(1, Link(3))
    >>> lnk3 = Link(4, Link(3, Link(2, Link(1))))
    >>> seq_in_link(lnk1, lnk2)
    True
    >>> seq_in_link(lnk1, lnk3)
    False
    """
    if sub_link is Link.empty:
        return True
    if link is Link.empty:
        return False
    if link.first == sub_link.first:
        return seq_in_link(link.rest, sub_link.rest)
    else:
        return seq_in_link(link.rest, sub_link)

def gen_inf(lst):
    """
    >>> t = gen_inf([3, 4, 5])
    >>> next(t)
    3
    >>> next(t)
    4
    >>> next(t)
    5
    >>> next(t)
    3
    >>> next(t)
    4
    """
    while True:
        for i in lst:
            yield i

def is_iter(item):
    try:
        it = iter(item)
    except TypeError:
        return False
    else:
        return True

def nested_gen(lst):
    """
    >>> a = [1, 2, 3]
    >>> def g(lst):
    >>>     for i in lst:
    >>>         yield i
    >>> b = g([10, 11, 12])
    >>> c = g([b])
    >>> lst = [a, c, [[[2]]]]
    >>> list(nested_gen(lst))
    [1, 2, 3, 10, 11, 12, 2]
    """
    for i in lst:
        if is_iter(i):
            yield from nested_gen(i)
        else:
            yield i

def mutated_gen(lst):
    """
    >>> lst = [1, 2, 3, 4, 5]
    >>> gen = mutated_gen(lst)
    >>> lst[1] = 7
    >>> next(gen)
    7
    >>> lst[0] = 5
    >>> lst[2] = 3
    >>> lst[3] = 9
    >>> lst[4] = 2
    >>> next(gen)
    9
    >>> lst.append(6)
    >>> next(gen)
    StopIteration Exception
    """
    origin_lst = lst[:]
    def gen(origin, lst):
        curr = 0
        while curr < len(lst):
            if len(lst) != len(origin):
                break
            else:
                if lst[curr] != origin[curr]:
                    yield lst[curr]
            curr += 1
    return gen(origin_lst, lst)
