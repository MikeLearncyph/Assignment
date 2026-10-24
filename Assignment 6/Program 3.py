def gallons (liters):
    return liters * 3.785
def main():
    while(True):
        liters = float(input("input the number of gallons: "))
        if liters < 0:
            break
        numbers = gallons(liters)
        print (f"{liters} gallons is {numbers}")

main()

