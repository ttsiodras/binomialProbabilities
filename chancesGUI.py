#!/usr/bin/env python
import sys

# How many users do you need to use to identify a GUI bug that occurs at 31% chance?
# This program prints the probabilities of the bug happening to at least one user,
# for noOfUsers from 2 to 12

g_total = int(sys.argv[1]) if len(sys.argv)>1 else 100000

def fact(n):
    return 1 if n<=1 else n*fact(n-1)

def choose(n,k):
    return fact(n)/(fact(k)*fact(n-k))

p = .31
for n in xrange(2, 13):
    print "The theory says for noOfUsers", n, "probability is", sum([choose(n,i)*(p**i)*((1-p)**(n-i)) for i in xrange(1,n+1)])
