
def mario_number(level):
    """
    Return the number of ways that Mario can traverse the level,
    where Mario can either hop by one digit or two digits each turn.
    A level is defined as being an integer with digits where a 1 is
    something Mario can step on and 0 is something Mario cannot step
    on.
    >>> mario_number(10101) # Hops each turn: (1, 2, 2)
    1
    >>> mario_number(11101) # Hops each turn: (1, 1, 1, 2), (2, 1, 2)
    2
    >>> mario_number(100101)# No way to traverse through level
    0
    """
    if level == 1:
        return 1
    elif level % 10 == 0:
        return 0
    else:
        return mario_number(level // 10) + mario_number(level // 100)
