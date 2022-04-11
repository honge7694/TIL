count = int(input())
temp = [input().split() for i in range(count)]

for i in temp:
    for j in i[1]:
        print(j * int(i[0]), end='')
    print()