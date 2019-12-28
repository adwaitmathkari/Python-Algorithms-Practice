"""

Morse code is the cheapest and most popular way of message communitcation. 
In Morse code, each letter of the alphabet is represented by a sequence of 
dots and dashes. Traditionally, dots were transmitted by a short note and 
dashes by a longer note, with pauses between different letters. Morse code 
representation of each letter of the english alphabet are as follows

a .-
b -...
c -.-.
d -..
e .
f ..-.
g --.
h ....
i ..
j .---
k -.-
l .-..
m --
n -.
o ---
p .--.
q --.-
r .-.
s ...
t -
u ..-
v ...-
w .--
x -..-
y -.--
z --..


For example dog is written as -..-----. Note that every combination of between 1 and 4 
dots and dashes is used, except for
..--
.-.-
---.
----
Interestingly incoming message tone of many mobile phones make the sound ... -- ... 
when receiving a SMS. Because this is the Morse Code for 'SMS'. Main problem with Morse 
Code is the gaps between letters. If gaps are absent by mistake then the message becomes ambiguous. 
For example, let the message is -..-----. and it is made up of three letters, it might mean njg, 
dog, xmg or xon. Again, let the message is -...----.--. and it is also made up of three letters. 
It might mean boy or djy. Write a program which reads in a message (between 1 and 10 letters all, both inclusive) 
and determines how many messages, with the same number of letters as the input, it might represent. 
Your program should output all possible messages. You have to consider small case letters only (a-z). 
Consider only 'dog', not 'DOG' or 'Dog'.

Input
First line of the input file will specify the number of test cases. 
In the following line you have to specify that many test cases, one at each line.

Output
For each test case the output file must have all possible messages, one message per line. 
At the end it should have- totaln Where 'n' is the total number of messages possible. 
For a wrong input (like 'Code' in above sample file), output file should contain the entry 'error' 
and in the following line it should mention 'total 0'.

Example
Input:
3
dog
man
Code

Output:
dog

njg

xmg

xon

total 4

gme

gtn

man

meg

mwe

qte

tkn

tng

ttp

tye

total 10

error

total 0


"""









