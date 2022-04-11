# user_input = list(map(str, input().split()))
# reverse_input = ''
# reverse_list = []

# for i in range(len(user_input)):
#     for j in user_input[i]:
#         reverse_input = j + reverse_input
#     reverse_list.append(reverse_input)
#     reverse_input = ''

# print(max(reverse_list))

num1, num2 = input().split()

num1 = int(num1[::-1])
num2 = int(num2[::-1])

print(num1) if num1 > num2 else print(num2)