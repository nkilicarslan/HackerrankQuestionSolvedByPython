from collections import Counter
number_of_shoes = int(input())
list_of_size_shoe = []
list_of_cost = []
amount_of_money = 0
my_list = list(map(int,input().split()))

counter_dict = Counter(my_list)

number_of_customers = int(input())
for i in range(number_of_customers):
    the_string = input()
    shoe_size, cost = the_string.split()
    list_of_size_shoe.append(shoe_size)
    list_of_cost.append(cost)
for i in range(number_of_customers):
    shoe_size = int(list_of_size_shoe[i])
    if (counter_dict[shoe_size] > 0):
        counter_dict[shoe_size] -= 1
        amount_of_money += int(list_of_cost[i])
    else:
        pass
print(amount_of_money)