#!/usr/bin/env python3
import random, sys

# How many times do you need to toss a die to be 85% sure you'll see a one at least once? 
# Answer: 11 (not 10, as in the article)

g_total = int(sys.argv[1]) if len(sys.argv)>1 else 100000

def fact(n):
    return 1 if n<=1 else n*fact(n-1)

def choose(n,k):
    return fact(n)/(fact(k)*fact(n-k))

def experiment(ntimes):
    success = 0
    for i in range(1, g_total):
        for j in range(0, ntimes):
            if random.choice([1,2,3,4,5,6]) == 1:
                success += 1
                break
    print("When trying", ntimes, "times, I got ", float(success)/g_total)

p = 1./6.
for n in range(2, 15):
    experiment(n)
    print("The theory says...", sum([choose(n,i)*(p**i)*((1-p)**(n-i)) for i in range(1,n+1)]))
