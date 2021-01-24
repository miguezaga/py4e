file_name = input("Enter a file name: ")
fhandler = open(file_name)
count = 0
for line in fhandler:
    words = line.split()
    if (len(words) == 0 or words[0] != "From"): continue
    print(words[1])
    count = count + 1

print("There were %d lines in the file with From as the first word" % count)
