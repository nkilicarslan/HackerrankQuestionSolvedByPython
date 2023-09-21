import os

def countingSort(arr):
    # create an array to store the number of times a value appears in the array
    res_arr = [0] * 100
    # loop through the array and store the number of times a value appears in the array
    for value in arr:
        res_arr[value] += 1
    # return the array
    return res_arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
