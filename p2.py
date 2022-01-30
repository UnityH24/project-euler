
def generate_fib(n):
    a, b = 0, 1
    while b < n:
        if b % 2 == 0:
            yield b
        z = a + b
        a = b
        b = z

def main():
    print(sum(generate_fib(4000000)))

if __name__ == "__main__":
    main()
