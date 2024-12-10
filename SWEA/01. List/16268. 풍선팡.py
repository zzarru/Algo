T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    total_lst = []
    for i in range(N):
        for j in range(M):
            neighbor_sum = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    neighbor_sum = neighbor_sum + lst[ni][nj]


            total = neighbor_sum + lst[i][j]
            total_lst.append(total)

    print(f'#{test} {max(total_lst)}')



