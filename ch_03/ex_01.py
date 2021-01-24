hours = int(input("Enter hours:\n"))
rate = int(input("Enter rate\n"))
pay = hours * rate

if (hours > 40):
    print("Pay: ", pay * 1.5)
else:
    print("Pay: ", pay)
