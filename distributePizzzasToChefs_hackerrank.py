

# The Chefs of the restaurants are asked to prepare Pizzas for their customers. The Restaurant has N chefs and each chef has a rank R(1<=R<=10). A chef with a rank R can cook x Pizzas by the given function:

# F(x) = R* (x*x - x +1) .

# Where F(x) is the time taken ( In minutes ) to make x pizzas. Here R is the rank of the chef.

# The waiter has already taken the orders and wants to know the minimum time to get the orders done.

# NOTE: All the chefs can make Pizzas parallelly.

# Input Format

# The first line tells the number of test cases. Each test case consists of 2 lines. In the first line of the test case we have P the number of Pizzas ordered and the number of chefs N. In the next line N integers denotes the rank of a chef.

# Constraints

# 1<=|T|<=1000
# 1<=|P|<=1000
# 1<=|N| <=100
# 1<=Rank[i]<=10
# Output Format

# For each test case print an integer which tells the number of minutes needed to get the order done in a new line.

# Sample Input 0

# 3
# 10 4
# 1 2 3 4
# 8 1
# 1
# 8 8
# 1 1 1 1 1 1 1 1
# Sample Output 0

# 13
# 57
# 1
# Explanation 0

# For Test case 1: Chef 1 will make 4 pizzas , Chef 2 ,Chef 3, Chef 4 will make two pizzas each.
# For Test case 2: The Chef 1 will make all 8 pizzas.
# For Test case 3: All Chefs will make 1 pizza each.


import math


def r(x):
    return x**2-x+1


def maxPizzasIntTime(t, r):
    if t < r:
        return 0
    # t = r(x**2 -x +1)
    root = (1 + math.sqrt(1+4*(t/r - 1)))/2
    return int(root)


def possibleInTime(t, pizzas, chefs):
    sum1 = 0
    for chef in chefs:
        sum1 += maxPizzasIntTime(t, chef)
    return sum1 >= pizzas


def leastTime(pizzas, chefs):

    # binary over time = 0 to time = maximum
    p = pizzas
    maxTime = 10*(p**2-p+1)

    # binary
    least = 0
    most = maxTime

    while (least <= most):
        mid = (least+most) // 2

        if possibleInTime(mid, pizzas, chefs):
            most = mid - 1
        else:
            least = mid+1

    if possibleInTime(most, pizzas, chefs):
        return most
    else:
        return least



def solve():
    for _ in range(int(input())):
        pizzas, nch = map(int, input().split())
        chefs = list(map(int, input().split()))
        print(leastTime(pizzas, chefs))

def test():

    for chefs, pizzas in [([1,2,3,4], 10), ([1,1,1,1,1,1,1,1], 8), ([1], 10)]:

        print(leastTime(pizzas, chefs))
solve()
# test()