fhand = open('mbox-short.txt') # maybe it needs to chek if the file is there
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue # Maybe it says 'from' but has no sender

"""
The next line guards against the case that the line starts with from
but there are not any words after
"""
    if len(words) < 3 : continue


    print(words[2]) # maybe this line needs to check if it is a week day
