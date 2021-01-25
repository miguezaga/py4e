fname = input("Enter a file name: ")
fhandle = open(fname)

d_days = dict()
for line in fhandle:
    words = line.split()
    if (len(words) == 0 or words[0] != "From"): continue
    d_days[words[2]] = d_days.get(words[2], 0) + 1

print(d_days)
