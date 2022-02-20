#given a directed graph and nodes n1,n2 find if theres a path between n1 and n2

import sys
from time import time


def routeBetweenNode(start, end, n, edges):
    d = {}
    for e in edges:
        d[e[0]] = d.get(e[0], []) + [e[1]]

    exploredNodes = set()

    def find(curr, target, d, ans):
        if ans[0] or curr in exploredNodes:
            return
        
        exploredNodes.add(curr)

        for node in d.get(curr, []):
            if node == target:
                ans[0] = True
                return
            if node not in exploredNodes:
                find(node, target, d, ans)

    ans = [False]
    find(start, end,  d, ans)
    return ans[0]


def routeBetweenNode1(start, end, n, edges):
    #make a universal list of good nodes
    # go t oeach node taht was just recently traversed
    # and add all the next nodes for those nodes

    # going breadth first
    d = {}
    for e in edges:
        d[e[0]] = d.get(e[0], []) + [e[1]]

    explored = set()
    explored.add(start)
    currNodes = [start]
    # def find(curr, target,  )
    while currNodes != []:
        nextNodes = []
        for node in currNodes:
            for nextn in d.get(node, []):
                if nextn == end:
                    return True
                if nextn not in explored:
                    explored.add(nextn)
                    nextNodes.append(nextn)
        currNodes = nextNodes
    return False 


f = open("input.txt")
T = int(f.readline())
sys.setrecursionlimit(20 * 1000)

t=time()
for _t in range(T):
    n, m = map(int, f.readline().strip().split())
    edges = list()
    for i in range(m):
        edge = list(map(int, f.readline().strip().split()))
        edges.append(edge)
    start, end = map(int, f.readline().strip().split())


    result = routeBetweenNode(start, end, n, edges)
    print('yes' if result else 'no')

print("DFS ALG", time() - t)
f.close()


f = open("input.txt")
T = int(f.readline())

t = time()
for _t in range(T):
    n, m = map(int, f.readline().strip().split())
    edges = list()
    for i in range(m):
        edge = list(map(int, f.readline().strip().split()))
        edges.append(edge)
    start, end = map(int, f.readline().strip().split())

    result = routeBetweenNode1(start, end, n, edges)
    print('yes' if result else 'no')

print("iterative bfs alg", time() - t)
