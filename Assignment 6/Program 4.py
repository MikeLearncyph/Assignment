def numbers(list):
    total = 0
    for number in list:
        total += number
    return total

def main():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = numbers(my_list)
    print(result)

main()