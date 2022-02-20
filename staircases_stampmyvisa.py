"""

King Lear's wants to address his kingdom in a grand style. Help him out with your programming skills.
King Lear is preparing for his debut on the grand stage - but in order to make a grand entrance, he 
needs a grand staircase! As his personal assistant, you've been tasked with figuring out how to build 
the best staircase EVER.Lear has given you an overview of the types of blocks available, plus a budget. 
You can buy different amounts of the blocks. King Lear wants to know how many different types of staircases 
can be built with each amount of blocks, so he can pick the one with the most options.Each type of staircase 
should consist of 2 or more steps. No two steps are allowed to be at the same height - each step must be lower 
than the previous one. All steps must contain at least one block. A step's height is classified as the total 
amount of blocks that make up that step.Write a function called countPossibleStaircases(n) that takes a 
positive integer n and returns the number of different staircases that can be built from exactly n blocks.
 n will always be at least 3 (so you can have a staircase at all), but no more than 600, because King Lear's 
 not made of money!
 
 For example, when N = 3, you have only 1 choice of how to build the staircase, with
 the first step S1 having a height of 2 and the second step S2 having a height of 1:
(# indicates a block)
#
#   #
S1 S2
Here the staircase has 2 steps: S1 and S2 where height(S1) = 2, height(S2) = 1
Notice that height(S1) > height(S2) is the rule.When N = 4, you still only have 1 staircase choice:
#
#
#   #
S1 S2
Here the staircase has 2 steps: S1 and S2 where height(S1) = 3, height(S2) = 1
Notice that height(S1) > height(S2) is the rule.But when N = 5, there are two ways you can build a staircase from the given blocks. The two staircases can have heights (4, 1) or (3, 2), as shown below:
#
#
#
#   #
S1 S2
Here the staircase has 2 steps: S1 and S2 where height(S1) = 4, height(S2) = 1
Notice that height(S1) > height(S2) is the rule.

#
#   #
#   #
S1 S2
Here the staircase has 2 steps: S1 and S2 where height(S1) = 3, height(S2) = 2
Notice that height(S1) > height(S2) is the rule.Similarly when N = 6, there are three ways you can build a staircase from the given blocks: (5, 1), (4, 2), (3, 2, 1). Last one is shown below:
#
#   #
#   #   #
S1 S2 S3
Here the staircase has 3 steps: S1, S2 and S3 where height(S1) = 3, height(S2) = 2, height(S3) = 1
Notice that height(S1) > height(S2) > height(S3) is the rule.Test Case 1:
Input:
(int) n = 3
Output:
(int) 1Test Case 2:
Input:
(int) n = 4
Output:
(int) 1Test Case 3:
Input:
(int) n = 5
Output:
(int) 2Test Case 4:
Input:
(int) n = 6
Output:
(int) 3
Test Case 4:
Input:
(int) n = 8
Output:
(int) 5
If your code is taking more than a second to execute, you are not doing it right. Think smarter!

"""



def addStep(lastNum,sum1,lim, nCombinations):
    if sum1==lim:
        # print(lastNum,sum1,lim,nCombinations[0])
        nCombinations[0]+=1
    else:
        if sum1+lastNum+1>lim:
            nCombinations[0]+=1
        else:
            addStep(lastNum+1, sum1+1, lim,nCombinations)
            addStep(lastNum+1, sum1+lastNum+1, lim, nCombinations)
def findNoOfCombinations(n):

    nCombinations = [0]

    addStep(1,1,n,nCombinations)

    return nCombinations[0]-1



for _ in range(5):
    print(findNoOfCombinations(int(input())))



