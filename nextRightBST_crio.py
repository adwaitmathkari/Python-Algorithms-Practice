# from createBSTMinHeight import minimalTree

class TreeNodeNext:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


def populatingNextRightPointersInEachNode1(root):
    currl = [root]
    nextl = []
    flag = True

    while flag:
        for i in range(len(currl) - 1):
            if currl[i]:
                currl[i].next = currl[i+1]
        nextl = []

        for i in currl:
            if i:
                nextl += [i.left, i.right]
            else:
                nextl += [None, None]
        currl = nextl
        flag = False
        for i in currl:
            if i:
                flag = True


def populatingNextRightPointersInEachNode(root):
    currl = [root]
    nextl = []
    flag = True
    s = ''
    while flag:

        nextl = []

        for i in range(len(currl)):
            if i == len(currl) - 1:
                s+='null '
                if currl[i]:
                    nextl += [currl[i].left, currl[i].right]
                else:
                    nextl += [None, None]
                continue
            if currl[i]:
                currl[i].next = currl[i+1]
                val = currl[i+1].val if currl[i] else 'null'
                s+= str(val)+' '

                nextl += [currl[i].left, currl[i].right]
            else:
                nextl += [None, None]

        currl = nextl
        flag = False
        for i in currl:
            if i:
                flag = True
    s = s[:-1]
    print(s)
    return s 


t = TreeNodeNext(1)
t.left = TreeNodeNext(2)
t.right = TreeNodeNext(3)
t.left.left = TreeNodeNext(4)
t.left.right = TreeNodeNext(5)
t.right.left = TreeNodeNext(6)
t.right.right = TreeNodeNext(7)


populatingNextRightPointersInEachNode(t)

print(t.next, t.left.next.val, t.right.left.next.val)
