
curry2 = lambda h: lambda x: lambda y: h(x, y)

w = "h"
h = w
def y(z):
    a = "h"
    if z == 'h':
        return z + "i"
    z = lambda f: f(a)
    return lambda g: z(g)


def keep_ints(cond, n):
    """Print out all intergers 1..i..n where cond(i) is true"""
    for i in range(n):
        if cond(i + 1):
            print(i + 1)


def keep_ints(n):
    """Print out all intergers 1..i..n where cond(i) is true"""
    def f(cond):
        for i in range(n):
            if cond(i + 1):
                print(i + 1)
    return f

def multiply(m,n):
    """multiply using recursion whithout * or mul"""
    if m == 1 and n == 1:
        return 1
    elif m > 1:
        return multiply(m - 1, n) + n
    else:
        return n

def countdown(n):
    if n == 1:
        print(1)
    else:
        print(n)
        return countdown(n - 1)

def countup(n):
    def count(n, k):
        if n >= 1:
            print(k)
            return count(n - 1,k + 1)
    return count(n, 1)

def sum_every_other_digit(n):
    if n < 10:
        return n
    else:
        n, last = n // 100, n % 10 
        return sum_every_other_digit(n) + last

def rec(x, y):
    """return x^y"""
    if y > 0:
        return x * rec(x, y - 1)
    return 1

