def lonelyinteger(a):

    dict_num = {}
    unique_elem = 0

    for number in a:
        if number not in dict_num:
            dict_num[number] = 1
        else:
            dict_num[number] += 1

    for number in dict_num:
        if dict_num[number] == 1:
            unique_elem = number

    return unique_elem


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
