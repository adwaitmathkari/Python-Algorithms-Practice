def kthCharacter(s, e, k, table):
    if s==0:
        l = table[e]
    else:
        l = [table[e][i] - table[s-1][i] for i in range(26)] 
    sch = 0
    for i in range(26):
        sch+=l[i]
        if sch>=k:
            return chr(i+97)

def build_table(s):
    d = {}
    l = [0 for i in range(26)]
    fl = []
    for i in range(len(s)):
        l[ord(s[i])-97] += 1
        fl.append(l[:])
    return fl

def main():
    f = open("kthChar_test.txt")
    (n, num_tests) = [int(x) for x in f.readline().strip().split()]
    one_str = f.readline().strip()
    table = build_table(one_str)



    for i in range(num_tests):
        (s, e, k) = [int(x) for x in f.readline().strip().split()]
        print(kthCharacter(s-1, e-1, k, table))


main()
