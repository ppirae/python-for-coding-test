h = int(input())
count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i)+str(j)+str(k):
                count += 1

            # 나는 이렇게 생각했다
            # if str(i)=='3' or str(j)=='3' or str(k)=='3':
            # count += 1
            # 이렇게하면 13분, 23분 등은 체크가 안되서 오답이다.

print(count)
