count = int(input())
grade = list(map(int, input().split()))
result = 0

m_grade = max(grade)

for i in grade:
    result += (i / m_grade * 100)

print(result/count)