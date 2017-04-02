#!/usr/bin/env  python

"""
An ITERABLE is 
    anything that can be loop over (i.e. string or file)
    anything that can appear on the right-side of a FOR-loop: for x in iterable:
    anything that you can call with iter() and have it return an ITERATOR
    an object that defines __iter__ that returns a fresh ITERATOR, or it may have a __getitem__ method suitable for indexed lookup

An ITERAOR is
    an obejct with state that remembers where it is during iteration
    an object with a __next__ method in Python3, next method in Python2, that 
        returns the next value in the iteration
        updates the state to point at the next value
        signals when it is done by raising StopIteration error
    an object that is self-iterable, meaning that it has an __iter__ method that returns itself
"""

# The builtin function next calls the __next__ method in Python 3 or next method in Python 2 on the object

# Iterator Protocol 
"""
When you write >>>for x in some_iterable:
                    ...loop body...
 
python performs the following two steps

1) Gets an iterator for some_iterable, by calling iter(some_iterable). This returns an object with an next() or __next__() method.

2) Keep calling the next() method on the iterator returned from step1. The return value from next() is assigned to x and the loop body is executed. If the exception StopIteration is raised from within next(), it means there are no more values in the iterator and the loop is exited.

An important thing to note is that Python performs the above two steps anytime it wants to loop over the contents of an object -- so it could be a FOR loop, but it could also be code like >>> listA.extend(listB).
"""

"""
There are four ways to build an iterative function:
    create a generator using the YIELD keyword
    use a generator expression
    create an iterator (defines __iter__ and __next__)
    create a function that Python can iterate over on its own (defines __getitem__)

"""

def uc_gen(text):
    for char in text:
        yield char.upper()

def uc_genexp(text):
    return (char.upper() for char in text)

class uc_iter():
    def __init__(self, text):
        self.text = text
        self.index = 0
    def __iter__(self):
        return self
    def next(self):
        try:
            result = self.text[self.index].upper()
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

class uc_getitem():
    def __init__(self, text):
        self.text = text
    def __getitem__(self, index):
        result = self.text[index].upper()
        return result

for iterator in uc_gen, uc_genexp, uc_iter, uc_getitem:
    for ch in iterator('abcde'):
        print ch,
    print






class MyList(object):
    def __init__(self):
        self.list = [42, 3.1415, "Hello World!"]
    def __iter__(self):
        return iter(self.list)

m = MyList()
for x in m:
    print x
# 42
# 3.1415
# Hello World!

class Seq(object):
    def __init__(self):
        self.x = 0
    def next(self):     # python2 only, __next__ in Python3
        if self.x < 10:
            self.x += 1
            return self.x
        else:
            raise StopIteration
    def __iter__(self):
        return self

s = Seq()
for x in s:
    print x
    
# All generators are iterators
def f123():
    yield 1
    yield 2
    yield 3

for x in f123():
    print x
#1
#2
#3

"""
class weird():
    def __init__(self):
        self.x = 0
    def next(self):
        if self.x < 10:
            self.x += 1
            yield self.x
        else:
            raise StopIteration
    def __iter__(self):
        return self

x = weird()
print next(next(x))
print next(next(x))
"""


