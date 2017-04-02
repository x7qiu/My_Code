#!/usr/bin/env	python

# Create an empty list
Empty1 = []
Empty2 = list()
## ex1
L = [1, 9, 8, 4]
LC = [elem*2 for elem in L]
print LC                            # [2, 18, 16, 8]

## ex2
LC = [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x**2 + y**2 == z**2]
print LC                            # [(3, 4, 5), (5, 12, 13), (6, 8, 10) ...] 

## ex3
L = ['a', 'mmm', 'foo', 'b', 'c', 'd', 'd']
LC = [elem for elem in L if L.count(elem) == 1]
print LC                            # ['a', 'mmm', 'foo', 'b', 'c']

## ex4
myDict = {'a':1, 'b':2, 'c':3, 'd':4}
under3 = [i[0] for i in myDict.items() if i[1] < 3]
print under3
under3 = [id for (id, salary) in myDict.items() if salary < 3]
print under3

## ex5
LC = []
outer = ['a', 'b', 'c']
inner = ['d', 'e', 'f']
for i in outer:
    for j in inner:
        LC.append(i+j)
print LC 

LC = [i+j for i in outer for j in inner]        # the order is consistent 
print LC
