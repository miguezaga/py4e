numbers_list = list()
while (True):
    number = input("Enter a number: ")

    if (number == "done"): break

    try:
        numbers_list.append(int(number))

    except:
        print("Invalid input")

print("Maximum: ",max(numbers_list))
print("Minimum: ", min(numbers_list))
