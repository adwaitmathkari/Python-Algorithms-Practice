"""
Last week Saraswathi celebrated her 3rd birthday. She received a xylophone as a birthday gift. This xylophone has 8 keys(A,B,C,D,E,F,G,H). Saraswathi started liking the tunes she could produce with that. She does not like certain sequences that make her cry. A tune is unpleasant when it contains a sequence that make her cry. All other tunes are pleasant tunes. Ram her brother who is studying combinatorics in school, wants to find out for a given tune how many distinct non-empty sub tunes exist that are pleasant. Can you help Ram by writing a program that answers his question?

T - Given tune

S - sub tune of the given tune

T - any combination of keys (A,B,C,D,E,F,G,H)

S - where every key used is present in T. If a particular key is present in T K times then you can use that key in S upto K times.

Example 1

T - ABC

S - A, B, C, AB, BA, AC, CA, BC, CB, ABC, ACB, BAC, BCA, CBA, CAB.

Example 2

T - AAB

S - A, B, AA, AB, BA, AAB, ABA, BAA

Input Format

Given Tune

N - (number of tunes that saraswathi dislikes)

N-lines each containing one such tune.

Constraints

Length of the Tune is <= 8

Output Format

Number of pleasant subtunes of the given tune.

"""

from itertools import combinations, permutations




def answer(tune, patterns):
    # 'abcda'
    # patterns [ab,ac,ade,aa]
    #  
    set1 = set()
    ltune = list(tune)
    # print(ltune)
    for lenTune in range(1,len(tune)+1):
        #lenTune
        listCombinations = list(combinations(ltune, lenTune))
        # print('combi---------', listCombinations)
        for combi in listCombinations:
            # print(''.join(list(combi)))
            lPermutations = list(permutations(''.join(list(combi))))
            # print(lPermutations)
            for permu in lPermutations:
                sPermu = ''.join(list(permu))
                good = True
                for pat in patterns:
                    if pat in sPermu:
                        good = False
                        break
                if good:
                    set1.add(sPermu)
    
    finalList = list(set1)
    # print(finalList)
    return len(finalList)


if __name__ == '__main__':

    given_tune = input()
    number_of_unpleasant_patterns = int(input())
    unpleasant_patterns = [input() for i in range(number_of_unpleasant_patterns)]
    print(answer(given_tune, unpleasant_patterns))
