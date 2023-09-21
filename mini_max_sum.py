def miniMaxSum(arr):
    # get the max and min value of the array
    max_value = max(arr)
    min_value = min(arr)
    # calculate the total value of the array
    total_value = sum(arr)
    # print the total value of the array minus the max and min value
    print(str(total_value-max_value) + " " + str(total_value - min_value))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
