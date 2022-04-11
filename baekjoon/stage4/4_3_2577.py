# a = int(input())
# b = int(input())
# c = int(input())

# result = a * b* c
# cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# for i in str(result):
#     if i == '0':
#         cnt[0] += 1
#     if i == '1':
#         cnt[1] += 1
#     if i == '2':
#         cnt[2] += 1
#     if i == '3':
#         cnt[3] += 1
#     if i == '4':
#         cnt[4] += 1
#     if i == '5':
#         cnt[5] += 1
#     if i == '6':
#         cnt[6] += 1
#     if i == '7':
#         cnt[7] += 1
#     if i == '8':
#         cnt[8] += 1
#     if i == '9':
#         cnt[9] += 1

# for idx, i in enumerate(cnt):
#     print(f'{cnt[idx]}')

a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))

for i in range(10):
    print(result.count(str(i)))