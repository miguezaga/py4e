fname = input("Enter a file name: ")
fhandle = open(fname)

d_school = dict()

for line in fhandle:
    words = line.split()
    if (len(words) == 0 or words[0] != "From"): continue

    mail = words[1]
    startpos = mail.find("@")

    school = (mail[startpos + 1:])
    d_school[school] = d_school.get(school, 0) + 1

print(d_school)    
