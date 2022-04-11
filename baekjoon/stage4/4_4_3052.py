tmp = [int(input()) for i in range(10)]
result = [i % 42 for i in tmp]
result = set(result)

print(len(result))