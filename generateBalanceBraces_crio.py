# Setting up a recursion
# setting up a nice recursion
# start with one bracket and iterate over it
# OK so the braces are just '(' and ')'
# so that makes life easier
# for sure


def balancedBraces(n):
    finalList = []
    addBrace('', 0, finalList, n, n)
    return finalList


def addBrace(combination, braceVal, finalList, nLeft, nRight):
    if nLeft == nRight == 0:
        finalList.append(combination)
    if nLeft > 0:
        addBrace(combination+'(', braceVal+1, finalList, nLeft-1, nRight)
    if nRight > 0:
        if braceVal > 0:
            addBrace(combination+')', braceVal-1, finalList, nLeft, nRight-1)


print(len(balancedBraces(13)))


