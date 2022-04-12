temp = input()
# alp_list = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
alp_list = [-1] * 26
count = 0

for i in temp:
    id = ord(i) - 97

    if alp_list[id] == -1:
        alp_list[id] = count
    count += 1

[print(j, end= ' ') for j in alp_list]





