from functools import cache

def collatz(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def main():
    longest = (0, )
    for i in range(3, 1000000):
        print(i)
        l = collatz(i)
        if l > longest[0]:
            longest = (l, i)
    print(longest)

if __name__ == "__main__":
    main()
