from collections import Counter

def get_prime_factors(n):
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            n /= i
            factors.append(i)
        else:
            i += 1
    return factors

def product(l):
    p = 1
    for i in l:
        p *= i
    return p

def main():
    counts = {i:0 for i in range(2, 21)}
    for i in range(2, 21):
        factors = get_prime_factors(i)
        num_factors = Counter(factors)
        for j in num_factors:
            num = num_factors[j]
            if num > counts[j]:
                counts[j] = num
    print(product([a ** b for a, b in counts.items()]))
        

if __name__ == "__main__":
    main()
