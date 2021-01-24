total = 0
count = 0

while (True):
    number = input("Enter a number: ")

    if (number == "done"):
        break

    try:
        number = int(number)
        total = total + number
        count = count + 1
    except:
        print("Invalid input")

average = total / count

print(total, count, average)
