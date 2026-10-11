number = float(input("Enter a number to exchange: "))
while number >= 0:
    cm = number * 2.54
    print(f"{number} inches = {cm} cm")
    number = float(input("Enter a number to exchange: "))
    if number <= 0:
        break
