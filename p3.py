
def main():
    n = 600851475143
    biggest = 1
    i = 2
    while n > 1:
        if n % i == 0:
            print(i)
            n //= i
            biggest = i if (i > biggest) else biggest
        else:
            i += 1

    print(biggest)

if __name__ == "__main__":
    main()

