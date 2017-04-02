#!/usr/bin/env python

### With the above line we can do the following:
### chmod +x Re.py
### ./Re.py
import re

### CHEAT SHEET
# .         Any char except \n
# a         the char a
# ab        the string ab
# a|b       a or a
# a*        0 or more a's
# \         Escapes a special char

# *         0 or more
# +         1 or more
# ?         0 or 1
# {2}       exactly 2
# {2, 5}    btw 2 and 5
# {2, }     2 or more
# {, 5}     up to 5

# [a-d]     one char of the set {a, b, c, d}
# [^a-d]    one char except the set {a, b, c, d}   
# \d        one digit
# \D        one non-digit
# \s        one whitespace
# \S        one non-whitespace
# \w        one word 
# \W        one non-word

# ^         start of string
# $         end of string
# \A        start of string, ignores m flag
# \Z        end of string, ignores m flag
# \b        word boundary
# \B        Non-word boundary
# [\b]      backspace character












## match
# Ex1
m = re.match('foo', 'food on the table') 
if m is not None:
    print m.group()
else:
    print "None"
# Ex2        
m = re.match('foo', 'seafood')
if m is not None:
    print m.group()
else:
    print "None"
# Ex3
bt = 'bat|bet|bit'
m = re.match(bt, 'bat')
if m is not None:
    print m.group()
else:
    print "None"
# Ex4
m = re.match(bt, 'He bit me')
if m is not None:
    print m.group()
else:
    print "None"

## search
# Ex
m = re.search('foo', 'seafood')
if m is not None:
    print m.group()
else:
    print "None"

m = re.search(bt, 'He bit me')
if m is not None:
    print m.group()
else:
    print "None"

m = re.match('\w\w\w-\d\d\d', 'abc-123')
print m.group()
print m.groups()
#print m.group(1)

m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
print m.group()
print m.groups()
print m.group(1)

m = re.match('(ab)', 'ab')
print m.group()
print m.groups()

m = re.match('(a)(b)', 'ab')
print m.group()
print m.groups()

m = re.match('(a(b))', 'ab')
print m.group()
print m.groups()

m = re.findall('car', 'carry the barcardi to the car')
print m

m = re.sub('[ae]', 'X', 'abcdef')
print m

m = re.subn('[ae]', 'X', 'abcdef')
print m
