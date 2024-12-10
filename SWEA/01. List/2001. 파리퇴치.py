T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())

    lst = [list(map(int, input().split())) for _ in range(N)]

    di = []
    dj = []
    for i in range(M):
        for j in range(M):
            di.append(i)
            dj.append(j)

    total_kill = []
    for i in range(N+1-M):
        for j in range(N+1-M):
            kill = 0
            for k in range(M*M):
                ni = i + di[k]
                nj = j + dj[k]
                kill = kill + lst[ni][nj]
            total_kill.append(kill)


    print(f'#{test} {max(total_kill)}')