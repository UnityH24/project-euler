file = "names.txt"

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    piv = arr.pop()
    gtp = []
    ltp = []
    
    for i in arr:
        if comp_strings(i, piv):
            gtp.append(i)
        else:
            ltp.append(i)
    return quicksort(ltp) + [piv] + quicksort(gtp)

def comp_strings(s1, s2):
    i = 0  
    s1_len = len(s1)
    s2_len = len(s2)
    while len(s1) < s2_len:
        s1 += 'a'
    while len(s2) < s1_len:
        s2 += 'a'
    while s1[i] == s2[i]:
        i += 1
    return ord(s1[i]) > ord(s2[i])

def main():
    names = [name[1:len(name) - 1] for name in open(file).read().split(',')]
    sorted_names = quicksort(names)
    s = 0
    for i, name in enumerate(sorted_names):
        score = 0
        for c in name:
            score += ord(c) - 64
        score *= (i + 1)
        s += score
        print(i + 1, name, score)
    print(s)

if __name__ == "__main__":
    main()
