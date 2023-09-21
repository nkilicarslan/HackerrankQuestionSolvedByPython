import os

def diagonalDifference(arr):
    # get the length of the matrix
    matrix_length = len(arr)
    left_diag_sum = 0
    right_diag_sum = 0
    left_index = 0
    right_index = matrix_length - 1
    # loop through the matrix and get the sum of the left and right diagonal
    for row in arr:
        left_diag_sum += row[left_index]
        right_diag_sum += row[right_index]
        left_index += 1
        right_index -= 1
    # return the absolute difference of the left and right diagonal
    return abs(left_diag_sum - right_diag_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
