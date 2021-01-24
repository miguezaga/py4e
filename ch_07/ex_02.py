file_name = input("Enter a file name: ")
fhandler = open(file_name)
total = 0
count = 0
for line in fhandler:
    if (line.find("X-DSPAM-Confidence:") == -1): continue
    total = total + float(line.rstrip()[-6:])
    count = count + 1
average = total / count
print("Average spam confidence: ", average)
