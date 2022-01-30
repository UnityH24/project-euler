def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

def main():
    print(sum_digits(2 ** 1000))

if __name__ == "__main__":
    main()
