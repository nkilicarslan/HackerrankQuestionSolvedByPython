from itertools import product
first_list = list(map(int,input().split()))
second_list = list(map(int,input().split()))
cartesian_product_result = product(first_list,second_list)
for i in cartesian_product_result:
    print(i,end=" ")