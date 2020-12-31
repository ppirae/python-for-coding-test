n, k = map(int,input().split(" "))
result = 0

# N이 K 이상이라면 계속 나누기
while n >= k:
    if n % k != 0:
        n -= 1
        result += 1
    else:
        n //= k
        result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)
