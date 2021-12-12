def count_substring(string, sub_string):
    count = 0
    other_count = 0
    for i in range((len(string)-len(sub_string)+1)):
        if(string[i] == sub_string[0]):
            for j in range(len(sub_string)-1):
                if(string[i+1]==sub_string[j+1]):
                    i += 1
                    other_count +=1
                    if (other_count + 1 == len(sub_string)):
                        count += 1
                    continue
            other_count = 0



    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)