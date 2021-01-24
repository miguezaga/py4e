import random

def computegrade (score):

    try:

        if (score >= 0 and score <= 1):
            if (score >= 0.9):
                grade = "A"
            elif (score >= 0.8):
                grade = "B"
            elif (score >= 0.7):
                grade = "C"
            elif (score >= 0.6):
                grade = "D"
            else:
                grade = "F"

            print(grade)

        else:
            print("The number has to be between 0.0 and 1.0")

    except:
        print("Bad score")

for i in range(10):
    computegrade(random.random())

computegrade("bear")
