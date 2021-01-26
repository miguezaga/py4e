import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo-full.txt')
char_count = 0
for line in fhand:
    line = line.decode().strip()
    if char_count < 300:
        print(line)
    char_count += len(line)
print(char_count)
