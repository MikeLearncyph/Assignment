while True:
    fish = int(input("pleace input the length of the zander fish: "))
    if fish < 42:
        left = 42 - fish
        print (f"release the fish to the lake! The fish is {left} cm below the limit")
    else:
        print ("you meet the limit")
        break
        