file_name = input('Enter file: ')
fhandler = open(file_name)

all_words = list()

for line in fhandler:
    line_words = line.split()

    for word in line_words:
        if (word in all_words): continue
        else:
            all_words.append(word)

all_words.sort()

print(all_words)
