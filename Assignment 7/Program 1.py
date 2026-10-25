def main ():
    seasons = ("Winter", "Spring", "Summer", "Fall")
    month = int(input("Enter a month: "))

    if month == 12 or month <= 2:
        print (seasons[0])
    elif month <= 5:
        print (seasons[1])
    elif month <= 8:
        print (seasons[2])
    else:
        print (seasons[3])
main()