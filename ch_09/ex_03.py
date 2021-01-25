fname = input("Enter a file name: ")
fhandle = open(fname)

d_mail = dict()

for line in fhandle:
    words = line.split()

    if (len(words) == 0 or words[0] != "From"): continue
    mail = words[1]

    d_mail[mail] = d_mail.get(mail, 0) + 1

print(d_mail)
