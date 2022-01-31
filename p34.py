from functools import cache

@cache
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

def digit_sum(n):
    s = 0
    while n:
        s += fact(n % 10)
        n //= 10
    return s

def main():
    s = 0
    for i in range(3, 1000000):
        if digit_sum(i) == i:
            s += i
    print(s)

if __name__ == "__main__":
    main()

