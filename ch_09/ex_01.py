file = input("Enter file name: ")
fhandler = open(file)

dic_words = dict()

for line in fhandler:
    sentence = line.split()

    for word in sentence:
        dic_words[word] = 'lolz'

print(dic_words)
