"""
You land up in King Lear's kingdom with your laptop. Help him out with your programming skills.
King Lear loves efficiency and hates anything that wastes time. He's very smart after all! 
He generously rewards people who identify sources of inefficiency and come up with ways to remove them. 
You've spotted one such source, and you think solving it will help you build the reputation you need to 
get promoted.Every time the King's servants pass each other in the corridor, each of them must stop and 
greet each other - one at a time - before resuming their path. A greet is five seconds long, so each 
exchange of greets takes a full ten seconds (King Lear's greet is a bit, er, involved). You think that 
by removing the greet requirement, you could save several collective hours of servent time per day. 
But first, you need to show him how bad the problem really is.Write a program that counts how many 
greets are exchanged during a typical walk along a corridor. The corridor is represented by a string.
For example: "--->-><-><-->-"Each corridor string will contain three different types of characters: '>', 
an servent walking to the right; '<', an servent walking to the left; and '-', an empty space. 
Every servent walks at the same speed either to right or to the left, according to their direction. 
Whenever two servants cross, each of them greets the other. They then continue walking until they 
reach the end, finally leaving the corridor. In the above example, they greet 10 times.Write a function 
countGreets(s) which takes a string representing servants walking along a corridor and returns the number 
of times the servants will greet. s will contain at least 1 and at most 10000 characters, each one of -, >, or <.

Test Case 1:
Input:
(string) s = "--<-<>-->--<"
Output:
(int) 4

Test Case 2:
Input:
(string) s = "----><----"
Output:
(int) 2

Test Case 3:
Input:
(string) s = "--->-><-><-->-"
Output:
(int) 10

"""

def servantGreetings(s):
        
    rightS=0
    leftS=0
    greetings=0
    for i in range(len(s)):
        if s[i]=='>':
            rightS+=1
        elif s[i]=='<':
            greetings+=rightS
    for i in range(len(s)-1,-1,-1):
        if s[i]=='<':
            leftS+=1
        elif s[i]=='>':
            greetings+=leftS
    return greetings

    
s='-<>-<<<<<--<><<<>>--><>>><--><-<><>-<<<<>>>><--<><<->>>>><>><<->-<>><'
print(servantGreetings(s))

