from itertools import permutations
the_string, number = input().split()
sorted_string = list(the_string)
sorted_string.sort()
permutations_sorted_list = list(permutations(sorted_string,int(number)))
for elem in permutations_sorted_list:
    print("".join(elem))
