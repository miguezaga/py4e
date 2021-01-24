file_name = input("Enter a file name: ")
fhandler = open(file_name)
for line in fhandler:

    print(line.rstrip().upper())
