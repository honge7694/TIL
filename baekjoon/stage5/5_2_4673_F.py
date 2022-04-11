# def selfNumber(a):
#     b = str(a)
#     temp = 0
    
#     for i in b:
#         temp += int(i)
    
#     if int(b) > 10000:
#         return b
        
#     b = int(b) + temp
#     print(b)
    
    
#     return selfNumber(b)

# number = int(input())
# selfNumber(number)

natural_num = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

self_num = sorted(natural_num - generated_num)
for i in self_num:
    print(i)