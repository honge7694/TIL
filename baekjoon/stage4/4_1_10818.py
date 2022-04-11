count = int(input())
numbers = list(map(int, input().split()))

max = numbers[0]
min = numbers[0]

for i in numbers:
    print(f'i = {i}')
    if i > max:
        max = i
        print(f'max = {max}')
    
    elif i < min:
        min = i
        print(f'min = {min}')

print(max, min)