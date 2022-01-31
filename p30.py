def digit_sum(n):
    s = 0
    while n:
        s += (n % 10) ** 5
        n //= 10
    return s

def main():
    s = 0
    for i in range(2, 1000000):
        if digit_sum(i) == i:
            s += i
    print(s)

if __name__ == "__main__":
    main()
