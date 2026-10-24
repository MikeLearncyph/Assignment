import random
def roll_dice(sides):
    return random.randint(1,sides)
def main():
    sides = int(input("Enter a number of sides: "))
    result = roll_dice(sides)
    print(result)
    while result != sides:
        result = roll_dice(sides)
        print(result)

main()
