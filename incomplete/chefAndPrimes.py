"""
This is an interactive problem.

Shef chose some prime number P between 2 and 10^9 inclusive. You want to guess it.

Before that, you may ask Shef at most M questions, since he is quite busy. In each question,
you tell Shef an integer x (1≤x≤109) and Shef tells you x^2 modulo P. 
At the end, you guess Shef's prime P and he tells you if your guess was correct.

However, Shef will sometimes cheat: he can change his prime any number of times +
during the game (even after you tell him your guess), 
but only in such a way that all his answers to your previous questions remain correct.

Show Shef that you can always guess the correct prime, even if he tries to cheat!

first, M=10 and shef does not cheat
then  M=5 and chef does not cheat,
finally M=2.

"""

#thus here i want to find p
# and i cangive some X and get X^2 mod p
# thus if i give 200 then i can have (40000) mod p 
# if p=101 then 40000 mod 101 = 

def f(x,p):
    return (x**2)%p
print(f(200,101))#4

def generatePrimes():
    pass







