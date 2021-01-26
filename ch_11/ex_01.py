import re

fname = "mbox.txt"
fhandle = open(fname)

re_input = input("Enter a regular expression: ")

count = 0
for line in fhandle:
    if (re.search(re_input, line)):
        count += 1

print("%s had %d lines that matched %s" % (fname, count, re_input) )
