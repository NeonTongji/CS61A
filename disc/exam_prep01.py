
def longest_increasing_suffix(n):
    m, suffix, k = 1, 0, 1
    while n:
        n, last = n // 10, n % 10
        if m > 0:
            m, suffix, k = m * (last - (n % 10)), suffix + last * k, 10 * k
        else:
            return suffix
    return suffix

def sandwich(n):
    tens, ones = n // 10 % 10, n % 10
    n = n // 100
    while n:
        if n % 10 == ones:
            return True
        else:
            tens, ones = n % 10, tens
            n = n // 10
    return False

def luhn_sum(n):
    def luhn_digit(digit):
        x = digit * multiplier
        return x // 10 + x % 10
    total, multiplier = 0, 1
    while n:
        n, last = n // 10, n % 10
        total += luhn_digit(last)
        multiplier = 3 - multiplier
    return total
