def timeConversion(s):
    # if the input is in AM
    if s[8] == "A":
        # split the string into a list
        splitted_str = s[:-2].split(":")
        # if the hour is greater than 11, add 12 to the hour and mod it by 24
        if int(splitted_str[0]) > 11:
            splitted_str[0] = str((int(splitted_str[0]) + 12) % 24)
            # if the hour is less than 10, add a 0 to the front of the hour
            if int(splitted_str[0]) < 10:
                splitted_str[0] = "0" + splitted_str[0]
            return ":".join(splitted_str)
        return s[:-2]
    else:
        # if the input is in PM
        splitted_str = s[:-2].split(":")
        # if the hour is less than 12, add 12 to the hour and mod it by 24
        if int(splitted_str[0]) < 12:
            splitted_str[0] = str((int(splitted_str[0]) + 12) % 24)
            # if the hour is less than 10, add a 0 to the front of the hour
            if int(splitted_str[0]) < 10:
                splitted_str[0] = "0" + splitted_str[0]
            return ":".join(splitted_str)
        return s[:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
