enter = 0
while enter < 5:
    username = input("Enter your name: ")
    password = input("Enter your password: ")
    enter += 1
    if enter >= 5:
        print("Access Denied")

    if username == "python" and password == "rules":
        print("Welcome")
        break
