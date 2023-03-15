t = int(input()) # 테스트 케이스

for i in range(t):
    n = int(input()) # 가로 길이
    h = list(map(int, input().split())) # 건물 높이

    highest = 0
    for j in range(n):
        cnt = 0
        for l in range(j+1,n):
            if h[j] <= h[l]:
                cnt += 1

        if (n-1) - j - cnt > highest:
            highest = n-1 - j - cnt

    print(f'#{i+1} {highest}')