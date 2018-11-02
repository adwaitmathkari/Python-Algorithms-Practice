# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 20:16:15 2017

@author: Adwait
"""
import random

def genEven():
    import random
    ans=random.randrange(0, 100, 2)
    return ans

for i in range(10):
    print(genEven())
    
random.random()                             # Random float:  0.0 <= x < 1.0
#0.37444887175646646

random.uniform(2.5, 10.0)                   # Random float:  2.5 <= x < 10.0
#3.1800146073117523

random.expovariate(1 / 5)                   # Interval between arrivals averaging 5 seconds
#5.148957571865031

random.randrange(10)                        # Integer from 0 to 9 inclusive
#7

random.randrange(0, 101, 2)                 # Even integer from 0 to 100 inclusive
#26

random.choice(['win', 'lose', 'draw'])      # Single random element from a sequence
#'draw'

deck = 'ace two three four'.split()
random.shuffle(deck)                        # Shuffle a list
deck
#['four', 'two', 'ace', 'three']

random.sample([10, 20, 30, 40, 50,60,70,80,90,100], k=4)    # Four samples without replacement
#[40, 10, 50, 30]

 # Six roulette wheel spins (weighted sampling with replacement)
random.choices(['red', 'black', 'green'], [18, 18, 2], k=6)
#['red', 'green', 'black', 'black', 'red', 'black']

# Deal 20 cards without replacement from a deck of 52 playing cards
# and determine the proportion of cards with a ten-value
# (a ten, jack, queen, or king).
deck = random.collections.Counter(tens=16, low_cards=36)
seen = random.sample(list(deck.elements()), k=20)
seen.count('tens') / 20
#0.15

#>>> # Estimate the probability of getting 5 or more heads from 7 spins
#>>> # of a biased coin that settles on heads 60% of the time.
trial = lambda: random.choices('HT', cum_weights=(0.60, 1.00), k=7).count('H') >= 5
sum(trial() for i in range(10000)) / 10000
#0.4169

#>>> # Probability of the median of 5 samples being in middle two quartiles
trial = lambda : 2500 <= sorted(random.choices(range(10000), k=5))[2]  < 7500
sum(trial() for i in range(10000)) / 10000
#0.7958