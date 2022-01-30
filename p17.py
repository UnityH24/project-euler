nums = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

tens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}
teens = {
    1: "eleven",
    2: "twelve",
    3: "thirteen",
    4: "fourteen",
    5: "fifteen",
    6: "sixteen",
    7: "seventeen",
    8: "eighteen",
    9: "nineteen"
}

def num_to_english(n):
    if n == 0:
        return "zero"
    num = str(n)
    while len(num) < 6:
        num = "0" + num

    l = []
    
    th = int(num[-6:-3])
    h  = int(num[-3])
    t  = int(num[-2])
    o  = int(num[-1])

    if th:
        l.append(f"{num_to_english(th)} thousand")

    if h:
        l.append(f"{nums[h]} hundred")
    if t:
        if h:
            l.append("and")
        if t != 1:
            l.append(tens[t])
        else:
            if o:
                l.append(teens[o])
            else:
                l.append("ten")
            return " ".join(l)
    if o:
        if h:
            if not t:
                l.append("and")
        l.append(nums[o])
    return " ".join(l)

def count_letters(s):
    cs = 0
    for c in s:
        if not c.isspace():
            cs += 1
    return cs

def main():
    s = 0
    for i in range(1, 1000000):
        n = num_to_english(i)
        print(n)
        s += count_letters(n)
    print(s)

if __name__ == "__main__":
    main()
