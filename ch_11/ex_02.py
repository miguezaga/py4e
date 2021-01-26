import re

fname = input("Enter file name: ")
fhandle = open(fname)

count = 0
total = 0
l = list()
for line in fhandle:
    line = line.rstrip()
    if(re.search("^New Revision", line)):
        l.append(int(re.findall("[0-9]+", line)[0]))

print(int(sum(l) / len(l)))
