fname = input("Enter a file name: ")
fhandler = open(fname)

d = dict()
for line in fhandler:
    words = line.split()

    if (len(words) == 0 or words[0] != "From"): continue

    hour = words[5].split(":")[0]

    d[hour] = d.get(hour, 0) + 1

l = list()
for hour, count in list(d.items()):
    l.append( (hour, count) )

l.sort()

for hour, count in l:
    print(hour, count)
