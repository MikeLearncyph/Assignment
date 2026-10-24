def unit(diameter, price):
    area = 3.14159 * (diameter/ 2) **2
    return price/area * 10000
def main():
    d1 = float(input("Enter the diameter 1 piz(cm): "))
    p1 = float(input("Enter the price 1 piz(euro): "))
    d2 = float(input("Enter the diameter 2 piz(cm): "))
    p2 = float(input("Enter the price 2 piz(euro): "))
    unit1 = unit(d1, p1)
    unit2 = unit(d2, p2)

    if unit1 < unit2:
        print ("Pizza 1 better value than 2")
    elif unit1 > unit2:
        print ("Pizza 2 better value than 1")
    else:
        print ("same thing")
main()