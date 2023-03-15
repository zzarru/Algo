N = 9
lst = [list(map(int, input().split())) for _ in range(N)]

# 최댓값 구하기
cnt = -1
for i in range(N):
    for j in range(N):
        if lst[i][j] > cnt:
            cnt = lst[i][j]
            x, y = i+1, j+1

print(cnt)
print(x, y)