if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
the_values = student_marks[query_name]
sum = 0
for i in the_values:
    sum += i
sum = sum/len(the_values)
sum = "{:.2f}".format(sum)
print(sum)