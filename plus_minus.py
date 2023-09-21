def plusMinus(arr):
    # create a list to store the number of positive, negative and zero values
    number_of_counts = [0,0,0]
    # loop through the array and check if the number is positive, negative or zero
    for number in arr:
        if number > 0:
            number_of_counts[0] += 1
        elif number < 0:
            number_of_counts[1] += 1
        else:
            number_of_counts[2] += 1
    # calculate the total value of the array
    total_value = len(arr)
    # print the ratio of positive, negative and zero values
    print("{:.6f}".format(number_of_counts[0]/total_value))
    print("{:.6f}".format(number_of_counts[1]/total_value))
    print("{:.6f}".format(number_of_counts[2]/total_value))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
