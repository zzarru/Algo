# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def exitMaze(si, sj):
    queue = []
    visited = [[0]*N for _ in range(N)]
    queue.append((si,sj))
    visited[si][sj] = 1

    while queue:
        ci, cj = queue.pop(0)
        if maze[ci][cj] == 3:
            return visited[ci][cj] - 2

        # 4방향, 범위 내 , 1이 아니면 큐에 삽입한다.
        for di, dj in ((-1,0), (1,0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and maze[ni][nj] !=1:
                queue.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1

    return 0


T = int(input())
for test in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 출발 위치 좌표 구하기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j


    ans = exitMaze(si, sj)
    print(f'#{test} {ans}')