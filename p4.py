
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def main():
    curr_largest = (0, 0, 0)
    for a in range(100, 1000):
        for b in range(100, 1000):
            prod = a * b
            if is_palindrome(prod) and prod > curr_largest[0]:
                curr_largest = (prod, a, b)


    print(curr_largest)

if __name__ == "__main__":
    main()
