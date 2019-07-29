
def is_prime(n):
    """Return whether the number is prime ,using recursion
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    i = 2
    def prime_helper(n, i):
        if n // i <= i:
            return True
        elif n == 1 or n % i == 0:
            return True
        else:
            return prime_helper(n , i + 1)
    return prime_helper(n, i)

def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(n):
        if n == 1:
            return f(x)
        else:
            return f(repeat(n - 1))
    return repeat

def count_stair_ways(n):
    """ Count ways to go up a flight of stairs(n steps) by taking 1 or 2 steps each time"""
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def count_k(n, k):
    """ Count_stair_ways by taking up to k step
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1)
    1
    """
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return 0
    else:
        i = 1
        count = 0
        while i <= k:
            count += count_k(n - i, k)
            i += 1
        return count

    
def pascal(row, column):
    if column == 0:
        return 1
    elif row < column:
        return 0
    elif row == column:
        return 1
    return pascal(row - 1, column - 1) + pascal(row - 1, column)

