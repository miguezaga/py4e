max_n = None
min_n = None

while (True):
    number = input("Enter a number: ")

    if (number == "done"):
        break

    try:
        number = int(number)

        if (max_n == None or max_n < number):
            max_n = number

        if (min_n == None or min_n > number):
            min_n = number
    except:
        print("Invalid input")

print(max_n, min_n)
