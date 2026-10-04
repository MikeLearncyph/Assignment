while True:
    cabin = input('please enter your cabin class: ')
    if cabin == "A":
        print ("above the car deck, equipped with a window")
    elif cabin == "B":
        print ("windowless cabin above the car deck")
    elif cabin == "C":
        print ("windowless cabin below the car deck")
    elif cabin == "LUX":
        print ("upper-deck cabin with a balcony")
    else:
        print ("Invalid cabin class")