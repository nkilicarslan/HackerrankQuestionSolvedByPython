if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_of_list = max(arr)
    how_many_max = 0
    for i in arr:
        if(i == max_of_list):
            how_many_max += 1
    for i in range(0,how_many_max):
        arr.remove(max_of_list)
    print(max(arr))
