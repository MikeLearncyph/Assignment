number = input ("Enter a number: ")
if number != "":
    smaller = float (number)
    larger = float (number)
while number != "":
    some = float(number)
    if smaller > some:
        smaller = some
    if larger < some:
        larger = some
    number = input ("Enter a number: ")
print("smallest: ", smaller)
print("larger: ", larger)

