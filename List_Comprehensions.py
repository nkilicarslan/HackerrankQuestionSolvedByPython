if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
list1 = []
list2 = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if([i,j,k] in list1) != True:
                list1.append([i,j,k])
for i in list1:
    if(sum(i) != n):
        list2.append(i)
print(list2)
### another way
print([a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n)