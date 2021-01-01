n = int(input())
plans = list(map(str,input().split(" ")))
N = 1
M = 1

for step in plans:
    if step == 'R' and M != n:
        M += 1
    elif step == 'L' and M != 1:
        M -= 1
    elif step == 'U' and N != 1:
        N -= 1
    elif step == 'D' and N != n:
        N += 1
    else:
        continue

print(N,M)
