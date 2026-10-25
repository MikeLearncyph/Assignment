def main():
    names = set()
    while True:
        name = input("Please enter your name: ")
        if name == "":
            break
        if name in names:
            print("exists")
        else:
            print("New name")
            names.add(name)
    for name in names:
        print(name)
main()