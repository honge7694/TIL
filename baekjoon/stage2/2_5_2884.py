H, M = map(int, input().split())

if M <= 44 :
    if H <= 0 :
        H = 24 + H - 1
        M = 60 + M - 45
    else:
        H -= 1
        M = 60 + M - 45
else:
    M = M - 45

print(f"{H} {M}")