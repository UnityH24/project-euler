def d(n):
    if n == 0: return 0
    s = 1 
    
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            s += i

    return s

h = 0
for a in range(10000):
    b = d(a)
    if a != b:
        if d(b) == a:
            h += a
print(h)
