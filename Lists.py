if __name__ == '__main__':
    N = int(input())
listt = list()
for i in range(N):
    func_to_be_implemented = input().split()
    if(func_to_be_implemented[0] == "insert"):
        listt.insert(int(func_to_be_implemented[1]),int(func_to_be_implemented[2]))
    elif(func_to_be_implemented[0] == "print"):
        print(listt)
    elif(func_to_be_implemented[0] == "remove"):
        listt.remove(int(func_to_be_implemented[1]))
    elif(func_to_be_implemented[0] == "append"):
        listt.append(int(func_to_be_implemented[1]))
    elif(func_to_be_implemented[0] == "sort"):
        listt.sort()
    elif(func_to_be_implemented[0] == "pop"):
        listt.pop()
    elif(func_to_be_implemented[0] == "reverse"):
        listt.reverse()