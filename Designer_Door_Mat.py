length,widht = int(input()),int(input())

for i in range(1,length+1):
    list1 = []
    if(i>=1 and i<length/2):
        list1.append("-"*((widht-(6*i-3))//2))
        list1.append(".|."*(2*i-1))
        list1.append("-"*((widht-(6*i-3))//2))
        print("".join(list1))
    elif(i == (length+1)/2):
        list1.append("-"*((widht-7)//2))
        list1.append("WELCOME")
        list1.append("-" * ((widht - 7) // 2))
        print("".join(list1))
    else:
        list1.append("-" * (((widht-((length-i)*6+3)))//2))
        list1.append(".|."*(2*(length-i)+1))
        list1.append("-" * (((widht - ((length - i) * 6 + 3))) // 2))
        print("".join(list1))