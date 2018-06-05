import random

randint=random.randint(0,10)
userin=int(input("Guess the digit: "))
if randint == userin:
    print("Your answer is PERFECT!! Congratulations!!")
elif randint > userin:
    print("Your answer is low than  required")
elif randint < userin:
    print("Your answer is high than  required")
