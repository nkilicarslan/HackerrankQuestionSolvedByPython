def average(array):
    total_count = 0
    how_many_numbers = len(set(array))
    for elem in set(array):
        total_count += elem
    average_number = float(total_count)/how_many_numbers
    return average_number

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)