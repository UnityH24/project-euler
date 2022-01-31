def main():
    a, b = 1, 1
    count = 1
    while len(str(a)) < 1000:
        c = a + b
        a = b
        b = c
        count += 1
    print(count)

if __name__ == "__main__":
    main()
