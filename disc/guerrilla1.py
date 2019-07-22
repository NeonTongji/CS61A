
def count_digits(n):
    digit = 1
    while n // 10 > 0:
        digit +=1
        n = n // 10
    return digit

def count_matches(n, m):
    matches = 0
    while n > 0 and m > 0:
        if n % 10 == m % 10:
            matches += 1
        n, m = n // 10, m // 10
    return matches
