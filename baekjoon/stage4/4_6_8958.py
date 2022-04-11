temp = int(input())
grade = [input() for i in range(temp)]
count = 0
plus = 1

for idx, i in enumerate(grade):
    for j in grade[idx]:
        if j == 'O':
            count += plus
            plus += 1
        elif j == 'X':
            plus = 1

    print(count)
    count = 0
    plus = 1

