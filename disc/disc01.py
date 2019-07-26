
def wear_jacket(temp, raining):
    """Wear jacket if it is below 60 degree or it is raining"""
    return temp > 60 or raining

def  is_prime(n):
    if n == 1:
        return False
    i = 2
    while i <= n // i:
        if n % i == 0:
            return False
        i += 1
    return True
