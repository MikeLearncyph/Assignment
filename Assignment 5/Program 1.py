import random
times =  int(input("Enter how many times u want to play: "))
total = 0
for i in range(times):
    dice = int(input("Enter dice to roll: "))
    total += random.randint(1, 6)
    print(total)
