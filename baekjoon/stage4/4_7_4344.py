# n = int(input())

# for i in range(n):
#     numbers = list(map(int,input().split()))
#     avg = sum(numbers[1:]) / numbers[0]
#     cnt = 0
#     for j in numbers[1:]:
#         if j > avg:
#             cnt += 1
    
#     result = cnt/numbers[0] * 100
#     print(f'{result:.3f}%')


n = int(input())
numbers = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    avg = sum(numbers[i][1:]) / numbers[i][0]
    cnt = 0

    for j in numbers[i]:
        if j > avg:
            cnt += 1
    
    result = cnt / numbers[i][0] * 100
    print(f'{result:0.3f}%')