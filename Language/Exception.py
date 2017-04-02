### (1)except ErrorName handles that specific error. One and only one exception is handled.
### (2)except with no errorname handles all the exceptions not handled by previous excepts.
### (3)else is executed if no exception occurs. This is better than putting codes in try clause.
### (4)finally is executed regardless of whether or not exceptions occur.
### (5)raise is used when you need to determine wheter an exception was raised but dont intend to handle it.


## Ex.1
while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print "Oops! That was no valid number. Try again..."

## Ex.2
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}):{1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise


    
## Ex.3
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()

## Ex.4
(x, y) = (5, 0)
try:
    z = x/y
except ZeroDivisionError:
    print "divide by zero"

## Ex.5
"""
try:
    do_some_stuff()
except:                 # catch all exceptions
    rollback()
    raise               # raise without an argument re-raise the last exception
else:
    commit()
finally:
    cleanup_stuff()
