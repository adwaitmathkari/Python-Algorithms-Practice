
# Given a string S and a pattern P, find all the starting indices of the pattern’s anagrams in the given string.

# Note: 1) Anagrams mean permutations of the string. 2) Indexing of string starts from 0.


def find_anagrams(p, s):
    if len(p)>len(s):
        return []
    finalList = []
    d={}
    refDict = {}
    for ch in p:
        refDict[ch] = refDict.get(ch,0) + 1
    print(refDict)
    lp = len(p)

    for pointer in range(lp-1):
        d[s[pointer]] = d.get(s[pointer], 0) + 1
    print(d)
    for i in range(len(s) - len(p) + 1):
        d[s[i+lp-1]] = d.get(s[i+lp-1], 0) +1
        anagram = True
        for k in refDict.keys():
            if refDict[k] != d.get(k, -1):
                anagram = False
                break
        if anagram:
            finalList.append(i)
        d[s[i]] -=1
    return finalList

    

print(find_anagrams('aabcde', 'kasjdfglaskdhsadfaabcdebcdeaaf'))


