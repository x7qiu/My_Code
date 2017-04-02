#!/usr/bin/env  python

## get index of max elem in a list
a = [32, 37, 28, 30, 37, 25, 27, 24, 35, 55, 23, 31, 55, 21, 40, 18, 50,
             35, 41, 49, 37, 19, 40, 41, 31]

m = max(a)
[i for i,j in enumerate(a) if j == m]   # get all indices of max elem

a.index(max(a))                         # get one index of max elem

## 4
"""
with open("ztest.txt") as f:           # f is always closed even if a problem was encountered
    for line in f:
        print line
"""

## 5
A = [[1,2,3,4],
     [5,6,7,8]]

def column(matrix, i):
    return [row[i] for row in matrix]

#print column(A,2)

## 6 similar
elements = [(1,2,3),
            (4,5,6),
            (7,8,9)]

seconds = [x[1] for x in elements]
seconds = zip(*elements)[1]
#print seconds

#or
import operator
map(operator.itemgetter(1), elements)


## number of lines in a file
with open("ztest.txt") as f:
    print sum(1 for _ in f)

## remove duplicate in a list, not preserving order. Assuming items hashable
def uniq(items):
    return list(set(items))

## remove duplicate in a list, preserving order
## Using a set reduces "in" operation to O(1) instead of O(n) for a list, but requires hashable elements
def unique(items):
    found = set()
    keep = []
    for item in items:
        if item not in found:
            found.add(item)
            keep.append(item)
    return keep

def unique2(items):
    seen = set()
    seen_add = seen.add     # reduce resolving time
    return [item for item in items if not (item in seen or seen_add(item))]

L = [2, 1, 4, 3, 5, 1, 2, 1, 1, 6, 5]
#print uniq(L)
#print unique(L)
print unique2(L)

# Irrelavent, but iterating backwards over the indices ensure that removing items doesn't affect the iteration.

list1 = [1, 2, 3]
a = list1 * 3
b = [list1] * 3
print a             # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print b             # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

list1[2] = 4
print a             # [1, 2, 3, 1, 2, 3, 1, 2, 3]       # unchanged
print b             # [[1, 2, 4], [1, 2, 4], [1, 2, 4]] # changed, because reference to list, not copy

