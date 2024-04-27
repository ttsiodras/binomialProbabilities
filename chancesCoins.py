#!/usr/bin/env python3
import random, sys

# How many times do you need to toss a coin to be 85% sure you'll see tails at least once? 
# Answer: at least 3

g_total = int(sys.argv[1]) if len(sys.argv)>1 else 100000

def fact(n):
    return 1 if n<=1 else n*fact(n-1)

def choose(n,k):
    return fact(n)/(fact(k)*fact(n-k))

def experiment(ntimes):
    success = 0
    for i in range(1, g_total):
        for j in range(0, ntimes):
            if random.choice([0,1]) == 0:
                success += 1
                break
    print("When trying", ntimes, "times, I got ", float(success)/g_total)

p = 0.5
for n in range(2, 5):
    experiment(n)
    print("The theory says...", sum([choose(n,i)*(p**i)*((1-p)**(n-i)) for i in range(1,n+1)]))
