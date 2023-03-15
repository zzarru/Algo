from collections import deque

T = int(input())
for test in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    # 시작, 도착 좌표 구하기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                Si, Sj = i, j
            if maze[i][j] == '3':
                Gi, Gj = i, j

    # 델타 탐색 좌표 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 시작 점을 Q에 넣어주고 시작한다.
    Q = deque([(Si, Sj)])

    while Q:
        Ci, Cj = Q.popleft()
        for k in range(4):
                ni = Ci + di[k]
                nj = Cj + dj[k]

                if 0 <= ni < N and 0 <= nj < N:
                    # 델타탐색을 통해 인접 구역을 조사하고 방문한 적이 없으면 Q에 넣어준다.
                    if maze[ni][nj] == '0' or maze[ni][nj] == '3':
                        Q.append((ni, nj))
                        maze[ni][nj] = '1' # 방문한 구역은 1로 바꿔준다.

    if maze[Gi][Gj] == '1':
        print(f'#{test} 1')
    else:
        print(f'#{test} 0')