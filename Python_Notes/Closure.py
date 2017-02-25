#!/usr/bin/env  python

"""
import time
keepRunning = True
updates = []
def runLoop():
   while (keepRunning):
       for u in updates:
           u()

class foo:
   def __init__(self, x = 0):
       self.x = x

   def update(self):
       print self.x
       self.x += 1

f = foo()
g = foo(2)

updates.extend([f.update, g.update])
print updates
"""

## ex1
def startAt(x):
    def incrementBy(y):
        return x + y
    return incrementBy

closure1 = startAt(1)       # closure1 and closure2 are of function type
closure2 = startAt(2)

print closure1(1)       # --> 2
print closure2(1)       # --> 3

print closure1(1)       # --> 2
print closure2(1)       # --> 3

## ex2  dont quite understadn
def maker():
    count = [0]
    def counter():
        count[0] = count[0] + 1
        return count[0]
    return counter

a = maker()
print a()               # --> 1
print a()               # --> 2
print a()               # --> 3

print maker()()         # --> 1
print maker()()         # --> 1
print maker()()         # --> 1

