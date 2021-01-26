fname = input("Enter a file name: ")
fhandle = open(fname)

d = dict()
for line in fhandle:
    words = line.split()

    if (len(words) == 0 or words[0] != "From"): continue

    mail = words[1]
    d[mail] = d.get(mail, 0) + 1

l = list()
for mail, count in list(d.items()):
    l.append( (count, mail) )
    l.sort(reverse=True)


for key, val in l[0:1]:
    print(val, key)
