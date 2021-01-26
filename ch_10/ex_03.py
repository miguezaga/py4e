import string

fname = input("Enter a file name: ")
fhandle = open(fname)

letters = dict()
for line in fhandle:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation + " "))
    line = line.lower()

    for letter in line:
        letters[letter] = letters.get(letter, 0) + 1

l = list()
for letter, count in list(letters.items()):
    l.append( (count, letter) )

l.sort(reverse=True)

total = 0
for count, letter in l:
    total = total + int(count)

for count, letter in l:
    print(letter, round(count / total, 2))
