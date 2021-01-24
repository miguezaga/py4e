file_name = input("Enter the file name: ")

if (file_name == "na na boo boo"):
    print("NA NA BOO BOO TO YOU - You have been punk'd!")

else:

    try:
        fhandler = open(file_name)
        count = 0
        for line in fhandler:
            count = count + 1
        print("There were %d subject lines in %s" % (count, file_name))

    except:
        print("File cannot be opened: %s" % file_name)
