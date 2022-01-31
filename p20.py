def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i 
    return f

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def main():
    print(sum_digits(fact(100)))

if __name__ == "__main__":
    main()