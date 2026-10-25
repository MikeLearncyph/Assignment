def main ():
    airport = {}
    while True:
        pick = input ("Enter your choice , A (Enter a new Airport), B (Fetch Airport), C (Quit)")
        if pick == "A":
            codes = input("enter airport ICAO codes")
            name = input("enter airport name")
            airport[codes] = name
        elif pick == "B":
            codes = input ("enter ICAO codes")
            if codes in airport:
                print (airport[codes])
            else:
                print ("No airport")
        if pick in ("C", "c"):
            break
        else:
            print ("Enter a valid choice")
main()


