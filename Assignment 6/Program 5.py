def numbers(List):
    result = []
    for i in List:
        if i % 2 == 0:
            result.append(i)
    return result

def main():
    my_list = [1,2,3,4,5,6,7,8,9,10]
    new_list = numbers(my_list)
    print(my_list)
    print(new_list)

main()