numbers =[]
number = input("Enter a number: ")
while number != "":
    numbers = numbers + [float(number)]
    number = input("Enter a number: ")
numbers.sort(reverse=True)
for number in numbers [:5]:
    print (number)



