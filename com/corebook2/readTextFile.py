# !/usr/bin/env Python
'readTextFile.py -- read and display text file'

# get filename
fname = raw_input('Enter filename: ')
print fname

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
    for eachLine in fobj:
        print eachLine,
    fobj.close()
except IOError, e:
    print "*** file open error:", e
