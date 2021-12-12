arr = []
arr_score = []
arr_name = []
how_many_max = 0
min_value = 300
for i in range(int(input())):
    name = input()
    score = float(input())
    arr.append([name,score])
    arr_score.append(score)
for i in arr_score:
    if(i<min_value):
        min_value = i
for i in arr_score:
    if(i == min_value):
        how_many_max += 1
for i in range(0,how_many_max):
    arr_score.remove(min_value)
min_value = 300
for i in arr_score:
    if(i<min_value):
        min_value = i
for i,j in arr:
    if(min_value == j):
        arr_name.append(i)
arr_name.sort()
for i in arr_name:
    print(i)
