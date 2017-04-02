#!/usr/bin/env  python
import time

# One-liner: an iterator that's used to generate a series of values, usually fed to a FOR loop.

"""
When we call a normal Python function, execution starts at function's first line and continues until a RETURN statement, EXCEPTION, or the end of the function is encountered. Once a function returns control to its caller, that's it. Any work done by the function and stored in local variables is lost. A new call to the funtion creates everything from scratch.

Sometimes it's beneficial to have the "function" save its work, in which case the transfer of control is temporary and voluntary, and it is expected to be regained at a later time.
"""

# Why do we use generators?
"""
To give back a sequence of items one at a time instead of all at once.

It saves memory, improves effiency and solves problems otherwise cannot be solved by simple iterators.
i.e. when searching for a file in system, or generating infinite sequence of numbers.
"""

# How to create and use generators?
"""
By keyword "yield", "xrange" in Python2.x , or list comprehension with "()"

Generators are special type of iterators. Therefore we can use the built-in next() to get the next value, or use generators in places where iterators are used. For example in a FOR loop.

If the generator is created using YIELD, then, when you call the function, the code in the function body does not run. Instead, it returns a generator object. When you use next() on the generator, it executes the function body until it encounters a YIELD. At this point the state is saved, and the control flow is passed back. When you use next() on the generator again, execution starts at where it left off, aka one line after YIELD, untill it reaches the next YIELD or the end of loop, in which case another next() call will raise the StopIteration exception.
"""

## Example 
def simple_gen():
    yield 1
    yield 2
    yield 3

gen = simple_gen()          # now gen is a generator
print gen                   # <generator object simple_gen at 0x10f63a0f0>
print "first next(gen) yields", next(gen)         # next(gen) is more accurat and Python3 compatible
print "second next(gen) yields", next(gen)
print "third next(gen) yields", next(gen)
#print gen.next()           #StopIteration Exception

## Example       #from Python Essential Reference, PER
def countdown(n):
    print "Counting Down!"      # only gets printed once
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print i                     

# Example
def count(a, b):
    print "This line only print once!"
    while a > 0:
        yield a
        print "xixi"
        a -= 1
    while b > 0:
        yield b
        b -= 1

x = count(2, 2)
print next(x)       # This line only print once! 2
print next(x)       # 1
print next(x)       # 2
print next(x)       # 1

# Example  <infinite integers> 
def infi():
    i = 0
    while True:
        yield i
        i += 1

# Example  <fibonacci series>
def fib():
    a, b = 0,1 
    while 1:
        yield b
        a, b = b, a+b

# Example  <used as iterator in a for loop> 
doubles1 = [2*n for n in range(3)]     # standard list comprehension syntax    
doubles2 = (2*n for n in range(3))     # generator
for i in doubles2:
    print i

# Example  <efficiency>
start1 = time.time()
sum1 = sum(range(10000))
print "sum1 is", sum1
print "time used for sum1 is", time.time() - start1

start2 = time.time()
sum2 = sum(xrange(10000))
print "sum2 is", sum2
print "time used for sum2 is", time.time() - start2

# Example  <efficiency again!>
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn2(n):
    num = 0
    while num < n:
        yield num  
        num += 1

start11 = time.time()
sum11 = sum(firstn(100000))
print "time used for 1 is ", time.time() - start11


start22 = time.time()
sum22 = sum(firstn2(100000))
print "time used for 2 is ", time.time() - start22

# When is not a good time to use generators?
# 1) When you need to access data multiple times.
# Example
for i in xrange(100):     # loop through once , OK to use generator 
    for j in range(10):  # loop through multiple times, better to return a list
        i+j
# 2) When you need randome access, because generators don't keep an intanct list in memory.
# 3) When you need to performe len(), reversed(), keyword "in", and so on for the same reason above.







# Question: How to use both yield and return in the same function?
