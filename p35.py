def sieve(limit):
    is_prime = [False, False] + [True] * (limit - 2)
    i = 2
    while i * i < limit:
        if is_prime[i]:
            j = i*i
            while j <= limit:
                is_prime[j] = False
                j += i
        i += 1
    return is_prime

def first_digit(n):
    size = 0
    while n > 9:
        n //= 10
        size += 1
    return n, size

def rot(n):
    a, b  = first_digit(n)
    return n - (a * 10 ** b) + a, b

def main():
    primes = sieve(1000000)
    for i in range(1000000):
        if primes[i]:
            rotated = 


