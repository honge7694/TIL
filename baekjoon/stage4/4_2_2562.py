# numbers = list(map(int, input().split()))
# max = numbers[0]
# cnt = numbers[0]

# for i, j in enumerate(numbers):
#     if j > max:
#         max = j
#         cnt = i+1

# print(max, cnt)

# numbers = [int(input()) for i in range(9)]
temp = int(input())
numbers = [int(input()) for i in range(temp)]
print(max(numbers))
print(numbers.index(max(numbers)) + 1)
