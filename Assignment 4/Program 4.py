import random

number1  = random.randint(1, 10)
number = int(input("Enter a number: "))

while number!=number1:
    if number1 > number:
        print("too low")
        number = int(input("Enter a number: "))
    elif number > number1:
        print("too high")
        number = int(input("Enter another number: "))
    if number == number1:
        print("Correct")