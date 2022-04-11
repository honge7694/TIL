words = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'NMO', 'PQRS', 'TUV', 'WXYZ']
result = 0

for x in words:
    for i in range(len(dial)):
        if x in dial[i]:
            result += i+3

print(result)