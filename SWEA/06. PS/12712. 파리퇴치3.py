T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    #델타탐색 (+)
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    max_kill = 0
    for i in range(N):
        for j in range(N):
            kill = flies[i][j]
            for k in range(4):
                for l in range(1, M):
                    si = i + di[k]*l
                    sj = j + dj[k]*l

                    if 0 <= si < N and 0 <= sj < N:
                        kill += flies[si][sj]
            if kill > max_kill:
                max_kill = kill



    ci = [-1, -1, 1, 1]
    cj = [-1, 1, -1, 1]
    for i in range(N):
        for j in range(N):
            kill = flies[i][j]
            for k in range(4):
                for l in range(1, M):
                    si = i + ci[k]*l
                    sj = j + cj[k]*l

                    if 0 <= si < N and 0 <= sj < N:
                        kill += flies[si][sj]
            if kill > max_kill:
                max_kill = kill

    print(f'#{test} {max_kill}')