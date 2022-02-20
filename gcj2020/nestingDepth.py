"""
Problem
tl;dr: Given a string of digits S, insert a minimum number of opening and closing parentheses 
into it such that the resulting string is balanced and each digit d is inside exactly d pairs 
of matching parentheses.

Let the nesting of two parentheses within a string be the substring that occurs strictly 
between them. An opening parenthesis and a closing parenthesis that is further to its 
right are said to match if their nesting is empty, or if every parenthesis in their 
nesting matches with another parenthesis in their nesting. The nesting depth of a position p is the number of pairs of matching parentheses m such that p is included in the nesting of m.

For example, in the following strings, all digits match their nesting depth: 
0((2)1), (((3))1(2)), ((((4)))), ((2))((2))(1). 
The first three strings have minimum length among those that have the same digits in the same order, but the last one does not since ((22)1) also has the digits 221 and is shorter.

Given a string of digits S, find another string S', comprised of parentheses and digits, such that:
all parentheses in S' match some other parenthesis,
removing any and all parentheses from S' results in S,
each digit in S' is equal to its nesting depth, and
S' is of minimum length.

Input
The first line of the input gives the number of test cases, T. T lines follow. Each line represents a test case and contains only the string S.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the string S' defined above.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ length of S ≤ 100.

Test set 1 (Visible Verdict)
Each character in S is either 0 or 1.

Test set 2 (Visible Verdict)
Each character in S is a decimal digit between 0 and 9, inclusive.


"""

# strategy: 
# when non zero no is encountered put an opening bracket
# scan till the next zero and close bracket before it 
# if reach 0 then put the minimum no of closing brackets before the zero 
# subtract the min from all the numbers
# repeat




def solve(s):
    # s is '13428'
    ln = len(s)
    brackets=[[0,0] for i in range(ln +1)]

    l=list(map(int, list(s)))

    for _ in range(11):

        for i in range(ln):

            #if first and non zero then add an open bracket before
            #decrement by 1
            #continue till zero element is found or end is reached and add a closed bracket

            if i==0:
                if l[i]>0:
                    #open bracket at 0 and closed bracket at 1 in the tuple
                    brackets[i][0]+=1
            
            #if an element after 0 then need to add open bracket
            else:
                if l[i-1] == 0 and l[i]>0:
                    brackets[i][0]+=1
            
            if i==ln-1:
                if l[i]>0:
                    #add closed bracket after
                    brackets[i+1][1] +=1
            else:
                if l[i+1]==0 and l[i]>0:
                    brackets[i+1][1]+=1
        
        for i in range(ln):

            if l[i]>0:
                l[i]-=1

    #now need to make the string
    #need brackets s

    final=''
    for i in range(ln):
        final+=')' * brackets[i][1]
        final+='(' * brackets[i][0]
        final+= s[i]
    
    
    final+=')'*brackets[ln][1]
    # print(brackets)
    return final




t = int(input())

for case in range(1,t+1):
    print("Case #"+ str(case) +": "+solve(input()))




print(solve('111000212'))
print(solve('13428'))
print(solve('1101011111110110101010111111111111110000001110011111'))
