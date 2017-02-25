#!/usr/bin/env  python

f = open("ztest.txt", "a")
print >> f, "aha"           # Python 2.X only
f.close()



fzen = open("zen of python.txt", "r")   
l = fzen.read()             # reads everything into a str, with "\n" attached at the end. Can specify size.
                            # returns "" if read() on EOF.
print l                                   # Everything, with extra "\n" at the end.
#print isinstance(l, str)                  # True
#print l[-1] == "\n"                       # True
#print fzen.read() == ""                   # True  
fzen.close()




fzen2 = open("zen of python.txt")    # r mode by default
l = fzen2.readline()        # reads a single line into a str, with "\n" attached at the end.
                            # if readline() returns an empty string, EOF has been reached.
#print l                                   # Frist line
#print isinstance(l, str)                  # True
print fzen2.readline()
#fzen2.read()
#print fzen2.readline() == ""               # True
fzen2.close()




fzen3 = open("zen of python.txt")
for line in fzen3:
    print line

print 1
print 2

import time
def tail(f):
    f.seek(0, 2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        print hello
        yield line

def grep(lines, searchtext):
    for line in lines:
        if searchtext in line:
            yield line

wwwlog = tail(open("zen of python.txt"))
pylines = grep(wwwlog, "python")
for line in pylines:
    print line,
