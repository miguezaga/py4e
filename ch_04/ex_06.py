def computepay (hours, rate):

    try:
        pay = hours * rate

        if (hours > 40):
            print("Pay: ", pay * 1.5)
        else:
            print("Pay: ", pay)
    except:
        print("Error, please enter numeric input")

computepay("MANDELA", 10)
