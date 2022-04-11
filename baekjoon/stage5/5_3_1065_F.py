input_num = int(input())
hansu = 0

# 1. 자릿수를 구한다. => temp 필요.
# 2. 3자리 이상이면 그 때부터 비교.
# 3. 한수 count가 필요
# 4. 2자리 이하면 input_num의 값
# 5. 

for i in range(1, input_num+1):
    if i < 100 :
        hansu += 1
    elif i >= 1000:
        break
    else:
        numlist = list(map(int, str(i)))

        if numlist[0] - numlist[1] == numlist[1] - numlist[2]:
            hansu += 1

print(hansu)

        
