#!/usr/bin/env python

# In Python, each name is a tag refering to an object. So after a = b, a is b is also true.
# The intepretor caches some small integers and strings.
"""
If you are used to most traditional languages, you have a mental model of what happens in the following sequence:

a = 1
a = 2

You believe that "a" is a memory location that stores the value 1, then is updated to store the value 2. That's not how things work in Python. Rather, "a" starts as a reference to an object with the value 1, then gets reassigned to an object with value 2. 

When you call a function with a parameter, a new reference is created that refers to the object passed in. This is seperate from the referene that was used in the function call, so there's no way to update that referenceand make it refer to a new object.  
"""

"""
Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object. This is known as aliasing in other languages. This is usually not appreciated on a first glance at Python, and can be safely ignored when dealing with immutable basic types (numbers, strings, tuples). However, aliasing has a possibly surprising effect on the semantics of Python code involving mutable objects such as lists, dictionaries, and most other types. This is usually used to the benefit of the progarm, since aliases behave like pointers in some respects. For example, passing an object is cheap since only a pointer is passed by the implementation; and if a function modifies an object passed as an argument, the caller will see the change -- this eliminates the need for two different argument passing mechanisms as in Pascal.
"""
a = (1, 2, 3)
b = (1, 2, 3)
print id(a), id(b), a == b, a is b  # 4513741872 4513855920 True False
b = a
print id(a), id(b), a == b, a is b  # 4513741872 4513741872 True True



#Q: Why do we need immutable data types in Python?
#A: 1) Immutable objects can allow substantial optimization; this is presumably why strings are also immutable in Java, and just about everything is immutable in truly-functional languages.
#   2) In Python in particular, only immutables can be hashable (memebers of sets, keys in dictionaries). Again, this afford optimization.

#python -mtimeit '["free", "fie", "fo", "fum"]'
#python -mtimeit '("free", "fie", "fo", "fum"]'


#Q: In Python, is function argument passed by value or reference?
#A: Neither. 

# Key: the parameter passed in is actually a reference to an object, but the referene is passed by value.
# SO:
""" 1. If you pass a mutable object into a method, the method gets a referene to that same object, and you can mutate it, but if you rebind the reference in the method, the outer scope will know nothing about it . After you are done, the outer reference will still point at the original object. """

""" 2. If you pass an immutable object to a method, you still can't rebind the outer reference, and you can't even mutate the object. """

def update(list):
    list.append(1)

def reassign(list):
    list = [0, 1]

list = [0]
update(list) 
print list      # [0, 1]
list = [0]
reassign(list)
print list      # [0]

"""
B = A
    if A is immutable (int, string, tuple ...)
        if B changes, A doen not change
    if A is mutable (list, dict, ...)
        if B is modified in place, A also changes
        else if B is assigned to something else, A does not change

"""

"""
To try to mimic pass by reference, i.e. to change a immutable object in a function, you can do one of the two things
"""

#method1
def change(immutable):
    immutable = 'abc'
    return immutable

s = 'a'
s = change(s);
print s     # abc

#method2
def change(list):
    list[0] = 'abc'

s = ['a']
change(s)
print s[0]  # abc

