import random
points = int(input("How many random points: "))

drops = 0
count = 0
while count < points:
    x = random.randint(- 1,1)
    y = random.randint(- 1,1)
    if x ** 2 + y ** 2 < 1:
        drops += 1

        count += 1
pi = 4 * drops / points
print("pi: ", pi)