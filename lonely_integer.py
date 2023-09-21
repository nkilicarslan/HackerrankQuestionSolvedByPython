import os

def lonelyinteger(a):
    # create a dictionary to store the number of times a number appears
    dict_num = {}
    unique_elem = 0

    # loop through the array and check if the number is in the dictionary
    for number in a:
        if number not in dict_num:
            dict_num[number] = 1
        else:
            dict_num[number] += 1

    # loop through the dictionary and find the number appears once
    for number in dict_num:
        if dict_num[number] == 1:
            unique_elem = number

    # return the number that appears once
    return unique_elem


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
